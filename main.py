import uuid
import pprint

from my_classes import Page, StudentResponses, Response
from utility import parse_opml_course_from_workflowy

pages = parse_opml_course_from_workflowy()
# print(pages)
# pprint.pprint(pages)
for page in pages:
    if page.video_title == '':
        page.video_title = page.title

#print('hello 2983572398')
for page in pages:
    print('page', page)
    if page.student_responses:
        print('page.student_responses',page.student_responses)
        for response in page.student_responses.list_of_responses:
            pass
            #assert response.id_of_page_with_answer in [page.id for page in pages]

with open('page.md') as f:
    page_template = f.read()
for page in pages:
    if page.video_url == '':
        youtube_s = ''
    else:
        video_id = page.video_url.split('/')[-1]
        youtube_s = f'### Watch this video:\n<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    questions_s = ''
    student_responses = page.student_responses
    #(student_responses)
    if not page.is_anchor_page:
        try:
            student_responses = list(filter(lambda p: p.id == page.supporting_anchor_page_id, pages))[0].student_responses
            # hacky fix to add "more" to "I have no questions"
            for response in student_responses.list_of_responses:
                if response.response_text.startswith('I have no questions'):
                    response.response_text = response.response_text.replace('no questions', 'no more questions')
        except IndexError:
            (f'Hello 2959384728932, IndexError on page with id:{page.id}')
    # print('student_responses', student_responses)
    if student_responses is not None:
        questions_s += f'###' + page.question_for_viewer + '\n\n'
        for response in student_responses.list_of_responses:
            if response.id_of_page_with_answer == '':
                id_of_page_with_answer = ''
                print('warning: putting placeholder info for response:', response)
                questions_s += f'{response.response_text}    [placeholder_title](placeholder-slug.html)\n\n'
            else:
                # print('-------')
                # print('hi!', page)
                # print(pages)
                # print(response)

                #print(response)
                #print(response.id_of_page_with_answer)
                page_with_answer = list(filter(lambda p: p.id == response.id_of_page_with_answer, pages))[0]
                slug_of_page_with_answer = page_with_answer.slug
                questions_s += f'[{response.response_text}]({slug_of_page_with_answer}.html)\n\n'
    page_s = page_template.format(page_title=page.title,
                                  page_slug=page.slug,
                                  additional_text_s=page.additional_text,
                                  youtube_s=youtube_s,
                                  questions_s=questions_s)

    with open('pelican/content/' + page.slug + '.md', 'w') as out_file:
        out_file.write(page_s)
