import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-whitegrid')


class Chart:

    def __init__(self, input_text=None, mark='semicolon', filename=None):
        self.story = None
        self.mark = mark
        if input_text:
            self.setStoryFromList(input_text)
        elif filename:
            self.setStoryFromFile(filename)

    def setStoryFromList(self, input_text):
        self.story = Story(input_text=input_text)
        return 1

    def setStoryFromFile(self, filename):
        self.story = Story(filename=filename)
        return 1

    def getStory(self):
        return self.story

    def getCenterLine(self):
        sentence_count = self.story.getSentenceCount()
        mark_count = None
        if self.mark == 'semicolon':
            mark_count = self.story.getSemicolonCount()
        if self.mark == 'dash':
            mark_count = self.story.getDashCount()
        return mark_count / sentence_count

    def getSentenceCountArray(self):
        return self.story.getSentenceCountArray()

    def getSemicolonCountArray(self):
        return self.story.getSemicolonCountArray()

    def getDashCountArray(self):
        return self.story.getDashCountArray()

    def getY(self):
        if self.mark == 'semicolon':
            mark_array = self.getSemicolonCountArray()
        if self.mark == 'dash':
            mark_array = self.getDashCountArray()
        sentence_array = self.getSentenceCountArray()
        return mark_array / sentence_array

    def getUpperControlLimit(self):
        center_line = self.getCenterLine()
        sentence_count = self.getSentenceCountArray()
        control_limit = center_line+3*np.sqrt(center_line*(1-center_line)/sentence_count)
        return control_limit

    def getLowerControlLimit(self):
        center_line = self.getCenterLine()
        sentence_count = self.getSentenceCountArray()
        control_limit = center_line-3*np.sqrt(center_line*(1-center_line)/sentence_count)
        control_limit = np.where(control_limit < 0, 0, control_limit)
        return control_limit

    def plotControlChart(self):
        central_line = np.ones(shape=(self.story.getParagraphCount()))* self.getCenterLine()
        upper_limit = self.getUpperControlLimit()
        lower_limit = self.getLowerControlLimit()
        y = self.getY()

        df = pd.DataFrame({'data':y,
                         'central line':central_line,
                         'upper limit':upper_limit,
                         'lower limit':lower_limit})
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex='col')

        ax1.step(df['lower limit'].index, df['lower limit'].values, where='mid')
        ax1.step(df['upper limit'].index, df['upper limit'].values, where='mid')
        ax1.axhline(self.getCenterLine())
        ax1.plot(df['data'])
        ax1.set_ylabel("Semicolons per Sentence")

        # fig, (ax1, ax2) = plt.subplots(2, 1, sharex='col')
        # ax1.step(lower_limit.index, lower_limit.values, where='mid')
        # ax1.step(upper_limit.index, upper_limit.values, where='mid')
        # ax1.axhline(chart.getCenterLine())
        # ax1.plot(y)
        # ax1.set_ylabel("Semicolons per Sentence")
        fig.savefig('test_plot.jpg')


class Story:

    def __init__(self, input_text=None, filename=None):
        self.body_raw   = None
        self.body_array = None # holds array of arrays of raw paragraphs
        self.body       = [] # holds the list of Paragraph objects
        self.sentence_count = None
        self.paragraph_count = None
        self.semicolon_count = None
        self.dash_count = None
        if filename:
            self.setBody(self.readBody(filename))
            self.processRawBody()
        elif input_text:
            self.setBody(input_text)
            self.processRawBody()

    def readBody(self, filename):
        self.body_raw = []
        text = filename
        with open(text, encoding='utf-8-sig') as f:
            for line in f:
                self.body_raw.append(line)
        print(self.body_raw)
        return self.body_raw


    def setSentenceCount(self):
        sentence_count = 0
        for paragraph in self.body:
            sentence_count += paragraph.sentence_count
        self.sentence_count = sentence_count

    def getSentenceCount(self):
        if self.sentence_count == None:
            self.setSentenceCount()
        return self.sentence_count

    def getSentenceCountArray(self):
        output = np.array([])
        for paragraph in self.body:
            output = np.append(output, paragraph.sentence_count)
        return output

    def setSemicolonCount(self):
        semicolon_count = 0
        for paragraph in self.body:
            semicolon_count += paragraph.semicolon_count
        self.semicolon_count = semicolon_count

    def getSemicolonCount(self):
        if self.semicolon_count == None:
            self.setSemicolonCount()
        return self.semicolon_count

    def getSemicolonCountArray(self):
        output = np.array([])
        for paragraph in self.body:
            output = np.append(output, paragraph.semicolon_count)
        return output

    def setDashCount(self):
        dash_count = 0
        for paragraph in self.body:
            dash_count += paragraph.dash_count
        self.dash_count = dash_count

    def getDashCount(self):
        if self.dash_count == None:
            self.setDashCount()
        return self.dash_count

    def getDashCountArray(self):
        output = np.array([])
        for paragraph in self.body:
            output = np.append(output, paragraph.dash_count)
        return output

    def setParagraphCount(self):
        self.paragraph_count = len(self.body)

    def getParagraphCount(self):
        if self.paragraph_count == None:
            self.setParagraphCount()
        return self.paragraph_count

    def readStory(self, story_file):
        pass

    def addParagraph(self, paragraph_array):
        pass

    def setBody(self, input_array):
        self.body_raw = input_array

    def getBody(self):
        return self.body

    def isNewline(self, test_string):
        if test_string == '\n':
            return True
        else:
            return False

    def createBodyList(self):
        for element in self.body_raw:
            pass

    def convertParagraphListToObject(self, input_list):
        return Paragraph(input_list)

    def appendParagraphToBody(self, paragraph):
        self.body.append(paragraph)
        return self.body

    def processRawBody(self):
        temp_paragraph_list = []
        pass
        for line in self.body_raw:
            if self.isNewline(line):
                self.appendParagraphToBody(self.convertParagraphListToObject(temp_paragraph_list))
                temp_paragraph_list = []
            else:
                temp_paragraph_list.append(line)
        if len(temp_paragraph_list) > 1:
            self.appendParagraphToBody(self.convertParagraphListToObject(temp_paragraph_list))



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
        self.setParagraphString(' '.join(self.paragraph_array).replace('\n',''))

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
        

