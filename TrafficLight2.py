"""
Traffic Light
"""

import time


class TrafficLight():

    def __init__(self):
        self.color_options = {'R': 'RED', 'Y': 'YELLOW', 'G': 'GREEN'}
        self.current_color = ''
        self.red = self.color_options['R']
        self.yellow = self.color_options['Y']
        self.green = self.color_options['G']
        self.working = False

    def turn_on(self):
        self.working = True

    def turn_off(self):
        self.working = False


def play_red(time):
    t.current_color = t.red
    print("\n" * 50 + t.current_color + " ", end='')
    lets_wait(time)

def play_yellow(time):
    t.current_color = t.yellow
    print("\n" + t.current_color + " ", end='')
    lets_wait(time)

def play_green(time):
    t.current_color = t.green
    print("\n" + t.current_color + " ", end='')
    lets_wait(time)

def lets_wait(wait_seconds):
    count_down = list(range(1, wait_seconds + 1))
    count_down.reverse()

    for num in count_down:

        print(str(num) + " ", end='')
        time.sleep(1)


# Program starts here:
t = TrafficLight()

t.turn_on()

while t.working:
    play_red(3)
    play_green(3)
    play_yellow(3)