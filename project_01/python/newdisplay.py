from Adafruit_CharLCD import Adafruit_CharLCD

class LCDDisplay:
    """ A class to control a character LCD display. """

    def __init__(self, rs, en, d4, d5, d6, d7, cols=16, lines=2):
        """ Initialize LCD display with GPIO pin assignments """
        self.lcd = Adafruit_CharLCD(rs, en, d4, d5, d6, d7, cols, lines)
        self.lcd.clear()
        self.cols = cols
        self.lines = lines

    def display_message(self, line1, line2=''):
        """ Displays two lines of text on the LCD """
        self.lcd.clear()
        self.lcd.set_cursor(0, 0)
        self.lcd.message(line1[:self.cols])  # limit to display width
        
        if self.lines > 1:
            self.lcd.set_cursor(0, 1)
            self.lcd.message(line2[:self.cols])

    def clear(self):
        """ Clears the LCD display """
        self.lcd.clear()

    def display_time(self, time_data, zone_name):
        """ Displays a formatted time and zone on the LCD """
        line1 = f"{zone_name} Time"
        line2 = f"{time_data['time']}"
        self.display_message(line1, line2)
