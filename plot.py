import csv
from collections import namedtuple
import matplotlib.pyplot as plt

letter = ['a', 'b', 'c']
letter_count = {}

with open('./words_count.csv') as words_count:
    word_csv = csv.reader(words_count)
    headings = next(word_csv)
    Row = namedtuple('Row', headings)
    for r in word_csv:
        row = Row(*r)
        letters = row[0]
        if letters[0] in letter:
            if letters[0] not in letter_count:
                letter_count[letters[0]] = []
            letter_count[letters[0]].append([row[0], int(row[1])])


def take_count(element):
    return element[1]


for key, value in letter_count.items():
    value.sort(key=take_count)
    print(key, value)
    x_value = []
    y_value = []
    for item in value:
        x_value.append(item[0][1])
        y_value.append(item[1])
    plt.title('Letter Count of ' + key)
    plt.bar(x_value, y_value)
    plt.xlabel('the letter after ' + key)
    plt.ylabel('Count')
    plt.savefig(key + ".png")
    plt.show()





