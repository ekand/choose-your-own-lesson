import os

import time

from notion_client import Client

import asyncio

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



def blocking_function(id):
    return asyncio.run(walk_children(id))

def walk_and_print_opml(opml_outline, indent = 0, max_depth_to_print = 2):
    #assert(type(opml_outline) == opml.OutlineElement), f'type(opml_outline) was {type(opml_outline)}'
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


def retrieve_notion_block(child_id, notion):
    block = notion.blocks.retrieve(child_id)
    return block


async def factorial_example_to_retrieve_block():
    pass


async def walk_children(child_id, outline=None, notion=None, debug=False):
    """Walk through Notion blocks, recursively including children,
    and store plain text values to an opml outline"""

    # this is hacky
    global recursion_iteration_counter

    recursion_iteration_counter += 1
    if recursion_iteration_counter > RECURSION_ITERATION_MAXIMUM:
        print('maxed out!')
        return outline

    if notion is None:
        notion = setup_notion()

    if outline is None:
        document = OPML()
        document.body.outlines.append(Outline(text="Outline"))
        outline = document.body.outlines[0]

    children = notion.blocks.children.list(child_id)
    print('children', children)
    if debug:
        # print('hi debug 1234123')
        walk_and_print_opml(outline)
    tasks = []
    for child in children['results'][:]:
        tasks.append(asyncio.create_task(get_block_and_children(child, notion, outline)))
    print('tasks', tasks)
    await asyncio.gather(*tasks)
    # def main3():
    #     L = await asyncio.gather(
    #         tuple([my_coro for my_coro in get_block_and_children(child, notion, outline)]))


    # asyncio.run(main3())

    # async def factorial(name, number):
    #     f = 1
    #     for i in range(2, number + 1):
    #         print(f"Task {name}: Compute factorial({number}), currently i={i}...")
    #         await asyncio.sleep(1)
    #         f *= i
    #     print(f"Task {name}: factorial({number}) = {f}")
    #     return f
    #
    # async def main2():
    #     # Schedule three calls *concurrently*:
    #     L = await asyncio.gather(
    #         factorial("A", 2),
    #         factorial("B", 3),
    #         factorial("C", 4),
    #     )
    #     print(L)
    #
    # asyncio.run(main2())






    # background_tasks = set()
    #
    # # for i in range(10):
    # print(f"started at {time.strftime('%X')}")
    # for child in children['results'][:]:
    #     task = asyncio.create_task(get_block_and_children(child, notion, outline))
    #     #task = asyncio.create_task(some_coro(param=i))
    #
    #     # Add task to the set. This creates a strong reference.
    #     background_tasks.add(task)
    #
    #     # To prevent keeping references to finished tasks forever,
    #     # make each task remove its own reference from the set after
    #     # completion:
    #     task.add_done_callback(background_tasks.discard)
    # # [task for task in background_tasks]
    # print(f"finished at {time.strftime('%X')}")
    return outline


async def get_block_and_children(child, notion, outline):
    print('hello 923857')
    child_id = child['id']
    block = retrieve_notion_block(child_id, notion)
    print('block', block)
    the_type = block['type']
    # text = block[the_type]['rich_text'][0]['plain_text']
    current_outline = None
    for rich_text_object in block[the_type]['rich_text']:
        text = rich_text_object['plain_text']
        print(text)
        print('hello 9123857')
        # print([][0])
        current_outline = Outline(text=text)
        outline.outlines.append(current_outline)
    if child['has_children']:
        walk_and_print_opml(outline)
        await walk_children(child['id'], notion=notion, outline=current_outline)
        walk_and_print_opml(outline)


async def get_children_of_block(block_id, notion):
    return notion.blocks.children.list(block_id)


if __name__ == '__main__':
    ID = '398cf35c258b4d939c29ca1f3b6203fa'
    ID = 'd23b3d26680241328840448db039ee6e'
    test_opml_outline = walk_children(ID, debug=True)
    print(type(test_opml_outline))
#    test_opml_outline = parse_opml_course_from_workflowy(return_outline_too=True)[1]
    print(walk_and_print_opml(test_opml_outline))
