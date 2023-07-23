import os
from notion_client import Client

from opyml import OPML, Outline

from dotenv import load_dotenv

from pprint import pprint

load_dotenv()

notion = Client(auth=os.environ["NOTION_TOKEN"])
#
#
# users = notion.users.list()
#
# for user in users.get("results"):
#     name, user_type = user["name"], user["type"]
#     emoji = "😅" if user["type"] == "bot" else "🙋‍♂️"
#     print(f"{name} is a {user_type} {emoji}")
#
#
#
# Search for an item
results = notion.search(query="Learn").get("results")
print(len(results))
result = results[0]
print("The result is a", result["object"])
pprint(result)
pprint(result["properties"])


document = OPML()

pprint('foo')
document.body.outlines.append(Outline(text="Example"))
block = notion.blocks.retrieve('398cf35c-258b-4d93-9c29-ca1f3b6203fa')
block_children = notion.blocks.children.list('398cf35c-258b-4d93-9c29-ca1f3b6203fa')
print(type(block_children))
pprint(block_children)
# exit()
#for child_block in block_children['results']:
document.body.outlines[0].text='asdf'
pprint(document.body.outlines[0])



 #   print(foo)

'398cf35c-258b-4d93-9c29-ca1f3b6203fa'