def replace(text, letter, letter_to_change):
    text_splitted = text.split(letter)
    print(letter_to_change.join(text_splitted))


replace("Mississippi", "i", "I")
song = "I love spom! Spom is my favorite food.Spom, spom, yum!"
replace(song, "om", "am")
replace(song, "o", "a")
