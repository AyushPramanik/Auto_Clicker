import pyautogui as pt
import time

class Clicker:
    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=.8)
            pt.moveTo(position[0] + 10, position[1] + 10)
        
        except:
            print("No Image Found")
            return 0

if __name__ == '__main__':
    time.sleep(4)
    clicker = Clicker("target.png", speed=.001)

    end = 0
    while True:
        if clicker.nav_to_image() == 0:
            end += 1
        
        if end > 20: 
            break