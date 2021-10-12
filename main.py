'''
Alarm Clock Lab

A. As a developer, I want to use Python’s proper snake_case for variable names.

B. As a developer, I want to create a AlarmClock class.

C. As a developer, I want the AlarmClock class to have class instance variables to keep track of the AlarmClock’s current time, whether the alarm is on or off, 
   and the time the alarm is set to. (You can use arbitrary strings to represent the time, it does not need to accurately tell the current time or change over time).

D. As a developer, I want the AlarmClock class to have a method to set (or change) the current time and print to the console the current time.

E. As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off.

F. As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the current alarm time.

G. As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.

1. Print the clock’s time to the terminal

2. Call the alarm clock’s change time method to change the time

3. Toggle the alarm clock’s on off switch

Files:

alarm_clock.py

Create class AlarmClock
    __init__ self
    self.alarm_set
    self.current_time
    self.onoff
        
1. Method for creating a clock
    import
    
2. Method for print when alarm goes off

3. Method for toggle on_off

4. Method for printing clock

5. Method for setting the alarm time


main.py

import alarm_clock

Alarm Clock!!
The current time now is { }.

Would you like to set an alarm?
Type the correlating numbers to operate the alarm clock.
1. set alarm (set)
2. alarm on / off (toggle)
3. current time (time)
4. time alarm is set to (alarm)
5. Exit alarm clock

print initial greetings


A .function with the above methods (selection from B.)
    if selection is == 1
        5. Method setting time
    elif selection == 2
        3. Method toggle on off
    elif seleciton == 3
        4. Method print current time
    elif selection == 4
        2. Print when alarm goes off
    elif selection == 5
        $ . exit alarm clock

B. function with above text
    return selection

C. Execution function ()
    selection = 0
    While selection != 5
        B. Function print and selection
        A. Method execution (selection from B.)
    else:
        Print you exited the clock

'''

from alarm_clock import AlarmClock

clock_time = AlarmClock()
print (clock_time.clock())

