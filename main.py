word = "Programming"

if len(word) >= 2:
    second_letter = word[1]

    second_last_letter = word[-2]

    print("Second:", second_letter, ";")
    print("Penultimate letter:", second_last_letter, ";")
else:
    print("The word is too short to perform a slice operation")
