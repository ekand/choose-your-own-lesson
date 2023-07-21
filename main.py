import uuid

from my_classes import Page, NextLessonStructure, Answer

done_page = Page(str(uuid.uuid4()), "You are done.", 'done', 'https://youtu.be/6xi0Uw9XU_U', 'Done video', None)

what_is_this = Page(str(uuid.uuid4()), "What is this??", 'what', 'https://youtu.be/guHNT6lAa5I', 'What is this video',
                    NextLessonStructure("Do you have any questions?",
                                        [Answer("I have no questions", done_page.id)]))

template_page = Page(str(uuid.uuid4()), 'Lesson Title', 'first', 'https://youtu.be/<id>', '',
                     NextLessonStructure("Do you have any questions?",
                                         [Answer("I have no questions", done_page.id),
                                          Answer("<question_text>?", what_is_this.id),
                                          Answer("<question_text>?", what_is_this.id)]))

what_does_equal_do = Page(str(uuid.uuid4()), 'What Does The Equal Sign Do?', 'what-does-equal-do',
                          'https://youtu.be/<id>', '',
                          NextLessonStructure("Do you have any questions?",
                                              [Answer("I have no questions", done_page.id),
                                               Answer("What is this?", what_is_this.id)]))

why_quotes = Page(str(uuid.uuid4()), 'Why Is Hello World Wrapped In Quotes?', 'why-quotes', 'https://youtu.be/<id>', '',
                  NextLessonStructure("Do you have any questions?",
                                      [Answer("I have no questions", done_page.id),
                                       Answer("What does the equal sign do?", what_does_equal_do.id)]))

first_page = Page(str(uuid.uuid4()), 'Learn Python By Making Music: First Lesson', 'first',
                  'https://youtu.be/80tv4j052H4', 'First video',
                  NextLessonStructure("Do you have any questions?",
                                      [Answer("I have no questions", done_page.id),
                                       Answer("What does the equal sign do?", what_does_equal_do.id),
                                       Answer("Why is Hello World wrapped in quotes?", what_is_this.id),
                                       ]))

pages = [first_page, why_quotes, what_does_equal_do, what_is_this, done_page]
for page in pages:
    if page.video_title == '':
        page.video_title = page.title

for page in pages:
    video_id = page.video_url.split('/')[-1]
    youtube_s = f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    s = f'Title: {page.title}\nDate: 2023-07-21\nCategory: Lesson\nslug: {page.slug}\n\n' \
        f'###Watch this video:  ' \
        f'{youtube_s}  \n'
    if page.next_lesson is not None:
        s += f'###' + page.next_lesson.question_text + '\n\n'

        for answer in page.next_lesson.list_of_answers:
            s += f'{answer.answer_text}    [Go here]({list(filter(lambda p: p.id == answer.id_of_page_with_answer, pages))[0].slug}.html)\n\n'
    with open('pelican/content/' + page.slug + '.md', 'w') as out_file:
        out_file.write(s)