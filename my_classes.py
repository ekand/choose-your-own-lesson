from dataclasses import dataclass, field

# @dataclass
# class InventoryItem:
#     """Class for keeping track of an item in inventory."""
#     name: str
#     unit_price: float
#     quantity_on_hand: int = 0
#
#     def total_cost(self) -> float:
#         return self.unit_price * self.quantity_on_hand
@dataclass
class Answer:
    answer_text: str
    id_of_page_with_answer: str

@dataclass
class NextLessonStructure:
    question_text: str
    list_of_answers: list[Answer] = field(default_factory=Answer)

@dataclass
class Page:
    id: str
    title: str
    slug: str
    video_url: str
    video_title: str
    next_lesson: field(default_factory=NextLessonStructure)

