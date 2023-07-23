from opyml import OPML, Outline

document = OPML()
document.body.outlines.append(Outline(text="Example"))

for c in ['a', 'b', 'c']:
    my_outline = Outline(text=c)
    document.body.outlines[0].outlines.append(my_outline)
    for num in [1, 2, 3]:
        my_outline.outlines.append(Outline(text=str(num)))


print(document)
