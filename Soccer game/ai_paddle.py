import time
import random

class AIPaddle(object):
    def __init__(self, screensize):

        # ...

        # If time.time() > self.AI_time: the AI will work
        self.AI_on_after = time.time()
        # Probability of AI failing each second: 0 <= P <= 1
        self.P_AI_fail = 0.1
        # Duration in which AI won't do anything when it has failed
        self.T_AI_fail = 1.0
        self.next_fail_decision_T = time.time()

    def update(self, pong):
        # Each second: Decide if it's time to fail
        if time.time() > self.next_fail_decision_T:
            if random.random() <= self.P_AI_fail:
                self.AI_on_after = time.time() + self.T_AI_fail
            self.next_fail_decision_T = time.time() + 1.0

        # Random loss of concentration
        if time.time() > self.AI_on_afer:
            speed = 0
        else:
            speed = self.speed

        if pong.rect.top < self.rect.top:
            self.centery -= speed
        elif pong.rect.bottom > self.rect.bottom:
            self.centery += speed