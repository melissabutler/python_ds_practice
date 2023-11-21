def flip_case(phrase, to_swap):
    out = ""
    to_swap = to_swap.lower()

    for letter in phrase:
        if letter.lower() == to_swap:
            letter = letter.swapcase()
           
        out += letter
    print(out)        
    return out

        
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
