"""Repeating a beat in a loop."""

__author__ = "730481343"

beat: str = input("What beat do you want to repeat? ")

repeat_times: int = int(input("How many times do you want to repeat it? "))

counter: int = 0

if repeat_times < 0: 
    print("No beat...")

else: 
    while counter < repeat_times: 
        while repeat_times != counter:
            repeat_beats: str = beat
            final_beats: str = repeat_beats + "5"
            counter = counter + 1
            print(final_beats)
        
        # final_beat = final_beats
        counter = counter + 1
        