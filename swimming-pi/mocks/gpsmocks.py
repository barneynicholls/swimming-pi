class MockGPS(object):
    self.WATCH_ENABLE = 1
    self.WATCH_NEWSTYLE = 2

    """mock gps"""
    def gps(self,host,port):
        self.host = host
        self.port = port
        return MockGPSSession()

class MockGPSSession(object): 

    """mock session stream"""
    def stream(self,flags):
        self.flags = flags

    """mock session stream next() method"""
    def next(self):
        return (10,20)


#import gpxpy
#import gpxpy.gpx
