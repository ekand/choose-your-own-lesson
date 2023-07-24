import os

import opml
from notion_client import Client

from opyml import OPML, Outline

from dotenv import load_dotenv

# from utility import parse_opml_course_from_workflowy

from pprint import pprint




def setup_notion():
    load_dotenv()
    notion = Client(auth=os.environ["NOTION_TOKEN"])
    return notion


    # ID = '398cf35c-258b-4d93-9c29-ca1f3b6203fa'


# document = OPML()
# document.body.outlines.append(Outline(text="Example"))



# children = notion.blocks.children.list(ID)



def walk_and_print_opml(opml_outline, indent = 0, max_depth_to_print = 2):

    # # not this? # assert(type(opml_outline) == opml.OutlineElement), f'type(opml_outline) was {type(opml_outline)}'
    output_s = ''
    indent_steepness = 3
    if opml_outline is None:
        return
    if indent < max_depth_to_print:
        output_s += ' ' * indent_steepness + opml_outline.text

    for inner_outline in opml_outline.outlines:
        walk_and_print_opml(inner_outline, indent + 1)

    return output_s

recursion_iteration_counter = 0
RECURSION_ITERATION_MAXIMUM = 1000

maximum_recusion_depth_to_print = 3

def walk_children(child_id, document=None, outline=None, notion=None, debug=False):
    """Walk through Notion blocks, recursively including children,
    and store plain text values to an opml outline"""
    print('hi 29857')

    # this is hacky
    global recursion_iteration_counter

    recursion_iteration_counter += 1
    if recursion_iteration_counter > RECURSION_ITERATION_MAXIMUM:
        return outline, document

    if notion is None:
        notion = setup_notion()

    if document is None:
        document = OPML()
        document.body.outlines.append(Outline(text="Outline"))
        outline = document.body.outlines[0]

    children = notion.blocks.children.list(child_id)

    if debug:
        print('hi debug 1234123')
        #walk_and_print_opml(outline)

    for child in children['results'][1:]:
        child_id = child['id']
        block = notion.blocks.retrieve(child_id)
        print(block)
        the_type = block['type']
        # text = block[the_type]['rich_text'][0]['plain_text']
        current_outline = None
        for rich_text_object in block[the_type]['rich_text']:
            text = rich_text_object['plain_text']
            current_outline = Outline(text=text)
            outline.outlines.append(current_outline)
        if child['has_children'] and current_outline is not None:
            # walk_and_print_opml(outline)
            walk_children(child['id'], notion=notion, outline=current_outline)
            # walk_and_print_opml(outline)
    return outline, document


if __name__ == '__main__':
    ID = '398cf35c258b4d939c29ca1f3b6203fa'
    test_opml_outline = walk_children(ID, debug=True)
    print(type(test_opml_outline))
    # test_opml_outline = parse_opml_course_from_workflowy(return_outline_too=True)[1]
    #print(walk_and_print_opml(test_opml_outline))
