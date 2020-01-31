import pytest
import numpy as np
import numpy.testing as npt

@pytest.fixture
def Paragraph():
    from control_chart import Paragraph
    return Paragraph()

@pytest.fixture
def StoryModel():
    from control_chart import Paragraph
    return Paragraph()

@pytest.fixture
def sample_paragraph_array():
    return ['Lorem ipsum dolor sit amet, consectetur adipiscing elit? Cras varius -- sit amet\n', 'nulla id porttitor. In a diam enim! Interdum et malesuada fames ac ante ipsum\n', 'primis in faucibus. Pellentesque gravida luctus velit -- vitae congue erat\n', 'sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero. In\n', 'hac habitasse platea dictumst. Sed rutrum eros quis posuere gravida; Ut eu odio\n', 'feugiat -- laoreet arcu non, aliquet odio. In quis elit vel metus dictum\n', 'ultricies. Suspendisse iaculis bibendum vestibulum.\n']

@pytest.fixture
def sample_paragraph():
    return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit? Cras varius -- sit amet nulla id porttitor. In a diam enim! Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque gravida luctus velit -- vitae congue erat sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero. In hac habitasse platea dictumst. Sed rutrum eros quis posuere gravida; Ut eu odio feugiat -- laoreet arcu non, aliquet odio. In quis elit vel metus dictum ultricies. Suspendisse iaculis bibendum vestibulum.'

@pytest.fixture
def sample_sentence_array():
    return np.array(['Lorem ipsum dolor sit amet, consectetur adipiscing elit?', 'Cras varius -- sit amet nulla id porttitor.', 'In a diam enim!', 'Interdum et malesuada fames ac ante ipsum primis in faucibus.', 'Pellentesque gravida luctus velit -- vitae congue erat sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero.', 'In hac habitasse platea dictumst.', 'Sed rutrum eros quis posuere gravida; Ut eu odio feugiat -- laoreet arcu non, aliquet odio.', 'In quis elit vel metus dictum ultricies.', 'Suspendisse iaculis bibendum vestibulum.'])

@pytest.fixture
def sample_story_body():
    return ['Lorem ipsum dolor sit amet, consectetur adipiscing elit? Cras varius -- sit amet\n', 'nulla id porttitor. In a diam enim! Interdum et malesuada fames ac ante ipsum\n', 'primis in faucibus. Pellentesque gravida luctus velit -- vitae congue erat\n', 'sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero. In\n', 'hac habitasse platea dictumst. Sed rutrum eros quis posuere gravida; Ut eu odio\n', 'feugiat -- laoreet arcu non, aliquet odio. In quis elit vel metus dictum\n', 'ultricies. Suspendisse iaculis bibendum vestibulum.\n', '\n', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit? Cras varius -- sit amet\n', 'nulla id porttitor. In a diam enim! Interdum et malesuada fames ac ante ipsum\n', 'primis in faucibus. Pellentesque gravida luctus velit -- vitae congue erat\n', 'sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero. In\n', 'hac habitasse platea dictumst. Sed rutrum eros quis posuere gravida; Ut eu odio\n', 'feugiat -- laoreet arcu non, aliquet odio. In quis elit vel metus dictum\n', 'ultricies. Suspendisse iaculis bibendum vestibulum.\n']

@pytest.fixture
def Story():
    from control_chart import Story
    return Story()


class TestCanary:
    
    def test_Tweets(self):
        assert 1 == 1

class Test_Paragraph:

    def test__Set_initial_paragraph_array(self, Paragraph, sample_paragraph_array):
        correct_paragraph = sample_paragraph_array
        Paragraph.setParagraphArray(sample_paragraph_array)
        npt.assert_array_equal(Paragraph.getParagraphArray(), sample_paragraph_array)

    def test__Joins_array_into_string(self, Paragraph, sample_paragraph_array, sample_paragraph):
        correct_string = sample_paragraph
        Paragraph.setParagraphArray(sample_paragraph_array)
        Paragraph.convertArrayToString()
        assert Paragraph.getParagraphString() == correct_string

    def test__Splits_string_into_sentence_array(self, Paragraph, sample_paragraph, sample_sentence_array):
        correct_array = sample_sentence_array
        Paragraph.setParagraphString(sample_paragraph)
        Paragraph.convertStringToSentenceArray()
        npt.assert_array_equal(Paragraph.paragraph, correct_array)

    def test__Counts_semicolons(self, Paragraph, sample_paragraph_array):
        correct_count = 2
        Paragraph.setParagraphArray(sample_paragraph_array)
        Paragraph.setSemicolonCount()
        assert Paragraph.semicolon_count == correct_count

    def test__Counts_dashes(self, Paragraph, sample_paragraph_array):
        correct_count = 3
        Paragraph.setParagraphArray(sample_paragraph_array)
        Paragraph.setDashCount()
        assert Paragraph.dash_count == correct_count

    def test__Counts_sentences(self, Paragraph, sample_paragraph_array):
        correct_count = 9
        Paragraph.setParagraphArray(sample_paragraph_array)
        Paragraph.convertArrayToString()
        Paragraph.convertStringToSentenceArray()
        Paragraph.setSentenceCount()
        assert Paragraph.sentence_count == correct_count

    def test__Converts_raw_array_into_sentence_array(self, Paragraph, sample_paragraph_array, sample_sentence_array):
        correct_array = sample_sentence_array
        Paragraph.conditionParagraph(sample_paragraph_array)
        npt.assert_array_equal(Paragraph.paragraph, correct_array)

    def test__Counts_all_punctuations(self, Paragraph, sample_paragraph_array):
        correct_sentence_count = 9
        correct_semicolon_count = 2
        correct_dash_count = 3
        Paragraph.conditionParagraph(sample_paragraph_array)
        Paragraph.countPunctuation()
        assert Paragraph.sentence_count == correct_sentence_count
        assert Paragraph.semicolon_count == correct_semicolon_count
        assert Paragraph.dash_count == correct_dash_count
        

    def test__Initializes_with_paragraph(self, sample_paragraph_array, sample_sentence_array):
        from control_chart import Paragraph
        correct_paragraph = sample_sentence_array
        Paragraph = Paragraph(sample_sentence_array)
        npt.assert_array_equal(Paragraph.paragraph, correct_paragraph)




class Test_Story:

    def test__Sets_story_body(self, Story, sample_story_body):
        correct_body = sample_story_body
        Story.setBody(sample_story_body)
        npt.assert_array_equal(Story.body, correct_body)










    # def test__Adds_a_paragraph_to_the_body(self, Story, sample_paragraph_array):
        # correct_body_array_paragraph = sample_paragraph
        # Story.addParagraph(sample_paragraph_array)
        # assert Story.body_array[0].getParagraph() == correct_body_array_paragraph






    # def test__Sets_the_story(self, Story, sample_story):
        # correct_story = sample_story
        # Story.setStory(sample_story)




# class Test_Model:

    # def test__Set_X_if_X_is_Empty(self, model, sample_predictors):
        # correct_X = sample_predictors
        # model.setPredictors(sample_predictors)
        # print(f'correct_X:  {correct_X}')
        # print(f'sample_predictors:  {sample_predictors}')
        # print(f'model.X.sample_predictors:  {model.X.sample_predictors}')
        # npt.assert_array_equal(model.X.sample_predictors, correct_X)
