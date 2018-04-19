﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace swimming_pi_web.Models
{
    public class SensorReading
    {
        public DateTime Time { get; set; }

        public decimal Lat { get; set; }
        public decimal Lon { get; set; }

        public decimal Temp { get; set; }
        public decimal Speed { get; set; }

        public string SpeedColor { get; set; }

        public string TempColor { get; set; }
    }
}
