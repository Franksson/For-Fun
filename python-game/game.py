import random
import time

class Game:
    def __init__(self):
        self.name = "test"

    def reaction_game(self):
        delay = random.random() * 3
        time.sleep(delay)
        timer_start = time.time()
        print("Now!")
        input()
        timer_end = time.time()
        return timer_end - timer_start

game = Game()
print(game.reaction_game())