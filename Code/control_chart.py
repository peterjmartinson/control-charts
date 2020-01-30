import re
import numpy as np
# import nltk.data


text = 'SleepyHollow.txt'


with open(text, encoding='utf-8') as f:
    story = []
    for line in f:
        story.append(line)
        p = re.compile('START OF THIS PROJECT GUTENBERG EBOOK')
        if (p.search(line) != None):
            print(line)
    print(story)

class Story:

    def __init__(self):
        body_array = None

    def readStory(self, story_file):
        pass

    def addParagraph(self, paragraph_array):
        pass


class Paragraph: 

    def __init__(self, input_array=1024):
        self.paragraph = None
        self.paragraph_array = None
        self.paragraph_string = None
        self.semicolon_count = None
        self.dash_count = None
        self.sentence_count = None
        if type(input_array) != int:
            self.conditionParagraph(input_array)
            self.countPunctuation()

    def setParagraphArray(self, input_array):
        self.paragraph_array = np.array(input_array)

    def getParagraphArray(self):
        return self.paragraph_array

    def setParagraphString(self, input_string):
        self.paragraph_string = input_string

    def getParagraphString(self):
        return self.paragraph_string

    def setParagraph(self, input_array):
        self.paragraph = np.array(input_array)

    def getParagraph(self):
        return self.paragraph

    def convertArrayToString(self):
        self.setParagraphString(' '.join(self.paragraph_array))

    def convertStringToSentenceArray(self):
        thirties = re.compile(r'303030')
        dot_space = re.compile(r'\.\s+')
        q_space = re.compile(r'\?\s+')
        bing_space = re.compile(r'!\s+')
        output = thirties.split(dot_space.sub('.303030', q_space.sub('?303030', bing_space.sub('!303030', self.paragraph_string))))
        self.paragraph = output
        return 0

    def setSemicolonCount(self):
        if (self.paragraph_string == None):
            self.convertArrayToString()
        semicolon = re.compile(';')
        self.semicolon_count = len(semicolon.findall(self.paragraph_string))
        return self.semicolon_count

    def setDashCount(self):
        if (self.paragraph_string == None):
            self.convertArrayToString()
        dash = re.compile('--')
        self.dash_count = len(dash.findall(self.paragraph_string))
        return self.dash_count

    def setSentenceCount(self):
        if (len(self.paragraph) == 0):
            raise ValueError('No paragraph set!')
        self.sentence_count = len(self.paragraph)
        return self.sentence_count

    def conditionParagraph(self, input_array):
        self.setParagraphArray(input_array)
        self.convertArrayToString()
        self.convertStringToSentenceArray()
        return self.getParagraph()

    def countPunctuation(self):
        self.setSentenceCount()
        self.setSemicolonCount()
        self.setDashCount()
        return 1
        

