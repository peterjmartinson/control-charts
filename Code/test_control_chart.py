import pytest
import numpy as np
import numpy.testing as npt

@pytest.fixture
def Paragraph():
    from control_chart import Paragraph
    return Paragraph()

@pytest.fixture
def sample_paragraph_list():
    return ['Lorem ipsum dolor sit amet, consectetur adipiscing elit? Cras varius -- sit amet\n',
            'nulla id porttitor. In a diam enim! Interdum et malesuada fames ac ante ipsum\n',
            'primis in faucibus. Pellentesque gravida luctus velit -- vitae congue erat\n',
            'sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero. In\n',
            'hac habitasse platea dictumst. Sed rutrum eros quis posuere gravida; Ut eu odio\n',
            'feugiat -- laoreet arcu non, aliquet odio. In quis elit vel metus dictum\n',
            'ultricies. Suspendisse iaculis bibendum vestibulum.\n']

@pytest.fixture
def sample_paragraph():
    return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit? Cras varius -- sit amet nulla id porttitor. In a diam enim! Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque gravida luctus velit -- vitae congue erat sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero. In hac habitasse platea dictumst. Sed rutrum eros quis posuere gravida; Ut eu odio feugiat -- laoreet arcu non, aliquet odio. In quis elit vel metus dictum ultricies. Suspendisse iaculis bibendum vestibulum.'

@pytest.fixture
def sample_sentence_array():
    return np.array(['Lorem ipsum dolor sit amet, consectetur adipiscing elit?',
                    'Cras varius -- sit amet nulla id porttitor.',
                    'In a diam enim!',
                    'Interdum et malesuada fames ac ante ipsum primis in faucibus.',
                    'Pellentesque gravida luctus velit -- vitae congue erat sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero.',
                    'In hac habitasse platea dictumst.',
                    'Sed rutrum eros quis posuere gravida; Ut eu odio feugiat -- laoreet arcu non, aliquet odio.',
                    'In quis elit vel metus dictum ultricies.',
                    'Suspendisse iaculis bibendum vestibulum.'])

@pytest.fixture
def sample_story_body_list():
    return ['Lorem ipsum dolor sit amet, consectetur adipiscing elit? Cras varius -- sit amet\n',
            'nulla id porttitor. In a diam enim! Interdum et malesuada fames ac ante ipsum\n',
            'primis in faucibus. Pellentesque gravida luctus velit -- vitae congue erat\n',
            'sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero. In\n',
            'hac habitasse platea dictumst. Sed rutrum eros quis posuere gravida; Ut eu odio\n',
            'feugiat -- laoreet arcu non, aliquet odio. In quis elit vel metus dictum\n',
            'ultricies. Suspendisse iaculis bibendum vestibulum.\n', # 9 sentences
            '\n',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit? Cras varius -- sit amet\n',
            'nulla id porttitor. In a diam enim! Interdum et malesuada fames ac ante ipsum\n',
            'primis in faucibus. Pellentesque gravida luctus velit -- vitae congue erat\n',
            'sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero. In\n',
            'hac habitasse platea dictumst. Sed rutrum eros quis posuere gravida; Ut eu odio\n',
            'feugiat -- laoreet arcu non, aliquet odio. In quis elit vel metus dictum\n',
            'ultricies.\n', # 8 sentences
            '\n',
            'Cras varius -- sit amet\n',
            'nulla id porttitor. In a diam enim! Interdum et malesuada fames ac ante ipsum\n',
            'primis in faucibus. Pellentesque gravida luctus velit -- vitae congue erat\n',
            'sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero. In\n',
            'hac habitasse platea dictumst. Sed rutrum eros quis posuere gravida; Ut eu odio\n',
            'feugiat -- laoreet arcu non, aliquet odio. In quis elit vel metus dictum\n',
            'ultricies.\n'] # 7 sentences

@pytest.fixture
def Story():
    from control_chart import Story
    return Story()


@pytest.fixture
def Chart():
    from control_chart import Chart
    return Chart()


class TestCanary:
    
    def test_Tweets(self):
        assert 1 == 1

