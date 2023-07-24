import pickle
import pprint
import uuid
import opml
import copy

from opyml import OPML

import notion_play
from my_classes import Page, Response, StudentResponses


def parse_opml_course_from_workflowy(return_outline_too=False, debug_output=False):

    outline2 = opml.parse('input/pages.opml')
    #ID = '398cf35c258b4d939c29ca1f3b6203fa'
    # ID = 'd23b3d26680241328840448db039ee6e'
    ID = 'c929fc48e3354c0894e09b393975bb7f'


    load_from_notion = False
    if load_from_notion:
        opyml_outline = notion_play.walk_children(ID)
        document = OPML()
        document.body.outlines.append(opyml_outline)
        with open('interim/opyml_document.xml', 'w') as f:
            f.write(document.to_xml())
    parsed_xml = opml.parse('interim/opyml_document.xml')
    opml_outline = parsed_xml[0]
    # outline = other_thingy
    # print(outline)
    #opml_learn_python_by_making_music = other_thingy
    #print(type(opml_learn_python_by_making_music))
    #opml_the_code = outline[0]
    opml_anchor_pages = opml_outline[0]
    opml_special_pages = opml_outline[1]
    pages = []
    future_anchor_page = None
    special_pages = []
    for i, opml_special_page in enumerate(opml_special_pages):
        if debug_output:
            print('i', i, 'hello 289457298374')
        title_text_raw = opml_special_page.text
        label = 'Title: '
        assert title_text_raw.startswith(label)
        title = opml_special_page.text[len(label):]
        slug = slugify(title)
        label = 'AdditionalText: '
        for thing in opml_special_page:
            if debug_output:
                print(thing.text, 'hello 298457')
        additional_text = [thing for thing in opml_special_page if thing.text.startswith(label)][0].text[len(label):]
        label = 'VideoURL: '
        video_url = [thing for thing in opml_special_page if thing.text.startswith(label)][0].text[len(label):]
        video_title = title
        special_page = Page(id=str(uuid.uuid4()), is_anchor_page=False, title=title, slug=slug,
                            additional_text=additional_text, video_title=video_title, video_url=video_url,
                            next_anchor_page_id='', supporting_anchor_page_id='', question_for_viewer='', student_responses=None)
        pages.append(special_page)
        special_pages.append(special_page)
    for i, opml_anchor_page in enumerate(opml_anchor_pages[::-1]):
        if debug_output:
            print('i', i)
        title_text_raw = opml_anchor_page.text
        if title_text_raw == 'Title: Wrapping up' or title_text_raw== 'title Let\'s take a first look at the code for this lesson.':
            continue
        if title_text_raw == 'Title: First Look At The Code':
            continue
        #if title_text_raw == 'Title: Software Setup':
         #   continue
        if debug_output:
            print('title_text_raw', title_text_raw)
        label = 'Title: '
        assert title_text_raw.startswith(label)
        title = opml_anchor_page.text[len(label):]
        slug = slugify(title)
        additional_text = ''
        label = 'VideoURL: '
        video_url = [thing for thing in opml_anchor_page if thing.text.startswith(label)][0].text[9:]
        video_title = title  # maybe change me later
        try:
            next_anchor_page_id = future_anchor_page.id
        except Exception as e:
            print(e)
            next_anchor_page_id = ''

        supporting_anchor_page_id = ''  # leave as empty string for Anchor Pages
        tag_or_key_whatevs = 'QuestionForViewer: '
        question_for_viewer = [thing for thing in opml_anchor_page if thing.text.startswith(tag_or_key_whatevs)][0].text[len(tag_or_key_whatevs):]
        tag_or_key_whatevs = 'StudentResponses:'
        opml_student_responses = [thing for thing in opml_anchor_page if thing.text.startswith(tag_or_key_whatevs)][0]
        # ('Student responses')
        student_responses = []
        # rint('hi')
        supporting_pages = []
        for opml_student_response in opml_student_responses:
            label = 'Response: '
            if opml_student_response.text.startswith(label):
                # print('opml_student_response.text', opml_student_response.text)
                student_response_text = opml_student_response.text[len(label):]
                id_of_page_with_answer = ''  # todo
                student_response = Response(student_response_text, id_of_page_with_answer)
                student_responses.append(student_response)
                supporting_page_title_raw_text = opml_student_response[0].text
                label = 'Title: '
                assert supporting_page_title_raw_text.startswith(label)

                supporting_page_title = supporting_page_title_raw_text[len(label):]
                supporting_page_slug = slugify(supporting_page_title)
                supporting_page_additional_text = ''  # todo
                label = 'VideoURL: '
                supporting_page_video_url = [child for child in opml_student_response[0] if child.text.startswith(label)][0].text
                supporting_page_video_title = supporting_page_title  # todo finesse me
                label = 'QuestionForViewer: '
                supporting_page_question_for_viewer = [child for child in opml_student_response[0] if child.text.startswith(label)][0].text[len(label):]
                next_anchor_page_id = future_anchor_page.id if future_anchor_page else ''
                student_responses_for_supporting_page = copy.deepcopy(student_responses)
                if future_anchor_page is not None:
                    student_responses_for_supporting_page.append(Response("<this will never get displayed> I have no further questions, take me to the next Anchor Video:", future_anchor_page.id))
                supporting_page = Page(id=str(uuid.uuid4()), is_anchor_page=False,
                                       title=supporting_page_title, slug=supporting_page_slug,
                                       additional_text=supporting_page_additional_text,
                                       video_url=supporting_page_video_url,
                                       video_title=supporting_page_video_title,
                                       next_anchor_page_id=next_anchor_page_id,
                                       supporting_anchor_page_id='',  # fill in later, with the id of the anchor page that's about to be created
                                       question_for_viewer=supporting_page_question_for_viewer,
                                       student_responses=StudentResponses(student_responses_for_supporting_page)
                                       )
                supporting_pages.append(supporting_page)

            else:
                print('Warning: opml_student_response:', opml_student_response.text)

        # print(student_responses)
        if future_anchor_page is not None:
            student_responses.append(Response("I have no questions, take me to the next Anchor Video:", future_anchor_page.id))
        page = Page(id=str(uuid.uuid4()), is_anchor_page=True,
                    title=title, slug=slug, additional_text=additional_text,
                    video_url=video_url, video_title=video_title,
                    next_anchor_page_id=next_anchor_page_id,
                    supporting_anchor_page_id=supporting_anchor_page_id,
                    question_for_viewer=question_for_viewer,
                    student_responses=StudentResponses(student_responses))

        # page.student_responses = StudentResponses([Response('sometext', 'some_id')])
        #StudentResponses([Response()])
        #print('for response, answer_page in zip(page.student_responses.list_of_responses, supporting_pages):')
        #print('page.student_responses.list_of_responses', page.student_responses.list_of_responses)
        #print('supporting_pages', supporting_pages)
        for response, answer_page in zip(page.student_responses.list_of_responses, supporting_pages):
            response.id_of_page_with_answer = answer_page.id
        for supporting_page in supporting_pages:
            supporting_page.supporting_anchor_page_id = page.id
        pages.append(page)
        pages.extend(supporting_pages)
        future_anchor_page = page
        # print(page)
    for page in pages:
        # this is so hacky
        if not page.title.startswith("So you have a question that wasn"):
            print(page.title)
            page.student_responses.list_of_responses.append(
                Response('I have a question not listed here.', special_pages[0].id)
            )

    # if return_outline_too:
    #     return pages, opml_learn_python_by_making_music

    return pages


def slugify(text):
    text = text.lower().replace(' ', '-')
    return ''.join([char for char in text if char.isalpha() or char == '-'])

if __name__ == '__main__':
    test_parse = True
    if test_parse:
        parse_opml_course_from_workflowy()
