from manim import *

NUMBERS = [34, 57, 23, 18, 43, 37, 25, 41, 50, 28]
SORTED_NUMBERS = sorted(NUMBERS)

class MergeSortAnimation(Scene):
    number_tex_objects: list[MathTex] = []
    # To store every stack of group, and iterate it when running.
    # One stack has one or more number tex(already in vgroup),
    # and one or more stack combined into a "floor", which is 
    # on the same horizontal level.
    vgroups: list[list[list[MathTex]]] = []
    numbers: list[list[list[int]]] = []

    def construct(self):
        self.camera.background_color = GRAY_E

        # Create tex objects
        for number in NUMBERS:
            self.number_tex_objects.append(self.make_number_tex(number=number))

        # Showing first "floor"
        vgroup = VGroup(*self.number_tex_objects)
        vgroup \
            .arrange(RIGHT, buff=0.7) \
            .to_edge(UP) \
            .shift(DOWN * 0.7)
        self.vgroups.append([self.number_tex_objects])

        self.show_numbers(self.number_tex_objects)

        # rec=SurroundingRectangle(vgroup, buff=0.4, color=GOLD_B, corner_radius=0.16)
        # rec.set_stroke(width=5)
        # self.play(Create(rec))
        self.wait()

        # Split it into second "floor"
        middle_index = len(NUMBERS) // 2
        left_tex_objects = list(map(lambda x: MathTex(f"{x}", substrings_to_isolate=[f"{x}"]), NUMBERS[0:middle_index]))
        right_tex_objects = list(map(lambda x: MathTex(f"{x}", substrings_to_isolate=[f"{x}"]), NUMBERS[middle_index:]))
        left_vgroup = VGroup(*left_tex_objects) \
            .arrange(RIGHT, buff=0.5) \
            .to_edge(LEFT) \
            .shift(RIGHT * 0.7)
        right_vgroup = VGroup(*right_tex_objects) \
            .arrange(RIGHT, buff=0.5) \
            .to_edge(RIGHT) \
            .shift(LEFT * 0.7)
        print(middle_index, NUMBERS[0:middle_index], NUMBERS[middle_index:])
        print(left_tex_objects, right_tex_objects)
        self.show_numbers(left_tex_objects)
        self.show_numbers(right_tex_objects)


    def make_number_tex(self, number: int) -> MathTex:
        return MathTex(f"{number}", substrings_to_isolate=[f"{number}"])
    
    def show_numbers(self, number_tex_objects: list[MathTex]):
        for tex in number_tex_objects:
            self.play(Write(tex, run_time=0.2))

        self.wait()
