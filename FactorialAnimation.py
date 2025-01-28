from manim import *
from default_value import *

class FactorialAnimation(Scene):
    def construct(self):
        self.camera.background_color = GRAY_E
        title = Text("階乘 Factorial", font_size=TITLE_TEXT_FONT_SIZE)
        title \
            .to_edge(UP) \
            .shift(DOWN * 0.2)
        self.add(title)

        factorial_definition = MathTex(
            "n!", "=", "n \\times", "(n-1) \\times (n-2) \\times \\cdots \\times 2 \\times 1"
        )
        self.play(Write(factorial_definition))
        self.wait()

        self.play(factorial_definition[3].animate.set_color(BLUE_B))
        self.wait()

        factorial_definition2 = MathTex(
            "n!", "=", "n \\times", "(n - 1)!"
        )
        factorial_definition2[3].set_color(BLUE_B)
        self.play(Transform(factorial_definition, factorial_definition2))
        self.wait()

        self.play(factorial_definition.animate.shift(UP * 2))
        self.wait()

        image = ImageMobject("assets/factorial_recursive.png")
        image\
            .scale(1.5) \
            .shift(DOWN * 0.4)
        self.play(FadeIn(image))
        self.wait()

        self.play(image.animate.to_edge(LEFT).shift(RIGHT * 0.2))

        image1 = ImageMobject("assets/factorial_iterative.png")
        image1\
            .scale(1.5) \
            .shift(DOWN * 0.4) \
            .to_edge(RIGHT) \
            .shift(LEFT * 0.3)
        self.play(FadeIn(image1))
        self.wait()

        description_recursion = Text("遞迴解", font_size=25)
        description_recursion \
            .next_to(image, DOWN) \
            .shift(DOWN * 0.1) \
            .set_color(GRAY)
        description_iterate = Text("迴圈解", font_size=25)
        description_iterate \
            .next_to(image1, DOWN) \
            .shift(DOWN * 0.1) \
            .set_color(GRAY)
        
        self.play(Write(description_recursion), Write(description_iterate))
        self.wait(3)

        object_to_remove: list[Animation] = [
            FadeOut(title), FadeOut(factorial_definition), 
            FadeOut(description_iterate), FadeOut(description_recursion),
            FadeOut(image), FadeOut(image1)
        ]
        self.play(object_to_remove)

