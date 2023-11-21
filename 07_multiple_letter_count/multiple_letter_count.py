def multiple_letter_count(phrase):
    frequency = {}

    for letter in phrase:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency
