try:
    import gps
    import gpxpy
    import gpxpy.gpx
except ImportError:
    from mocks import MockGPS
    gps = MockGPS()
import logging
import time
from time import gmtime

class gyneo6mv2(object):

    def read(self):
        report = self.session.next()
        return (report.lat, report.lon, gmtime())

    def __init__(self):
        #Listen on port 2947 of gpsd
        self.session = gps.gps()
        #self.session = gps.gps("localhost", "2947")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    
    def read(self):
        result = (0,0,0)
        try:
            report = self.session.next();
            return (report.lat, report.lon, report.time)
        except:
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