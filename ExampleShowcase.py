from manim import *
from default_value import *
from shared_object import *

class ExampleShowcase(Scene):
    def construct(self):
        self.camera.background_color = GRAY_E
        
        self.recurrsion_animarion()

        self.quick_sort_image()

        self.wait()

        self.fibonacci_animation()

    def recurrsion_animarion(self):
        vgroup = VGroup()
        rounded_rectangles: list[RoundedRectangle] = []
        for i in range(5):
            rounded_rectangle = RoundedRectangle(0.2, width=1.2, height=0.9)
            color = BLUE_B if i != 4 else RED_B
            rounded_rectangle \
                .set_fill(color, opacity=1) \
                .set_stroke(color=WHITE, width=6) \
            
            rounded_rectangles.append(rounded_rectangle)

        arrows: list[Arrow] = []
        for i in range(4):
            arrow = Arrow(
                        end=rounded_rectangles[i].get_right()-2,
                        start=rounded_rectangles[i+1].get_left()-2,
                        stroke_width=9, max_stroke_width_to_length_ratio=9
                    )
            arrows.append(arrow)

        objects = []
        for i in range(4):
            objects.append(rounded_rectangles[i])
            objects.append(arrows[i])
        objects.append(rounded_rectangles[4])

        vgroup.add(*objects)
        vgroup.arrange(RIGHT)

        descriptions: list[Text] = []
        for i in range(5):
            description = Text(f"Case {i+1}" if i != 4 else "Base case", font_size=DESCRIPTION_TEXT_SIZE)
            description \
                .set_color(GRAY_B) \
                .next_to(rounded_rectangles[i], DOWN, buff=0.4)
            descriptions.append(description)

        for i, object in enumerate(objects):
            if i % 2 == 0:
                self.play(FadeIn(object, descriptions[int(i/2)]))
            else:
                self.play(FadeIn(object))

        self.wait()

        self.play(FadeOut(*objects, *descriptions, vgroup))


    def quick_sort_image(self):
        image = ImageMobject("assets/quick_sort.png")
        image \
            .scale(1.16) \
            .to_edge(UP, buff=0.6) \
        
        description = Text("快速排序 Quicksort", font_size=DESCRIPTION_TEXT_SIZE)
        description \
            .next_to(image, DOWN) \
            .set_color(GRAY)

        self.play(FadeIn(image))
        self.play(Write(description))
        self.wait()
        self.play(FadeOut(image), FadeOut(description))

    def fibonacci_animation(self):
        title = TopTitle("斐波那契數列 Fibonacci Sequence")
        self.play(FadeIn(title))
        fibonacci_tex = MathTex(r"F_0 = 0, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2} \quad \text{for } n \geq 2")
        self.play(Write(fibonacci_tex))
        self.wait()
        self.play(fibonacci_tex.animate.shift(UP))

        fibonacci_general_terms = MathTex(r"F_n = \frac{\phi^n - \psi^n}{\sqrt{5}} \text{ where } \phi = \frac{1 + \sqrt{5}}{2}, \quad \psi = \frac{1 - \sqrt{5}}{2}")
        fibonacci_general_terms.next_to(fibonacci_tex, DOWN)
        self.play(Write(fibonacci_general_terms))
        self.wait()

        self.play(FadeOut(fibonacci_tex), FadeOut(fibonacci_general_terms))
        self.wait()

    def quick_sort_animation(self):
        NUMBERS = [34, 57, 23, 18, 37, 43, 25, 41, 50, 28]
        SORTED_NUMBERS = sorted(NUMBERS)
        FLOORS: list[Floor] = [
            # Use >= to right, < to left
            Floor(groups=[NUMBERS], is_root=True),
            Floor(groups=[[34, 18, 23, 25, 28, 37], [57, 43, 41, 50]]),
            Floor(groups=[[18, 23, 25], [34, 37], [41], [57, 43, 50]]),
            Floor(groups=[[18, 23], [25], [34], [37], [41], [43], [57, 50]]),
            Floor(groups=[[18], [23], [25], [34], [37], [41], [43], [50], [57]]),
        ]
        tex_objects: list[list[list[MathTex]]] = []
        groups: list[list[VGroup]] = []
        vgroup = VGroup()
        for i, floor in enumerate(FLOORS):
            hgroup = VGroup()

            for group in floor.groups:
                texes = list(map(lambda x: self.make_tex(x), group))
                tex_objects.append(texes)
                boarder_vgroup = self.make_boarder_vgroup(*texes)
                hgroup.add(boarder_vgroup)

            hgroup.arrange(RIGHT, buff=0.6)
            if len(groups) <= i: groups.append([])
            groups[i].append(hgroup)
            vgroup.add(hgroup)
        vgroup.arrange(DOWN, buff=0.5)
        
        # self.play(Create(groups[0][0]), run_time=4)
        for i, group in enumerate(groups):
            for each_group in group:
                self.play(Create(each_group), run_time=5)
            self.wait(3 if i == 0 else DEFAULT_WAIT_TIME)

        self.wait()




    def make_boarder_vgroup(self, *mobjects: Mobject) -> VGroup:
        vgroup = VGroup(*mobjects)
        vgroup \
            .arrange(RIGHT, buff=0.6) \
            
        rectangle = RoundedRectangle(
            corner_radius=0.16, color=GREEN_C, 
            height=vgroup.get_height() + 0.35,
            width=vgroup.get_width() + 0.35
        )
        rectangle \
            .move_to(vgroup.get_center()) \
            .set_fill(opacity=0) \
            .set_stroke(width=7)
        
        vgroup.add(rectangle)
        
        return vgroup


    def make_tex(self, n: int) -> Text:
        return MathTex(f"{n}", substrings_to_isolate=[f"{n}"])
    
class Floor: 
    def __init__(self, groups: list[list[int]] = [], is_root: bool = False):
        self.is_root = is_root
        self.groups = groups