class Test_Paragraph:

    def test__Set_initial_paragraph_array(self, Paragraph, sample_paragraph_list):
        correct_paragraph = sample_paragraph_list
        Paragraph.setParagraphArray(sample_paragraph_list)
        npt.assert_array_equal(Paragraph.getParagraphArray(), sample_paragraph_list)

    def test__Joins_array_into_string(self, Paragraph, sample_paragraph_list, sample_paragraph):
        correct_string = sample_paragraph
        Paragraph.setParagraphArray(sample_paragraph_list)
        Paragraph.convertArrayToString()
        assert Paragraph.getParagraphString() == correct_string

    def test__Splits_string_into_sentence_array(self, Paragraph, sample_paragraph, sample_sentence_array):
        correct_array = sample_sentence_array
        Paragraph.setParagraphString(sample_paragraph)
        Paragraph.convertStringToSentenceArray()
        npt.assert_array_equal(Paragraph.paragraph, correct_array)

    def test__Counts_semicolons(self, Paragraph, sample_paragraph_list):
        correct_count = 2
        Paragraph.setParagraphArray(sample_paragraph_list)
        Paragraph.setSemicolonCount()
        assert Paragraph.semicolon_count == correct_count

    def test__Counts_dashes(self, Paragraph, sample_paragraph_list):
        correct_count = 3
        Paragraph.setParagraphArray(sample_paragraph_list)
        Paragraph.setDashCount()
        assert Paragraph.dash_count == correct_count

    def test__Counts_sentences(self, Paragraph, sample_paragraph_list):
        correct_count = 9
        Paragraph.setParagraphArray(sample_paragraph_list)
        Paragraph.convertArrayToString()
        Paragraph.convertStringToSentenceArray()
        Paragraph.setSentenceCount()
        assert Paragraph.sentence_count == correct_count

    def test__Converts_raw_array_into_sentence_array(self, Paragraph, sample_paragraph_list, sample_sentence_array):
        correct_array = sample_sentence_array
        Paragraph.conditionParagraph(sample_paragraph_list)
        npt.assert_array_equal(Paragraph.paragraph, correct_array)

    def test__Counts_all_punctuations(self, Paragraph, sample_paragraph_list):
        correct_sentence_count = 9
        correct_semicolon_count = 2
        correct_dash_count = 3
        Paragraph.conditionParagraph(sample_paragraph_list)
        Paragraph.countPunctuation()
        assert Paragraph.sentence_count == correct_sentence_count
        assert Paragraph.semicolon_count == correct_semicolon_count
        assert Paragraph.dash_count == correct_dash_count
        

    def test__Initializes_with_paragraph(self, sample_paragraph_list, sample_sentence_array):
        from control_chart import Paragraph
        correct_paragraph = sample_sentence_array
        Paragraph = Paragraph(sample_sentence_array)
        npt.assert_array_equal(Paragraph.paragraph, correct_paragraph)




class Test_Story:

    def test__Sets_raw_story_body(self, Story, sample_story_body_list):
        correct_body = sample_story_body_list
        Story.setBody(sample_story_body_list)
        npt.assert_array_equal(Story.body_raw, correct_body)

    def test__Identifies_new_line_in_paragraph_list(self, Story, sample_paragraph_list):
        sample_list = ['a\n', '\n']
        answer = Story.isNewline(sample_list[1])
        assert answer == True

    def test__Identifies_not_new_line(self, Story, sample_paragraph_list):
        sample_list = ['a\n', '\n']
        answer = Story.isNewline(sample_list[0])
        assert answer == False

    def test__Converts_paragraph_list_to_paragraph_object(self, Story, sample_paragraph_list):
        from control_chart import Paragraph
        p = Story.convertParagraphListToObject(sample_paragraph_list)
        assert p.sentence_count == 9

    def test__Push_paragraph_to_body_list(self, Story, sample_paragraph_list):
        from control_chart import Paragraph
        correct_sentence_count = 9
        p = Story.convertParagraphListToObject(sample_paragraph_list)
        Story.appendParagraphToBody(p)
        result_sentence_count = Story.body[0].sentence_count
        assert result_sentence_count == correct_sentence_count

    def test__Push_two_paragraphs_to_body_list(self, Story, sample_paragraph_list):
        from control_chart import Paragraph
        correct_sentence_count = 9
        p = Story.convertParagraphListToObject(sample_paragraph_list)
        Story.appendParagraphToBody(p)
        Story.appendParagraphToBody(p)
        result_sentence_count = Story.body[1].sentence_count
        assert result_sentence_count == correct_sentence_count

    def test__Converts_raw_body_to_list_of_paragraph_objects(self, Story, sample_story_body_list):
        Story.setBody(sample_story_body_list)
        Story.processRawBody()
        correct_sentence_count = 7
        result_sentence_count = Story.body[2].sentence_count
        assert result_sentence_count == correct_sentence_count

class Test_Chart:

    def test__Gets_the_story(self, Chart, Story, sample_story_body_list):
        Story.setBody(sample_story_body_list)
        Story.processRawBody()
        story = Chart.getStory()
        correct_sentence_count = 6
        result_sentence_count = story.body[2].sentence_count
        assert result_sentence_count == correct_sentence_count



##
# 1. Creates an array of all body text
# 2. Arranges a new list like the following:
#     [
#             [paragraph list],
#             [paragraph list],
#             ...
#     ]
#       
#     a. `for` loop over items in body_raw
#     b. append each element to a temporary list
#     c. When '\n' is reached, append the temporary list to the master list
#     d. repeat
# 3. Use a `for` loop to create a new np.array() {body} like the following:
#     [
#             Paragraph object,
#             Paragraph object,
#             ...
#     ]
# 
#     this step can be broken into phases
#     a. pick a [paragraph list]
#     b. Paragraph = Paragraph([paragraph list])
#     c. Append that new Paragraph to the master list
##
