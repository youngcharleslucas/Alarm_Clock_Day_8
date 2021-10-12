class AlarmClock:
    def __init__(self):
        self.set_alarm = ""
        self.toggle = ""
        self.print_time = ""
        self.print_settime = ""

    def clock (self):
        import datetime
        time = datetime.datetime.now()
        current_time = time.strftime("%X")
        return current_time

        

    # def set_alarm (self):



