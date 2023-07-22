import pprint
import uuid
import opml

from my_classes import Page, Response, StudentResponses

def parse_opml_course_from_workflowy():
    outline = opml.parse('input/pages.opml')
    # print(outline)
    anchor_pages = outline[0]
    pages = []
    for i, opml_anchor_page in enumerate(anchor_pages[::-1]):  # todo: eventually go in reverse
        print('i', i)
        title_text_raw = opml_anchor_page.text
        print(title_text_raw)

        if title_text_raw == 'Title: Wrapping up' or title_text_raw== 'title Let\'s take a first look at the code for this lesson.':
            continue
        print('title_text_raw', title_text_raw)
        label = 'Title: '
        assert title_text_raw.startswith(label)
        title = opml_anchor_page.text[len(label):]
        slug = title.lower().replace(' ', '-')
        slug = ''.join([char for char in slug if char.isalpha() or char == '-'])

        additional_text = ''
        label = 'VideoURL: '
        video_url = [thing for thing in opml_anchor_page if thing.text.startswith(label)][0].text[9:]
        video_title = title  # maybe change me later
        next_anchor_page_id = ''  # update me when possible
        supporting_anchor_page_id = ''  # leave as empty string for Anchor Pages
        tag_or_key_whatevs = 'QuestionForViewer: '
        question_for_viewer = [thing for thing in opml_anchor_page if thing.text.startswith(tag_or_key_whatevs)][0].text[len(tag_or_key_whatevs):]
        tag_or_key_whatevs = 'StudentResponses:'
        opml_student_responses = [thing for thing in opml_anchor_page if thing.text.startswith(tag_or_key_whatevs)][0]
        print('Student responses')
        student_responses = []
        print('hi')
        for opml_student_response in opml_student_responses:
            label = 'Response: '
            if opml_student_response.text.startswith(label):
                student_response_text = opml_student_response.text[len(label):]
                id_of_page_with_answer = ''  # todo
                student_response = Response(student_response_text, id_of_page_with_answer)
                student_responses.append(student_response)
            else:
                print('Warning: opml_student_response:', opml_student_response.text)

        print(student_responses)
        page = Page(id=str(uuid.uuid4()), is_anchor_page=True,
                    title=title, slug=slug, additional_text=additional_text,
                    video_url=video_url, video_title=video_title,
                    next_anchor_page_id=next_anchor_page_id,
                    supporting_anchor_page_id=supporting_anchor_page_id,
                    question_for_viewer=question_for_viewer,
                    student_responses=StudentResponses(student_responses))
        pages.append(page)
        print(page)

        if i == 1:
            pprint.pprint(page)
    return pages









if __name__ == '__main__':
    test_parse = True
    if test_parse:
        parse_opml_course_from_workflowy()
