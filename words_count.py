import csv

result = {}
with open('./words.txt', 'r') as words_file:
    for line in words_file.readlines():
        word = line.strip().lower().replace('-', '')
        for i in range(0, len(word) - 1):
            if word[i] not in result:
                result[word[i]] = [0] * 26
            result[word[i]][ord(word[i + 1]) - ord('a')] += 1


with open('./words_count.csv', 'w') as words_count:
    writer = csv.writer(words_count)
    writer.writerow(["word", "count"])
    for key in sorted(result.keys()):
        count = result[key]
        for i in range(0, len(count)):
            if count[i] != 0:
                writer.writerows([[key + chr(ord('a') + i), count[i]]])
