# Notes and Todo Software
# brupoon

class Note():
    
    def __init__(self, date, text):
        self.date = date
        self.text = text

        if self.date == -1:
            self.todo = True
            self.calendar = False
        else:
            self.todo = False
            self.calendar = True
