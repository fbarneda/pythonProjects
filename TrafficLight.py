"""
Traffic Light
"""

import time, random


class TrafficLight():

    def __init__(self):

        self.color_options = {'R': 'RED', 'Y': 'YELLOW', 'G': 'GREEN'}
        self.current_color = ''
        self.red = self.color_options['R']
        self.yellow = self.color_options['Y']
        self.green = self.color_options['G']

    def play_red(self, time):

        t.current_color = self.red
        print(t.current_color)
        lets_wait(time)

    def play_yellow(self, time):

        t.current_color = self.yellow
        print(t.current_color)
        lets_wait(time)

    def play_green(self, time):

        t.current_color = self.green
        print(t.current_color)
        lets_wait(time)


def lets_wait(wait_seconds):

    count_down = list(range(1, wait_seconds + 1))
    count_down.reverse()

    for num in count_down:

        print(str(num) + " seconds left")
        time.sleep(1)


# Program starts here:
t = TrafficLight()

while True:
    t.play_red(5)
    t.play_yellow(2)
    t.play_green(5)