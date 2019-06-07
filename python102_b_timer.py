import argparse
import subprocess
import sys

from time import sleep
from datetime import datetime, date, timedelta

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
        
    def notifications(self, message):
        subprocess.Popen(['notify-send', message])
        return    
    
    
    def change_event(self):
        if not self.right_now == None and not self.right_now in self.states:
            exit(1)
        
        timer_title = ''
        time_string = 'End time:> '
        
        if self.right_now == None:
            self.right_now = self.work_time
            timer_title = 'Actively Working'
            time_string = 'Start timer at:> '
            
        if self.right_now == self.work_time:
            self.remaining_sessions -= 1
            if self.remaining_breaks == 0:
                self.right_now = self.long_break
                timer_title = 'Take a long break.'
            else:
                self.right_now = self.short_break
                timer_title = 'Take a short break.'
                # time_string = 'Break timer at:> '
                
        elif self.right_now == self.short_break:
            self.remaining_breaks -= 1
            self.right_now = self.work_sessions
            timer_title = 'Actively Working'
            time_string = 'Short break timer at:> '
            
        elif self.right_now == self.long_break:
            self.right_now = self.work_sessions
            timer_title = 'Actively Working'
            self.remaining_sessions = self.work_sessions
            self.remaining_breaks = self.remaining_sessions - 1
            time_string = 'Long break timer at:> '
        else:
            print('This is the same \' should be an error \' case as mentioned by that guy.')
        
        self.end_time = datetime.now() + timedelta(self.right_now.interval_length)
        time_string += self.end_time.strftime("%H:%M:%S")
        self.notifications(time_string)
        
    def ticking_clock(self):
        print('1', self.right_now)
        self.change_event()
        print('2', self.right_now)
        while True:
            if datetime.now() >= self.end_time:
                self.change_event()
                sleep(0.2)
                
                
def main():
    try:
        # ap = argparse.ArgumentParser()
        
        # ap.add_argument('--work_duration', help='the length of the working session', type=int, default=25)
        # ap.add_argument('--break_duration_short', help='the length of a short break', type=int, default=5)
        # ap.add_argument('--break_duration_long', help='the length of a long break', type=int, default=30)
        
        # arguments = ap.parse_args()
        
        work_time, short_break, long_break = map(int, sys.argv[1:4])
        
        # time_clock = Clock(arguments.work_duration, arguments.break_duration_short, arguments.break_duration_long)
        time_clock = Clock(work_time, short_break, long_break)
        time_clock.ticking_clock()
    except Exception as e:
        print('One or more arguments are invalid.', str(e))
        exit(1)
        
if __name__ == '__main__':
    main()