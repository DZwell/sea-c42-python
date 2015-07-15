import sys
import string
import random


file = 'sherlock.txt'


def read_file(file):

    try:
        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        full_text = []
        for line in range(len(lines)):
            full_text.append(lines[line])

        return ' '.join(full_text)

    except IOError as e:
        print(str(e))
        sys.exit(1)


def remove_punctuation(text):

    def check_punctuation(char):
        for char in text:
            if (char is "'"):
                return 0
            if (char is '-'):
                return 0
            elif (char in string.punctuation):
                return 1
            else:
                return 0

    stripped_text = ''

    for char in text:
        if check_punctuation(char) is 0:
            stripped_text += char

    stripped_text = stripped_text.lower()

    stripped_text = stripped_text.replace('--', ' ')
    stripped_text = stripped_text.replace('-', ' ')

    words = stripped_text.split()
    words = [word for word in words if word != "'"]

    return words


def build_trigrams(words):

    word_pairs = {}

    for w in range(len(words) - 2):
        leading_pair = tuple(words[w:w+2])
        end_word = words[w+2]
        if leading_pair in word_pairs:
            word_pairs[leading_pair].append(end_word)
        else:
            word_pairs[leading_pair] = [end_word]
    return word_pairs


def create_text(word_pairs):

    new_text = []

    for i in range(100):
        key_list = list(word_pairs.keys())
        sentence = list(random.choice(key_list))

        for j in range(random.randint(2, 10)):
            pair = tuple(sentence[-2:])
            if pair in word_pairs:
                sentence.append(random.choice(list(word_pairs[pair])))
            else:
                break
        sentence[0] = sentence[0].capitalize()
        sentence[-1] += '.'
        new_text.extend(sentence)

    new_text = ' '.join(new_text)

    print(new_text)
    return new_text

if __name__ == '__main__':

    create_text(build_trigrams(remove_punctuation(read_file(file))))










