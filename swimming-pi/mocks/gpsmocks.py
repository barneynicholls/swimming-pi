import random

class MockGPS(object):
    WATCH_ENABLE = 1
    WATCH_NEWSTYLE = 2

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
        return MockGPSReport()

class MockGPSReport(object):



    def __init__(self):
        random.seed()
        self.lat = random.randint(-900000,900000) / 10000
        self.lon = random.randint(-1800000,1800000) / 10000

