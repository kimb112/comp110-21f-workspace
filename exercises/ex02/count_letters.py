"""Counting letters in a string."""

__author__ = "730481343"

search_letter: str = input("What letter do you want to search for?: " )
search_word: str = input("Enter a word: ")

counter: int = 0
search_result: int = 0

while counter < len(search_word): 
    if search_word[counter] == search_letter: 
        search_result = search_result + 1
        counter = counter + 1
    else: 
        counter = counter + 1

search_result_string: str = str(search_result)
print("Count: " + search_result_string)
