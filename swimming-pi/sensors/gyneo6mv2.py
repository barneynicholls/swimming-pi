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
        gpsReport = gpsReport()

        try:
            report = self.session.next();
            if report is not None and report['class'] == 'TPV':
                if 'lat' in report:
                    gpsReport.lat = report.lat
                if 'lon' in report:
                    gpsReport.lon = report.lon
                if 'speed' in report:
                    gpsReport.speed = report.speed * gps.MPS_TO_KPH
                if 'time' in report:
                    gpsReport.time = report.time
                if 'alt' in report:
                    gpsReport.alt = report.alt
            return gpsReport
        except Exception as e:
            logging.error(str(e))
            return gpsReport

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