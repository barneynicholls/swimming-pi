import random
import datetime

class MockGPS(object):
    WATCH_ENABLE = 1
    WATCH_NEWSTYLE = 2
    MPS_TO_KPH = 2

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

    """mock session report"""
    def __init__(self):
        random.seed()
        self.lat = random.randint(-900000,900000) / 10000
        self.lon = random.randint(-1800000,1800000) / 10000
        self.speed = random.randint(0,100000) / 10000
        self.time = datetime.datetime.utcnow().isoformat()
        self.Items = { "class" : "TPV"}

    def __getitem__(self, item):
        return self.Items[item]