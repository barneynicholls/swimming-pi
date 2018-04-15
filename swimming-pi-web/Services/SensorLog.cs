using swimming_pi_web.Models;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace swimming_pi_web.Services
{
    public class SensorLog
    {
        public static IEnumerable<SensorReading> Process(string fileName)
        {
            List<SensorReading> readings = new List<SensorReading>();

            using (StreamReader file = new StreamReader(fileName))
            {
                string line;
                //2018-04-13T06:53:20.002Z,21.687,50.18061163,-4.977751431,0.1512
                while ((line = file.ReadLine()) != null)
                {
                    var tokens = line.Split(",", StringSplitOptions.RemoveEmptyEntries);

                    readings.Add(new SensorReading()
                    {
                        Time = DateTime.Parse(tokens[0]),

                        Temp = Decimal.Parse(tokens[1]),
                        Lat = Decimal.Parse(tokens[2]),
                        Lon = Decimal.Parse(tokens[3]),
                        Speed = Decimal.Parse(tokens[4]),

                    });

                }

                file.Close();
            }

            return NormaliseData(readings);
        }

        private static IEnumerable<SensorReading> NormaliseData(IEnumerable<SensorReading> readings)
        {
            const int rounding = 7;


            // group into 14 bands
            const int bands = 14;

            var speedMin = readings.Min(r => r.Speed);
            var speedBand = (readings.Max(r => r.Speed) - speedMin) / bands;


            var groupedToLocation = from r in readings
                                    group r by new { Lat = Math.Round(r.Lat, rounding), Lon = Math.Round(r.Lon, rounding) } into g
                                    select new SensorReading
                                    {
                                        Lat = g.Key.Lat,
                                        Lon = g.Key.Lon,
                                        Temp = g.Average(x => x.Temp),
                                        Speed = g.Average(x => x.Speed),
                                        Time = g.Min(x => x.Time),
                                        SpeedWeight = Math.Floor( (g.Average(x => x.Speed) - speedMin) / speedBand)
                                    };

            return groupedToLocation;
        }
    }
}
