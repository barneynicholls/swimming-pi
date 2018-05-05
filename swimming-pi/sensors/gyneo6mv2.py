try:
    import datetime
    import gps
except ImportError:
    from mocks import MockGPS
    gps = MockGPS()
import logging
import time
from time import gmtime
from sensors import gpsReport

class gyneo6mv2(object):

    def read(self):
        report = self.session.next()
        return (report.lat, report.lon, gmtime())

    def __init__(self):
        #Listen on port 2947 of gpsd
        self.session = gps.gps("localhost", "2947")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    
    def read(self):

        result = gpsReport.gpsReport()

        try:
            report = self.session.next();
            if report is not None and report['class'] == 'TPV':
                if 'lat' in report:
                    result.lat = report.lat
                if 'lon' in report:
                    result.lon = report.lon
                if 'speed' in report:
                    result.speed = report.speed * gps.MPS_TO_KPH
                if 'time' in report:
                    result.time = report.time
                if 'alt' in report:
                    result.alt = report.alt
            return result
        except Exception as e:
            logging.error(str(e))
            return result

    #def read(self):
    #    result = (0,0)

    #    try:
    #        report = self.session.next()
		  #  # wait for a 'TPV' report and display the current time
		  #  # to see all report data, uncomment the line below
		  #  #print report
		  #  if report['class'] == 'TPV':
    #            result = (report.lat,report.lon)
    #            break
	   # except StopIteration:
		  #  self.session = None
		  #  logging.error("GPSD has terminated")
    #    return result