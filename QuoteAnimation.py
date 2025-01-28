from manim import *

class QuoteAnimation(Scene):
    def construct(self):
        self.camera.background_color = GRAY_E

        quote = "To iterate is human, to recursion is divine."
        quote_text = Text(quote, font="")
        author = "— L. Peter Deutsch"
        author_text = Text(author, color=GRAY_B, font_size=DEFAULT_FONT_SIZE - 5)

        group = VGroup(quote_text, author_text)
        group.arrange(DOWN, aligned_edge=LEFT)

        self.play(Write(quote_text))
        self.play(Write(author_text))
        self.wait(3)
        self.play(FadeOut(quote_text, author_text))
        self.wait()

