from datetime import datetime, date, timedelta

class currentState:
    def __init__(self, interval_length):
        if not interval_length == None:
            self.interval_length = interval_length
            
            
class Clock:
    work_time = None
    short_break = None
    long_break = None


