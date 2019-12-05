
# For testing code, grab the words from Internet
from urllib.request import urlopen
u='https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt'
response = urlopen(u)
words = [i.strip().decode('utf8') for i in response.readlines()]

def get_average_word_length(words):
    '''
    Compute the average length of the words
    :param words: input, list
    :return: string
    '''

    assert bool(words) == True, "words cannot be empty"
    assert isinstance(words, list), "words must be a list"
    assert all(isinstance(i, str) for i in words), "words must be a list of string"

    sum=0

    for i in words:
        sum+=len(i)

    ave=sum/len(words)

    return ave


def get_longest_word(words):
    '''
    What's the longest word
    :param words: input, list
    :return: string
    '''

    assert bool(words) == True, "words cannot be empty"
    assert isinstance(words, list), "words must be a list"
    assert all(isinstance(i, str) for i in words), "words must be a list of string"

    longest_word = ''
    for i in words:
        if len(i) > len(longest_word):
            longest_word = i

    return longest_word


def get_longest_words_startswith(words, start):
    '''
    What is the longest word that starts with a specific letter
    :param words: input, list
    :param starts: input, string
    :return: string
    '''

    assert isinstance(start, str), "starting letter must be of type string"
    assert start.isspace() == False, "string cannot be made up of space"
    assert len(start) == 1, "string can only be a single letter"

    assert bool(words) == True, "words cannot be empty"
    assert isinstance(words, list), "words must be a list"
    assert all(isinstance(i, str) for i in words), "words must be a list of string"

    # starts = starts.lower()
    longest_word = ""

    for i in words:
        if i[0] == start:
            if len(i) > len(longest_word):
                longest_word = i

    return longest_word


def get_most_common_start(words):
    '''
    What is the most common starting letter
    :param words: input, list
    :return: string
    '''

    assert bool(words) == True, "words cannot be empty"
    assert isinstance(words, list), "words must be a list"
    assert all(isinstance(item, str) for item in words), "words must be a list of string"

    letter_freq = {}

    for i in words:
        if i[0] not in letter_freq.keys():
            letter_freq[i[0]] = 1

        else:
            letter_freq[i[0]] += 1

    return max(letter_freq, key=letter_freq.get)
    # Very useful statement, Returns key based on max value


def get_most_common_end(words):
    '''
    What is the most common ending letter
    :param words: input, list
    :return: string
    '''

    assert bool(words) == True, "words cannot be empty"
    assert isinstance(words, list), "words must be a list"
    assert all(isinstance(item, str) for item in words), "words must be a list of string"

    letter_freq = {}

    for i in words:
        if i[-1] not in letter_freq.keys():
            letter_freq[i[-1]] = 1
        else:
            letter_freq[i[-1]] += 1

    return max(letter_freq, key=letter_freq.get)
