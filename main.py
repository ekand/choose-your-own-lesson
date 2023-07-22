import uuid
import pprint

from my_classes import Page, StudentResponses, Response
from utility import parse_opml_course_from_workflowy

pages = []
question_not_listed_page = Page(id=str(uuid.uuid4()), is_anchor_page=True,
                                title="So you have a question that wasn't listed for you.", slug='other-question',
                                additional_text="You've come to this page because you have a question that wasn't listed on the previous page. Please follow [this GitHub link](https://github.com/ekand/choose-your-own-lesson/issues){:target=\"_blank\"} and click 'New issue' to raise the issue with this project's maintainer. Then return here and push the back button on your browser to continue with the lesson as best you can.",
                                video_url='',
                                video_title='',
                                next_anchor_page_id='',
                                supporting_anchor_page_id='',
                                question_for_viewer='',
                                student_responses=None)
pages.append(question_not_listed_page)

question_not_listed_response = Response(response_text='I have a question that is not listed here:',
                                        id_of_page_with_answer=question_not_listed_page.id)
# what_does_equal_do = Page(str(uuid.uuid4()), 'What Does The Equal Sign Do?', 'what-does-equal-do', '',
#                           'https://youtu.be/<id>', '',
#                           StudentResponses("Do you have any questions?",
#                                             [Response("I have no questions", done_page.id),
#                                              Response("What is this?", what_is_this.id)]))
#
# why_quotes = Page(str(uuid.uuid4()), 'Why Is Hello World Wrapped In Quotes?', 'why-quotes', '', 'https://youtu.be/<id>',
#                   '',
#                   StudentResponses("Do you have any questions?",
#                                     [Response("I have no questions", done_page.id),
#                                      Response("What does the equal sign do?", what_does_equal_do.id)]))

next_anchor_page = Page(id=str(uuid.uuid4()), is_anchor_page=True,
                        title="<next anchor page>", slug="next-anchor-page",
                        additional_text='',
                        video_url='https://youtu.be/<id>?start=10&end=20',
                        video_title='',
                        next_anchor_page_id='',
                        supporting_anchor_page_id='',
                        question_for_viewer='<question for viewer>',
                        student_responses=None)
pages.append(next_anchor_page)

install_python_page = Page(id=str(uuid.uuid4()), is_anchor_page=False,
                           title='Install Python', slug='install-python',
                           additional_text='See this video for instructions on how to install Python',
                           video_url='https://youtu.be/<id>?start=10&end=20',
                           video_title='<video_title>',
                           next_anchor_page_id=next_anchor_page.id,
                           supporting_anchor_page_id='',
                           question_for_viewer='Do you have any additional questions?',
                           student_responses=None, )
pages.append(install_python_page)

install_pycharm_page = Page(id=str(uuid.uuid4()), is_anchor_page=False,
                            title='Install PyCharm Community Edition', slug='install-pycharm',
                            additional_text='',
                            video_url='https://youtu.be/<id>?start=10&end=20',
                            video_title='<video_title>',
                            next_anchor_page_id=next_anchor_page.id,
                            supporting_anchor_page_id='',
                            question_for_viewer='<question for viewer>',
                            student_responses=None)
pages.append(install_pycharm_page)

software_setup_page = Page(id=str(uuid.uuid4()), is_anchor_page=True, title='Software Setup', slug='software-setup',
                           additional_text='',
                           video_url='https://youtu.be/<id>?start=10&end=20',
                           video_title='<video title>',
                           next_anchor_page_id='<next_anchor_page_id>',
                           supporting_anchor_page_id='',
                           question_for_viewer='Do you have any questions?',
                           student_responses=StudentResponses(
                               [Response('How do I install Python? Can you guide me '
                                         'through the steps for my computer in '
                                         'detail?', install_python_page.id),

                                Response('How do I install PyCharm Community Edition? '
                                         'Can you guide me'
                                         'through the steps for my computer in '
                                         'detail?', install_pycharm_page.id)]))
pages.append(software_setup_page)

install_python_page.supporting_anchor_page_id = software_setup_page.id
install_pycharm_page.supporting_anchor_page_id = software_setup_page.id

# done_page = Page(str(uuid.uuid4()), "You are done.", 'done',
#                  '', 'https://youtu.be/6xi0Uw9XU_U', 'Done video', None)
#
# what_is_this = Page(str(uuid.uuid4()), "What is this??", 'what', '', 'https://youtu.be/guHNT6lAa5I',
#                     'What is this video',
#                     PossibleQuestions("Do you have any questions?",
#                                       [Response("I have no questions", done_page.id)]))
#
# template_page = Page(str(uuid.uuid4()), 'Lesson Title', 'first', '', 'https://youtu.be/<id>', '',
#                      PossibleQuestions("Do you have any questions?",
#                                        [Response("I have no questions", done_page.id),
#                                         Response("<question_text>?", what_is_this.id),
#                                         Response("<question_text>?", what_is_this.id)]))

why_python_music_page = Page(id=str(uuid.uuid4()), is_anchor_page=False,
                             title='Why You Might Want To Learn Python By Making Music', slug='why-python-music',
                             additional_text='',
                             video_url='https://youtu.be/<id>?start=10&end=20',
                             video_title='',
                             next_anchor_page_id=software_setup_page.id,
                             supporting_anchor_page_id='',
                             question_for_viewer='Do you have any additional questions?',
                             student_responses=None)
pages.append(why_python_music_page)

what_choose_your_own_lesson_page = Page(id=str(uuid.uuid4()), is_anchor_page=False,
                                        title='Choose Your Own Lesson', slug='choose-your-own-lesson',
                                        additional_text='',
                                        video_url='https://youtu.be/<id>?start=10&end=20',
                                        video_title='',
                                        next_anchor_page_id=software_setup_page.id,
                                        supporting_anchor_page_id='',
                                        question_for_viewer='Do you have any additional questions?',
                                        student_responses=None)
pages.append(what_choose_your_own_lesson_page)
welcome_page = Page(id=str(uuid.uuid4()), is_anchor_page=True,
                    title='Welcome To Learn Python By Making Music: Hello World', slug='welcome',
                    additional_text='',
                    video_url='https://youtu.be/80tv4j052H4',
                    video_title='Welcome Video',
                    next_anchor_page_id=software_setup_page.id,
                    supporting_anchor_page_id='',
                    question_for_viewer='Do you have any questions for now?',
                    student_responses=StudentResponses(
                        [Response("Why would I want to learn Python By making music?", why_python_music_page.id),
                         Response("What is Choose Your Own Lesson?", what_choose_your_own_lesson_page.id),
                         Response("I have no questions, take me to the next Anchor Video:", software_setup_page.id),
                         question_not_listed_response]))
welcome_page.supporting_anchor_page_id = welcome_page.id
why_python_music_page.supporting_anchor_page_id = welcome_page.id
what_choose_your_own_lesson_page.supporting_anchor_page_id = welcome_page.id
pages.append(welcome_page)

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
                questions_s += f'{response.response_text}    [{page_with_answer.title}]({slug_of_page_with_answer}.html)\n\n'
    page_s = page_template.format(page_title=page.title,
                                  page_slug=page.slug,
                                  additional_text_s=page.additional_text,
                                  youtube_s=youtube_s,
                                  questions_s=questions_s)

    with open('pelican/content/' + page.slug + '.md', 'w') as out_file:
        out_file.write(page_s)
