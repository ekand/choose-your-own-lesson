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
class Response:
    response_text: str
    id_of_page_with_answer: str

@dataclass
class StudentResponses:
    list_of_responses: list[Response] = field(default_factory=Response)

@dataclass
class Page:
    id: str
    is_anchor_page: bool
    title: str
    slug: str
    additional_text: str
    video_url: str
    video_title: str
    next_anchor_page_id: str  # may need to initialize as '' then fill in later, or may be '' for last anchor page
    supporting_anchor_page_id: str  # '' if is_anchor_page, also may need to initialize as '' then fill in later
    question_for_viewer: str  # may be zero for special pages with no questions
    student_responses: field(default_factory=StudentResponses)  # None if not is_anchor_page


