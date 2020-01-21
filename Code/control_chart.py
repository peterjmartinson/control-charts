import re

text = 'SleepyHollow.txt'


with open(text, encoding='utf-8') as f:
    for line in f:
        p = re.compile('\*\*\* START OF THIS PROJECT GUTENBERG EBOOK')
        if (p.search(line) != None):
            print(line)

