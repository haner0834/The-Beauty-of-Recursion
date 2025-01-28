from manim import *

PREVIOUS_ITEM_COLOR = TEAL_B
CURRENT_ITEM_COLOR = GREEN_B
CONSTANT_COLOR = BLUE_B

class RecurrenceRelationAnimation_Case2(Scene):
    strike_throughs: list[Line] = []
    objects_to_remove: list[Animation] = []

    def construct(self):
        self.camera.background_color = GRAY_E
        formula = RecurrenceRelationFormula()
        # self.add(title)
        self.play(Write(formula))

        self.wait()

        self.play(formula.animate.to_edge(UL))
        tex_objects: list[MathTex] = []

        for i in range(1, 4): 
            tex = MathTex(
                f"a_{i+1} = a_{i} + {(i+1) * 10}",
                substrings_to_isolate=[f"a_{i}", f"a_{i+1}", f"{(i+1) * 10}"]
            )
            tex.set_color_by_tex(f"{(i+1) * 10}", BLUE_B)
            tex.set_color_by_tex(f"a_{i+1}", GREEN_B)
            tex.set_color_by_tex(f"a_{i}", TEAL_B)
            tex_objects.append(tex)

        vdots = MathTex(r"\vdots")
        tex_objects.append(vdots)

        tex_n = MathTex(r"a_n = a_{n-1} + 10n", substrings_to_isolate=[r"a_n", r"a_{n-1}", "10n"])
        tex_n.set_color_by_tex(r"a_n", GREEN_B)
        tex_n.set_color_by_tex(r"a_{n-1}", TEAL_B)
        tex_n.set_color_by_tex("10n", BLUE_B)
        tex_objects.append(tex_n)

        vgroup = VGroup(*tex_objects)
        calculate_line = Line()
        vgroup.add(calculate_line)
        calculate_line.set_width(vgroup.width)

        general_terms_result = MathTex(
            r"a_n = a_1 + 20 + 30 + \cdots + 10n",
            substrings_to_isolate=[r"a_n", r"a_1", r"20 + 30 + \cdots + 10n"]
        )
        general_terms_result \
            .set_color_by_tex(r"a_n", CURRENT_ITEM_COLOR) \
            .set_color_by_tex(r"20 + 30 + \cdots + 10n", CONSTANT_COLOR) \
            .set_color_by_tex(r"a_1", PREVIOUS_ITEM_COLOR)
        vgroup.add(general_terms_result)

        vgroup.arrange(DOWN, aligned_edge=LEFT)
        vgroup.move_to(ORIGIN)

        self.wait(2)

        for i, tex in enumerate(tex_objects):
            if i == 3: self.wait(4)
            self.play(TransformFromCopy(formula, tex))

        self.highlight_a(tex_objects=tex_objects)

        self.play(Create(calculate_line))

        self.wait()

        self.eliminate_a(tex_objects=tex_objects)

        self.wait()

        self.play(Write(general_terms_result))
        
        arithmetic_sequence_part = general_terms_result.get_part_by_tex(r"20 + 30 + \cdots + 10n")
        if arithmetic_sequence_part:
            brace = BraceBetweenPoints(
                arithmetic_sequence_part.get_left(), 
                arithmetic_sequence_part.get_right(),
            )
            brace_tex = brace.get_tex(r"\times n - 1")
            self.play(
                Create(brace), Write(brace_tex)
            )

        self.wait()
        
        object_to_remove: list[Animation] = []
        for tex in tex_objects:
            object_to_remove.append(FadeOut(tex))
        lines_to_remove: list[Animation] = []
        for line in self.strike_throughs:
            lines_to_remove.append(FadeOut(line))
        # remove virtical calculation
        self.play(
            vgroup.animate.remove(tex_objects),
            object_to_remove,
            lines_to_remove,
            FadeOut(calculate_line)
        )
        # move to center
        self.play(
            general_terms_result.animate.shift(UP * 2),
            brace.animate.shift(UP * 2),
            brace_tex.animate.shift(UP * 2)
        )

        general_terms2 = MathTex(
            r"a_n = 5 + 10(\frac{(n-1)(2+n)}{2})",
            substrings_to_isolate=[r"10(\frac{(n-1)(2+n)}{2})", r"5", r"a_n"]
        )
        general_terms2 \
            .set_color_by_tex(r"a_n", CURRENT_ITEM_COLOR) \
            .set_color_by_tex(r"5", PREVIOUS_ITEM_COLOR) \
            .set_color_by_tex(r"10(\frac{(n-1)(2+n)}{2})", CONSTANT_COLOR)
        self.play(Transform(general_terms_result, general_terms2), FadeOut(brace), FadeOut(brace_tex))
        self.wait(0.7)

        general_terms3 = MathTex(r"a_n = 5 + 5[(n - 1)(2 + n)]",
                                 substrings_to_isolate=[r"5[(n - 1)(2 + n)]", r"5", r"a_n"])
        general_terms3 \
            .set_color_by_tex(r"a_n", CURRENT_ITEM_COLOR) \
            .set_color_by_tex(r"5", PREVIOUS_ITEM_COLOR) \
            .set_color_by_tex(r"5[(n - 1)(2 + n)]", CONSTANT_COLOR)
        self.play(Transform(general_terms_result, general_terms3))
        self.wait(0.7)

        general_terms4 = MathTex(r"a_n = 5 + 5(n^2 + n - 2)",
                                 substrings_to_isolate=[r"5(n^2 + n - 2)", r"5", r"a_n"])
        general_terms4 \
            .set_color_by_tex(r"a_n", CURRENT_ITEM_COLOR) \
            .set_color_by_tex(r"5", PREVIOUS_ITEM_COLOR) \
            .set_color_by_tex(r"5(n^2 + n - 2)", CONSTANT_COLOR)
        self.play(Transform(general_terms_result, general_terms4))
        self.wait(0.7)

        final_general_terms = MathTex(r"a_n = 5n^2 + 5n - 5",
                                    substrings_to_isolate=[r"5n^2 + 5n - 5", r"a_n"])
        final_general_terms \
            .set_color_by_tex(r"a_n", CURRENT_ITEM_COLOR) \
            .set_color_by_tex(r"5n^2 + 5n - 5", CONSTANT_COLOR)
        self.play(Transform(general_terms_result, final_general_terms))

        
        self.wait(3)


    def highlight_a(
            self, tex_objects: list[MathTex], 
            highlight_color: ManimColor=GOLD):
        for i in range(2):
            tex = tex_objects[i]
            next_tex = tex_objects[i+1]
            # Highlighting same item
            self.play(
                tex.animate.set_color_by_tex(f"a_{i+2}", highlight_color),
                next_tex.animate.set_color_by_tex(f"a_{i+2}", highlight_color)
            )
            # Rollback the color
            self.play(
                tex.animate.set_color_by_tex(f"a_{i+2}", CURRENT_ITEM_COLOR),
                next_tex.animate.set_color_by_tex(f"a_{i+2}", PREVIOUS_ITEM_COLOR)
            )
            self.wait()

    def eliminate_a(self, tex_objects: list[MathTex]):
        ...


