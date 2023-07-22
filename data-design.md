# Data Design

page will be a web page
It will have
- title
- id (uuid?)
- questions [list of question]


question will have
- [list of quetiontexts]

be more informal

users will see a page like this:

<lesson title>
<embedded youtube video>
Do you have an questions?
- I have no questions
- what is a variable in Python?
- Why is 'Hello World' in quotation marks?
Next Lesson

What will we call these data

page has
title
youtube url
next lesson structure
question
[possible answers]

question has
question text
list of possible answers, each pointing to a page's id


There is a distinction between "Anchor Videos" and "Supporting Videos"
An Anchor video will have possible questions, and also get "I have no questions."
A Supporting video will have all the possible questions from its associated Anchor video, and also get "I have no further questions."

If a student on an anchor video clicks "I have not questions," they go to the next anchor video. If a student clicks "I have no further questions" on a Supporting Video, they will also go to the next Anchor Video. Otherwise, they will go to a Supporting Video.

How will I design this data?
How about a flag for Anchor Video(boolean)?
That should be enough.