def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    char_frequency = {}
    for char in phrase:
         if char in char_frequency:
            # If it is, increment the frequency count by 1
            char_frequency[char] += 1
         else:
            # If it's not, initialize the frequency count to 1
            char_frequency[char] = 1
    
    return char_frequency


print(multiple_letter_count('Yay'))