class RecurrenceRelationFormula(VGroup):
    first = MathTex()
    second = MathTex()
    brace = None

    def __init__(self):
        super().__init__()
        vgroup = VGroup()

        self.first = MathTex("a_1 = 5", substrings_to_isolate=["a_1", "5"])
        self.first \
            .set_color_by_tex("5", PREVIOUS_ITEM_COLOR) \
            .set_color_by_tex("a_1", PREVIOUS_ITEM_COLOR)

        self.second = MathTex("a_n = a_{n-1} + 10n, n \geq 2", substrings_to_isolate=["a_n", "a_{n-1}", "10n"])
        self.second \
            .set_color_by_tex("a_{n-1}", PREVIOUS_ITEM_COLOR) \
            .set_color_by_tex("a_n", CURRENT_ITEM_COLOR) \
            .set_color_by_tex("10n", CONSTANT_COLOR)
            
        vgroup \
            .add(self.first, self.second) \
            .arrange(DOWN, aligned_edge=LEFT)

        self.brace = BraceBetweenPoints(vgroup.get_top() + 0.2, vgroup.get_bottom() + 0.2)

        self.add(self.brace, vgroup)
        self.arrange(RIGHT)

    def write_animation(self) -> list[Animation]:
        return [Write(self.first), Write(self.second), Write(self.brace)]