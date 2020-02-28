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
            'ultricies. Suspendisse iaculis bibendum vestibulum.\n', # 9 sentences, 2 semicolons, 3 dashes
            '\n',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit? Cras varius -- sit amet\n',
            'nulla id porttitor. In a diam enim! Interdum et malesuada fames ac ante ipsum\n',
            'primis in faucibus. Pellentesque gravida luctus velit -- vitae congue erat\n',
            'sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero. In\n',
            'hac habitasse platea dictumst. Sed rutrum eros quis posuere gravida; Ut eu odio\n',
            'feugiat -- laoreet arcu non, aliquet odio. In quis elit vel metus dictum\n',
            'ultricies.\n', # 8 sentences, 2 semicolons, 3 dashes
            '\n',
            'Cras varius -- sit amet\n',
            'nulla id porttitor. In a diam enim! Interdum et malesuada fames ac ante ipsum\n',
            'primis in faucibus. Pellentesque gravida luctus velit -- vitae congue erat\n',
            'sodales et; Suspendisse ut ante elementum, dapibus justo in, lacinia libero. In\n',
            'hac habitasse platea dictumst. Sed rutrum eros quis posuere gravida; Ut eu odio\n',
            'feugiat -- laoreet arcu non, aliquet odio. In quis elit vel metus dictum\n',
            'ultricies.\n'] # 7 sentences, 2 semicolons

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

    def test__Sets_total_sentence_count(self, Story, sample_story_body_list):
        Story.setBody(sample_story_body_list)
        Story.processRawBody()
        result_sentence_count = Story.getSentenceCount()
        correct_sentence_count = 24
        assert result_sentence_count == correct_sentence_count


    def test__Sets_total_semicolon_count(self, Story, sample_story_body_list):
        Story.setBody(sample_story_body_list)
        Story.processRawBody()
        result_semicolon_count = Story.getSemicolonCount()
        correct_semicolon_count = 6
        assert result_semicolon_count == correct_semicolon_count

    def test__Sets_total_dash_count(self, Story, sample_story_body_list):
        Story.setBody(sample_story_body_list)
        Story.processRawBody()
        result_dash_count = Story.getDashCount()
        correct_dash_count = 9
        assert result_dash_count == correct_dash_count

    def test__Sets_total_paragraph_count(self, Story, sample_story_body_list):
        Story.setBody(sample_story_body_list)
        Story.processRawBody()
        result_paragraph_count = Story.getParagraphCount()
        correct_paragraph_count = 3
        assert result_paragraph_count == correct_paragraph_count

    def test__Sets_sentence_count_array(self, Story, sample_story_body_list):
        Story.setBody(sample_story_body_list)
        Story.processRawBody()
        sentence_count_array = Story.getSentenceCountArray()
        correct_sentence_count_array = np.array([9,8,7])
        npt.assert_array_equal(sentence_count_array, correct_sentence_count_array)

    def test__Sets_semicolon_count_array(self, Story, sample_story_body_list):
        Story.setBody(sample_story_body_list)
        Story.processRawBody()
        semicolon_count_array = Story.getSemicolonCountArray()
        correct_semicolon_count_array = np.array([2,2,2])
        npt.assert_array_equal(semicolon_count_array, correct_semicolon_count_array)

    def test__Sets_dash_count_array(self, Story, sample_story_body_list):
        Story.setBody(sample_story_body_list)
        Story.processRawBody()
        dash_count_array = Story.getDashCountArray()
        correct_dash_count_array = np.array([3,3,3])
        npt.assert_array_equal(dash_count_array, correct_dash_count_array)


