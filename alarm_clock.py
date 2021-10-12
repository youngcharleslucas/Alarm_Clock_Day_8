from datetime import datetime


class AlarmClock:
    def __init__(self):
        self.set_alarm = []
        self.toggle = ""
        self.print_time = ""
        self.print_settime = ""
        self.current_time = ""

    def clock (self):
        import datetime
        time = datetime.datetime.now()
        self.current_time = time.strftime("%X")
        return self.current_time
      
    def setting_alarm (self):
        self.set_alarm = []
        proper_time = True
        while proper_time == True:
            hour_alarm = int(input("What hour would you like to set the alarm?: "))
            min_alarm = int(input("What minute would you like to set the alarm?: "))
            if hour_alarm <= 24 and hour_alarm >= 00 and min_alarm <= 60:
                self.set_alarm.append(hour_alarm)
                self.set_alarm.append(min_alarm)
                proper_time = False
            else: 
                print("Please enter a correct time")
        return self.set_alarm 

    def activate_alarm (self, alarm_time):
        import time
        now = datetime.now()
        print_alarm = (f"ALARM!!! The time is {now}")
        run_alarm = True
        while run_alarm == True:
            if int(datetime.now().strftime("%M")) == int(alarm_time[1]):
                print(print_alarm)
                run_alarm = False
            else:
                print(datetime.now().strftime("%M"))
                print(alarm_time[1])
                exit = input("{now} Enter any key to exit alarm")
                if exit != "":
                    time.sleep(5)
                else:
                    break


'''

What is the task you are trying to accomplish? What is the goal? (answer below)

Trying to exit the while loop for the alarm clock. I am using a while loop with a time.sleep(5). I need the while loop to update
the current time when comparing it to the set alarm. 
I am able to create an alarm on a while loop, but to meet the requirements of the project, I need to
be able to toggle the alarm on and off. This requires user input. Anytime I request user
input during the loop, the user needs to be there to hit enter so that the while loop can
cycle through again.



What do you think the problem or impediment is? (answer below)
There is a concept to while loops I do not under stand. or I am
comparing real time to the alarm the wrong way.


What have you specifically tried in your code? (answer below)
Not have user input.
Have user input


What did you learn by dropping a breakpoint? (if unable to run your app due to error, please state that below in your answer)

see first answer.

'''

                

            




