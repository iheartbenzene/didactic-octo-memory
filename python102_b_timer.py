from datetime import datetime, date, timedelta
from gi.repository import Notify

class currentState:
    def __init__(self, interval_length):
        if not interval_length == None:
            self.interval_length = interval_length
            
            
class Clock:
    work_time = None
    short_break = None
    long_break = None
    
    work_sessions = 4
    remaining_sessions = work_sessions
    remaining_breaks = work_sessions - 1
    right_now = None
    end_time = None
    
    def __init__(self, work_time, short_break_time, long_break_time):
        if (work_time or short_break_time or long_break_time) == None:
            exit(1)
        self.work_time = currentState(work_time)
        self.short_break = currentState(short_break_time)
        self.long_break = currentState(long_break_time)
        self.states = [self.work_time, self.short_break, self.long_break]
        
    def change_event(self):
        if not self.right_now == None and not self.right_now in self.states:
            exit(1)
        
        timer_title = ''
        time_string = 'End time:> '
        
        if self.right_now == None:
            self.right_now = self.work_time
            timer_title = 'Actively Working'
            
        elif self.right_now == self.work_time:
            self.remaining_sessions -= 1
            if self.remaining_breaks == 0:
                self.right_now = self.long_break
                timer_title = 'Take a long break.'
            else:
                self.right_now = self.short_break
                timer_title = 'Take a short break.'
                
        elif self.right_now == self.short_break:
            self.remaining_breaks -= 1
            self.right_now = self.work_sessions
            timer_title = 'Actively Working'
            
        elif self.right_now == self.long_break:
            self.right_now = self.work_sessions
            timer_title = 'Actively Working'
            self.remaining_sessions = self.work_sessions
            self.remaining_breaks = self.remaining_sessions - 1
        
        self.end_time = datetime.now + timedelta(self.right_now.interval_length)
        time_string += self.end_time.strftime("%H:%M:%S")
        