from manim import *
from default_value import *

class TopTitle(Text):
    def __init__(self, text, color=WHITE, **kwargs):
        super().__init__(text, color=color, font_size=TITLE_TEXT_FONT_SIZE, **kwargs)
        self \
            .to_edge(UP, buff=0.5)