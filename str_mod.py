

def reverse_string(input_string):
    """
    Reverse a given string.

    :param input_string: string to be reversed
    :returns: reversed version of input string
    :raises TypeError: if input is not string
    """

    output_string = ""
    # Iterate backwards over input and append output string
    for i in range(len(input_string) - 1, -1, -1):
        character = input_string[i]
        output_string += character

    return output_string


def pig_latin(input_string):
    """
    Converts a given string into pig latin.
    Currently replaces returns with spaces and doesn't handle 
        punctuation or proper capitalization

    :param input_string: string to be converted
    :returns: given string in pig latin
    :raises TypeError: if input is not string
    """

    vowels = "aeiou"
    suffix = "ay"

    # Turn string into list of words
    word_list = input_string.split()
    latin_word_list = []
    # Iterate over words and format them
    for word in word_list:
        # Keep punctuation at end of word
        punctuation = ""
        if not word[-1].isalpha():
            punctuation = word[-1]
            word = word[0:-1]
        # Keep capitalization at beginning of word
        capitalize = False
        if word[0].isupper():
            capitalize = True
            word = word[0].lower() + word[1:]
        # Find first vowel in string
        latin_word = word
        for i in range(0, len(word)):
            character = word[i]
            if character.lower() in vowels:
                # Move first syllable to end and append suffix
                latin_word = word[i:] + word[0:i] + suffix + punctuation
                # Return capitalization of original word
                latin_word = latin_word.title() if capitalize else latin_word
                break

        latin_word_list.append(latin_word)

    # Join words list into string separated by spaces
    latin_string = " ".join(latin_word_list)
    return latin_string


def count_vowels(input_string):
    """
    Counts the number of each vowel in given string.

    :param input_string: string to count the vowels of
    :returns: dictionary of each vowel and corresponding count
    :raises TypeError: if input is not string
    """

    vowels = "aeiouy"
    vowel_counts = {v : 0 for v in vowels}
    for letter in input_string:
        if letter in vowel_counts.keys():
            vowel_counts[letter] = vowel_counts.get(letter) + 1
    return vowel_counts


print(count_vowels("The quick brown fox jumps over the lazy dog"))
# print(reverse_string("This string is going to be reversed."))
# print(pig_latin("This string can't be in pig latin.\nBut it can if you fix punctuation."))
