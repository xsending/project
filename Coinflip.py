import random
# 0 represents heads, 1 represents tails
number_of_streaks = 0 # tracks how many times heads or tails appeared 6 times consecutively
streak_count1 = 0 # tracks the appearance of tails
streak_count0 = 0 # tracks the appearance of heads

for repeat in range(10000): #repeats the 100 flips 10000 times
    for flip in range(100): #creates a coin flip 100 times
        number = random.randint(0, 1) # randomly generates either 0 or 1
        if number == 1: # checks if flip result is tails
            streak_count1 += 1 # keeps track whether tails consecutively appeared
        else:
            if number == 0: # checks if flip result is not tails
                streak_count1 = 0 # TAILS tracker is reset if flip result is not tails
        if streak_count1 == 6: # checks if tails appeared 6 times
            number_of_streaks += 1 # adds a point to STREAK tracker if tails appeared 6 times
            streak_count1 = 0 # resets TAILS tracker after adding a point to the STREAK tracker

        if number == 0: # checks if flip result is heads
            streak_count0 += 1 # keeps track whether heads consecutively appeared
        else:
            if number == 1: # checks if flip result is not heads
                streak_count0 = 0 # HEADS tracker is reset if flip result is not heads
        if streak_count0 == 6: # checks if heads appeared 6 times
            number_of_streaks += 1 # adds a point to STREAK tracker if heads appeared 6 times
            streak_count0 = 0 # resets HEADS tracker after adding a point to the STREAK tracker

print(number_of_streaks/1000000 * 100) # checks the probability of heads or tails appearing 6 times consecutively
