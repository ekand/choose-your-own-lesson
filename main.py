import uuid

from my_classes import Page, NextLessonStructure, Answer

done_page = Page(str(uuid.uuid4()), "You are done.", 'done', 'https://youtube.com/done', 'Done video', None)
what_is_this = Page(str(uuid.uuid4()), "What is this??", 'what', 'https://youtube.com/whatisthis', 'What is this video',
                    NextLessonStructure("Do you have any questions?",
                                        [Answer("I have no questions", done_page.id)]))

first_page = Page(str(uuid.uuid4()), 'First Lesson', 'first', 'https://youtube.com/first', 'First video',
                  NextLessonStructure("Do you have any questions?",
                                      [Answer("I have no questions", done_page.id),
                                       Answer("What is this?", what_is_this.id)]))
pages = [first_page, what_is_this, done_page]

for page in pages:
    with open('pelican/content/' + page.slug + '.md', 'w') as out_file:

        s = f'Title: {page.title}\nDate: 2023-07-21\n Category: Lesson\nslug: {page.slug}\n\n' \
            f'{page.title}\n\n' \
            f'###Watch this video then come back: [{page.video_title}]({page.video_url})\n\n'
        if page.next_lesson is not None:
            s += f'###' + page.next_lesson.question_text + '\n\n'

            for answer in page.next_lesson.list_of_answers:
                s += f'{answer.answer_text}    [Go here]({list(filter(lambda p: p.id == answer.id_of_page_with_answer, pages))[0].slug}.html)\n\n'

        out_file.write(s)
