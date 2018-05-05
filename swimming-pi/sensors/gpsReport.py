import datetime

class gpsReport(object):

    def __init__(self):
         self.lat = 0
         self.lon = 0
         self.alt = 0
         self.speed = 0
         self.time = datetime.datetime.utcnow().isoformat()
