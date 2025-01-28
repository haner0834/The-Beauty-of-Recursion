from manim import *

NUMBERS = [34, 57, 23, 18, 43, 37, 25, 41, 50, 28]
SORTED_NUMBERS = sorted(NUMBERS)

class SelectionSortAnimation(Scene):
    number_tex_objects: list[MathTex] = []
    sorted_number_tex_objects: list[MathTex] = []
    run_times = 0
    
    def construct(self):
        self.camera.background_color = GRAY_E
        
        # Initialize texes to show
        for number in NUMBERS:
            self.number_tex_objects.append(self.make_number_tex(number=number))

        for number in SORTED_NUMBERS:
            self.sorted_number_tex_objects.append(self.make_number_tex(number=number))
        
        # Intitialize groups
        group1 = VGroup(*self.number_tex_objects)
        group1 \
            .arrange(RIGHT, buff=0.7) \
            .to_edge(UP) \
            .shift(DOWN * 0.7)
        
        group2 = VGroup(*self.sorted_number_tex_objects)
        group2 \
            .arrange(RIGHT, buff=0.7) \
            .to_edge(ORIGIN) \
            .shift(DOWN * 0.7)

        self.show_numbers()

        self.demostrate_find_min()

        self.play(group1.animate.shift(UP * 0.7)) # IDK why the fuck this works, but well, ok, ok.
        
        self.wait()

    # -----------------------| `construct` end |----------------------- #

    def demostrate_find_min(self):
        first_tex = self.number_tex_objects[0]

        check_block = CheckOperator(
            height=first_tex.get_height() + 0.35,
            width=first_tex.get_width() + 0.35
        )
        check_block.move_to(first_tex.get_center())
        
        min_operator = MinOperator(width=first_tex.get_width() + 0.2)
        min_operator.move_to(first_tex.get_bottom() + DOWN*0.6)

        text = Text("0").set_color(BLUE_B)
        self.play(Write(text))
        
        self.play(
            Create(min_operator), FadeIn(check_block)
        )

        numbers = NUMBERS.copy()
        tex_objects = self.number_tex_objects.copy()
        for i in range(len(NUMBERS)):
            first_tex = tex_objects[0]
            self.play(
                min_operator.animate.move_to(first_tex.get_bottom() + DOWN*0.6)
            )

            self.iterate_animation(
                current_item=i, text=text, numbers=numbers, tex_objects=tex_objects,
                check_block=check_block, min_operator=min_operator
            )

        self.wait()
        self.play(
            FadeOut(check_block), FadeOut(min_operator)
        )

        self.wait(2)

    # -----------------------| `demostrate_find_min` end |----------------------- #

    def iterate_animation(self, current_item: int, text: Text, numbers: list[int],
                          tex_objects: list[MathTex], check_block: Mobject, 
                          min_operator: Mobject):
        number_tex_to_remove: Mobject = tex_objects[0]
        min_number = numbers[0]

        for i, tex in enumerate(tex_objects):
            self.run_times += 1
            self.play(check_block.animate.move_to(
                tex.get_center()), 
                Transform(text, Text(f"{self.run_times}").set_color(BLUE_B)),
                run_time=0.5,
            )

            number = numbers[i]
            if min_number > number:
                min_number = number
                self.play(
                    min_operator.animate.move_to(tex.get_bottom() + DOWN*0.6),
                    run_time=0.5
                )
                number_tex_to_remove = tex

        if number_tex_to_remove is not None:
            tex_objects.remove(number_tex_to_remove)
            numbers.remove(min_number)
            self.play(
                Transform(number_tex_to_remove, self.sorted_number_tex_objects[current_item])
            )

    def make_number_tex(self, number: int) -> MathTex:
        return MathTex(f"{number}", substrings_to_isolate=[f"{number}"])
    
    def show_numbers(self):
        for tex in self.number_tex_objects:
            self.play(Write(tex, run_time=0.2))

        self.wait()

# -----------------------| `MergeSortAnimation` end |----------------------- #

class CheckOperator(Mobject):
    def __init__(self, coverOn: Mobject, **kwargs):
        super().__init__(**kwargs)
        rectangle = RoundedRectangle(
            corner_radius=0.16, color=GREEN_C, 
            height=coverOn.get_height() + 0.35,
            width=coverOn.get_width() + 0.35
        )
        rectangle \
            .move_to(coverOn.get_center()) \
            .set_fill(opacity=0) \
            .set_stroke(width=7)
        
        self.add(rectangle)

    def __init__(self, height: float, width: float, **kwargs):
        super().__init__(**kwargs)
        rectangle = RoundedRectangle(
            corner_radius=0.16, color=GREEN_C, 
            height=height,
            width=width
        )
        rectangle \
            .set_fill(opacity=0) \
            .set_stroke(width=7)
        
        self.add(rectangle)

class MinOperator(VGroup):
    def __init__(self, width: float):
        super().__init__()
        # Operator
        check_block = RoundedRectangle(
            color=GOLD_B, height=0.05, 
            width=width,
            corner_radius=0.025
        )
        check_block \
            .set_fill(GOLD_B, opacity=1)
        
        # "Min" text
        text = Text("min", font_size=25)
        text \
            .set_color(GOLD_B) \
        
        self.add(check_block, text)
        self.arrange(DOWN)

class Grid(VGroup):
    def __init__(self, rows: int, cols: int, spacing: float=0.5, *vmobjects, **kwargs):
        super().__init__(*vmobjects, **kwargs)
        grid = self.create_grid(rows=rows, cols=cols, spacing=spacing)
        self.add(grid)

    def create_grid(rows, cols, spacing=0.5) -> VGroup:
        grid = VGroup()
        for _ in range(rows):
            row = VGroup(*[Square() for _ in range(cols)])
            row.arrange(RIGHT, buff=spacing)
            grid.add(row)
        grid.arrange(DOWN, buff=spacing)
        return grid