class Test_Chart:

    def test__Gets_the_story(self, Story, sample_story_body_list):
        from control_chart import Chart
        chart = Chart(sample_story_body_list)
        story = chart.getStory()
        correct_sentence_count = 7
        result_sentence_count = story.body[2].sentence_count
        assert result_sentence_count == correct_sentence_count

    def test__Gets_the_story_from_file(self, Story):
        from control_chart import Chart
        input_file_name = 'sample_text_body.txt'
        chart = Chart(filename=input_file_name)
        story = chart.getStory()
        correct_sentence_count = 7
        result_sentence_count = story.body[2].sentence_count
        assert result_sentence_count == correct_sentence_count

    def test__Calculates_semicolon_center_line(self, Chart, Story, sample_story_body_list):
        from control_chart import Chart
        chart = Chart(sample_story_body_list)
        story = chart.getStory()
        result_center_line = chart.getCenterLine()
        correct_center_line = 6/24
        assert result_center_line == correct_center_line

    def test__Calculates_dash_center_line(self, Chart, Story, sample_story_body_list):
        from control_chart import Chart
        chart = Chart(sample_story_body_list, mark='dash')
        story = chart.getStory()
        result_center_line = chart.getCenterLine()
        correct_center_line = 9/24
        assert result_center_line == correct_center_line

    def test__Gets_sentence_count_array(self, Story, sample_story_body_list):
        from control_chart import Chart
        chart = Chart(sample_story_body_list)
        result_array = chart.getSentenceCountArray()
        correct_array = np.array([9,8,7])
        npt.assert_array_equal(result_array, correct_array)

    def test__Gets_semicolon_count_array(self, Story, sample_story_body_list):
        from control_chart import Chart
        chart = Chart(sample_story_body_list)
        result_array = chart.getSemicolonCountArray()
        correct_array = np.array([2,2,2])
        npt.assert_array_equal(result_array, correct_array)

    def test__Gets_dash_count_array(self, Story, sample_story_body_list):
        from control_chart import Chart
        chart = Chart(sample_story_body_list)
        result_array = chart.getDashCountArray()
        correct_array = np.array([3,3,3])
        npt.assert_array_equal(result_array, correct_array)

    def test__Calculates_semicolon_y_values(self, Chart, Story, sample_story_body_list):
        from control_chart import Chart
        chart = Chart(sample_story_body_list)
        story = chart.getStory()
        result_y = chart.getY()
        correct_y = np.array([2/9, 2/8, 2/7])
        npt.assert_array_equal(result_y, correct_y)

    def test__Calculates_dash_y_values(self, Chart, Story, sample_story_body_list):
        from control_chart import Chart
        chart = Chart(sample_story_body_list, mark='dash')
        story = chart.getStory()
        result_y = chart.getY()
        correct_y = np.array([3/9, 3/8, 3/7])
        npt.assert_array_equal(result_y, correct_y)

    def test__Calculates_semicolon_upper_control_limit(self, Chart, Story, sample_story_body_list):
        from control_chart import Chart
        chart = Chart(sample_story_body_list)
        story = chart.getStory()
        center_line = 6/24 # for semicolons
        sentence_count = np.array([9,8,7])
        result_upper_control_limit = chart.getUpperControlLimit()
        correct_upper_control_limit = center_line+3*np.sqrt(center_line*(1-center_line)/sentence_count)
        npt.assert_array_equal(result_upper_control_limit, correct_upper_control_limit)

    def test__Calculates_dash_upper_control_limit(self, Chart, Story, sample_story_body_list):
        from control_chart import Chart
        chart = Chart(sample_story_body_list, mark='dash')
        story = chart.getStory()
        center_line = 9/24 # for dashes
        sentence_count = np.array([9,8,7])
        result_upper_control_limit = chart.getUpperControlLimit()
        correct_upper_control_limit = center_line+3*np.sqrt(center_line*(1-center_line)/sentence_count)
        npt.assert_array_equal(result_upper_control_limit, correct_upper_control_limit)

    def test__Calculates_semicolon_lower_control_limit(self, Chart, Story, sample_story_body_list):
        from control_chart import Chart
        chart = Chart(sample_story_body_list)
        story = chart.getStory()
        center_line = 6/24 # for semicolons
        sentence_count = np.array([9,8,7])
        result_lower_control_limit = chart.getLowerControlLimit()
        correct_lower_control_limit = center_line-3*np.sqrt(center_line*(1-center_line)/sentence_count)
        correct_lower_control_limit = np.where(correct_lower_control_limit < 0, 0, correct_lower_control_limit)
        npt.assert_array_equal(result_lower_control_limit, correct_lower_control_limit)

    def test__Calculates_dash_lower_control_limit(self, Chart, Story, sample_story_body_list):
        from control_chart import Chart
        chart = Chart(sample_story_body_list, mark='dash')
        story = chart.getStory()
        center_line = 9/24 # for dashes
        sentence_count = np.array([9,8,7])
        result_lower_control_limit = chart.getLowerControlLimit()
        correct_lower_control_limit = center_line-3*np.sqrt(center_line*(1-center_line)/sentence_count)
        correct_lower_control_limit = np.where(correct_lower_control_limit < 0, 0, correct_lower_control_limit)
        npt.assert_array_equal(result_lower_control_limit, correct_lower_control_limit)


