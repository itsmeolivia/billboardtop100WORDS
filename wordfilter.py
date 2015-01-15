from sys import argv

f = file('updated_outputChr.txt', 'w')

for word in open(argv[1]):
    word = word.strip().lower()
    if len(word) > 2 and '\'' not in word:
        f.write(word + '\n')
