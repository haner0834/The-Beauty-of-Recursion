from manim import *

PREVIOUS_ITEM_COLOR = TEAL_B
CURRENT_ITEM_COLOR = GREEN_B
CONSTANT_COLOR = BLUE_B

class SpecialRecurrenceRelationAnimation(Scene):
    def construct(self):
        self.camera.background_color = GRAY_E
        formula = RecurrenceRelationFormula()
        # self.add(title)
        self.play(Write(formula))

        self.wait()

        self.play(formula.animate.to_edge(UL))
        tex_objects: list[MathTex] = []

        results: list[MathTexData] = [
            MathTexData(content=r"a_2 = \frac{-1 - 7}{-3 -5} = {1}", sub_strings=["1"]),
            MathTexData(content=r"a_3 = \frac{1 - 7}{3 - 5} = {3}", sub_strings=["3"]),
            MathTexData(content=r"a_4 = \frac{3 - 7}{9 - 5} = {-1}", sub_strings=["-1"])
        ]
        for result in results: 
            tex = MathTex(result.content)
            tex_objects.append(tex)

        vgroup = VGroup(*tex_objects)

        vgroup.arrange(DOWN, aligned_edge=LEFT)
        vgroup.move_to(ORIGIN)

        self.wait(2)

        for i, tex in enumerate(tex_objects):
            if i == 3: self.wait(4)
            self.play(TransformFromCopy(formula, tex))

        self.wait(3)
        
        self.play(list(map(lambda x: FadeOut(x), tex_objects)))

        tex_objects.clear()
        vgroup.remove(*tex_objects)

        item_results = [-1, 3, 1]
        for i in range(6):
            tex_objects.append(MathTex(f"a_{i+1} = {item_results[i%3]}"))
        
        hgroup = VGroup(*tex_objects)
        hgroup.arrange(RIGHT) 
        hgroup.move_to(ORIGIN)
        
        for object in tex_objects:
            self.play(Write(object))

        self.wait(3)

        objects_to_remove: list[Animation] = [
            *list(map(lambda x: FadeOut(x), tex_objects)),
            FadeOut(formula)
        ]
        self.play(objects_to_remove)

class MathTexData:
    content: str = ""
    sub_strings: list[str] =[]
    def __init__(self, content: str = "", sub_strings: list[str] = []):
        self.content = content
        self.sub_strings = sub_strings

class RecurrenceRelationFormula(VGroup):
    first = MathTex()
    second = MathTex()
    brace = None

    def __init__(self):
        super().__init__()
        vgroup = VGroup()

        self.first = MathTex("a_1 = -1", substrings_to_isolate=["a_1", "-1"])
        self.first \
            # .set_color_by_tex("-1", PREVIOUS_ITEM_COLOR) \
            # .set_color_by_tex("a_1", PREVIOUS_ITEM_COLOR)

        self.second = MathTex(r"a_{n+1} = \frac{a_n - 7}{3a_n - 5} , n \in \mathbb{N}", substrings_to_isolate=["a_{n+1}", "3a_n - 5"])
        self.second \
            # .set_color_by_tex("a_{n+1}", CURRENT_ITEM_COLOR) \
            
        vgroup \
            .add(self.first, self.second) \
            .arrange(DOWN, aligned_edge=LEFT)

        self.brace = BraceBetweenPoints(vgroup.get_top() + 0.2, vgroup.get_bottom() + 0.2)

        self.add(self.brace, vgroup)
        self.arrange(RIGHT)

    def write_animation(self) -> list[Animation]:
        return [Write(self.first), Write(self.second), Write(self.brace)]