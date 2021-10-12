class AlarmClock:
    def __init__(self):
        self.set_alarm = []
        self.toggle = ""
        self.print_time = ""
        self.print_settime = ""

    def clock (self):
        import datetime
        time = datetime.datetime.now()
        current_time = time.strftime("%X")
        return current_time
      
    def set_alarm (self):
        self.set_alarm = []
        proper_time = True
        while True:
            hour_alarm = int(input("What hour would you like to set the alarm? Use 2 digits (00), and 24hr time."))
            min_alarm = int(input("What minute would you like to set the alarm? Use 2 digits (00)."))
            if hour_alarm <= 24 and hour_alarm >= 00 and min_alarm <= 60:
                self.set_alarm.append(hour_alarm)
                self.set_alarm.append(min_alarm)
                proper_time = False
            return self.set_alarm 

            




