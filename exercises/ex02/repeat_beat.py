"""Repeating a beat in a loop."""

__author__ = "730481343"

beat: str = input("What beat do you want to repeat? ")

repeat_times: int = int(input("How many times do you want to repeat it? "))

counter: int = 0

beat_string: str = ""

if repeat_times < 0: 
    print("No beat...")

else: 
    while counter < repeat_times: 
        if counter != repeat_times - 1:
            beat_string = beat_string + beat + " "
            counter = counter + 1
        else: 
            beat_string = beat_string + beat
            counter = counter + 1

    print(beat_string)
        
    
        