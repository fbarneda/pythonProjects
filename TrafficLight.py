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

    def play_red(self, time):
        t.current_color = self.red
        print("\n" * 50 + t.current_color + " ", end='')
        lets_wait(time)

    def play_yellow(self, time):
        t.current_color = self.yellow
        print("\n" + t.current_color + " ", end='')
        lets_wait(time)

    def play_green(self, time):
        t.current_color = self.green
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

while True:
    t.play_red(6)
    t.play_green(6)
    t.play_yellow(3)