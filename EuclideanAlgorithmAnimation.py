from manim import *
from default_value import *
from typing import Optional

FONT_SIZE = 30

class EuclideanAlgorithmAnimation(Scene):
    def construct(self):
        self.camera.background_color = GRAY_E

        title = Text("輾轉相除法 Euclidean Algorithm", font_size=TITLE_TEXT_FONT_SIZE)
        title \
            .to_edge(UP, buff=0.5)
        
        line = FullScreenWidthLine(buff=1)
        line.next_to(title, DOWN, buff=0.3)
        self.add(title, line)
        # Idea from Wiki Pedia, difference is Wiki uses substruction, I use remainder
        # here I choose (8, 18), where the answer is 2
        self.gcd_animation(8, 18)

        self.wait()


    def gcd_animation(self, n: int, m: int):
        ORIGIN_N = n
        ORIGIN_M = m
        def make_n_text(n: int) -> Text:
            text_content = f"n: {n}"
            text = Text(text_content, font_size=FONT_SIZE) \
                .to_edge(LEFT, buff=0.8) \
                .shift(UP * 0.5)
            return text

        def make_m_text(m: int) -> Text:
            text_content = f"m: {m}"
            text = Text(text_content, font_size=FONT_SIZE) \
                .to_edge(LEFT, buff=0.8) \
                .shift(DOWN * 0.5)
            return text
        
        # Create m and n objects, and arrange it horizontally
        n_squares = [BoarderSquare(side_length=0.4, fill_color=GREEN_B) for _ in range(n)]
        m_squares = [BoarderSquare(side_length=0.4, fill_color=BLUE_B) for _ in range(m)]

        n_vgroup = VGroup(*n_squares) 
        n_vgroup \
            .arrange(RIGHT, buff=0.2) \
            .to_edge(LEFT, buff=2) \
            .shift(UP * 0.5)
        
        m_vgroup = VGroup(*m_squares)
        m_vgroup \
            .arrange(RIGHT, buff=0.2) \
            .to_edge(LEFT, buff=2) \
            .shift(DOWN * 0.5)
        
        n_text = Text(f"n: {n}", font_size=FONT_SIZE)
        n_text \
            .to_edge(LEFT, buff=0.8) \
            .shift(UP * 0.5)
        
        m_text = Text(f"m: {m}", font_size=FONT_SIZE)
        m_text \
            .to_edge(LEFT, buff=0.8) \
            .shift(DOWN * 0.5)
            
        self.play(
            list(map(lambda x: FadeIn(x), n_squares)),
            list(map(lambda x: FadeIn(x), m_squares)),
            FadeIn(n_text), FadeIn(m_text)
        )
        self.wait()

        i = 0 # counter, for distinguishing whether to move up or down
        while True: # FUCKING PLACE, IDK WTH WAS GOING ON EITHER, but it worked
            m_vgroup_objects_to_remove = m_squares[(m%n):]
            n_vgroup_objects_to_remove = n_squares[(n%m):]

            if i == 0:
                guide_block = RoundedRectangle(0.25, width=config.frame_width-1, height=0.8)
                guide_block \
                    .to_edge(LEFT) \
                    .shift(DOWN * 0.5) \
                    .set_fill(BLUE_B, opacity=0.25) \
                    
                guide_text = Text("取n除以m的餘數", font_size=FONT_SIZE)
                guide_text \
                    .next_to(guide_block, DOWN)
                    
                self.play(FadeIn(guide_block), FadeIn(guide_text))
                self.wait()
                self.play(FadeOut(guide_block), FadeOut(guide_text))
                self.wait()

            if i % 2 == 0 and len(m_vgroup_objects_to_remove) > 0:
                self.play(
                    list(map(lambda x: FadeOut(x), m_vgroup_objects_to_remove)),
                    Transform(m_text, make_m_text(m%n))
                )
            elif len(n_vgroup_objects_to_remove) > 0:
                self.play(
                    list(map(lambda x: FadeOut(x), n_vgroup_objects_to_remove)),
                    Transform(m_text, make_m_text(n%m))
                )

            if i == 0:
                guide_block =  RoundedRectangle(0.25, width=config.frame_width-1, height=1.8)
                guide_block \
                    .to_edge(LEFT) \
                    .set_fill(BLUE_B, opacity=0.25) \
                
                guide_text = Text("交換m, n", font_size=FONT_SIZE)
                guide_text \
                    .next_to(guide_block, UP)

                self.play(FadeIn(guide_block), FadeIn(guide_text))
                self.wait()
                self.play(FadeOut(guide_block), FadeOut(guide_text))
                self.wait()

            
            if i % 2 == 0:
                for object in m_vgroup_objects_to_remove:
                    m_vgroup.remove(object)
                    m_squares.remove(object)
            else:
                for object in n_vgroup_objects_to_remove:
                    n_vgroup.remove(object)
                    n_squares.remove(object)

            self.play(
                m_vgroup.animate.shift(UP if i % 2 == 0 else DOWN),
                n_vgroup.animate.shift(DOWN if i % 2 == 0 else UP),
                Transform(n_text, make_n_text(m%n if i % 2 == 0 else n%m)),
                Transform(m_text, make_m_text(len(n_squares) if i % 2 == 0 else len(m_squares))),
            )

            check_block = RoundedRectangle(0.25, width=config.frame_width-1, height=0.8)
            is_n_zero = (len(n_squares if i % 2 == 1 else m_squares)) == 0
            check_block \
                .to_edge(LEFT) \
                .shift(UP * 0.5) \
                .set_fill(GREEN_B if is_n_zero else RED_B, opacity=0.3) \
            
            animation_objects = [check_block]

            if i == 0:
                guide_text = Text("檢查n是否為0", font_size=FONT_SIZE)
                guide_text.next_to(check_block, UP)
                animation_objects.append(guide_text)
            elif is_n_zero:
                guide_text = Text("n = 0, 最大公因數=m", font_size=FONT_SIZE)
                guide_text.next_to(check_block, UP)
                animation_objects.append(guide_text)

            self.play(list(map(lambda x: FadeIn(x), animation_objects)))
            if i == 0: self.wait(3)
            elif is_n_zero: self.wait()
            self.play(list(map(lambda x: FadeOut(x), animation_objects)))

            self.wait(0.5)

            if m%n == 0:
                gcd = len(n_squares)
                break
            elif n%m == 0:
                gcd = len(m_squares)
                break
            
            # Update state tracing
            i += 1
            n, m = m, m%n

        # After running recurrence animatio, transform "m: 2" to "(8, 18) = 2" and move to center
        self.wait()
        self.play(
            list(map(lambda x: FadeOut(x), m_squares)), FadeOut(n_text),
            list(map(lambda x: FadeOut(x), n_squares)),
        )
        m_squares.clear()

        result = MathTex(f"({ORIGIN_N}, {ORIGIN_M}) = {gcd}", substrings_to_isolate=[f"{ORIGIN_N}", f"{ORIGIN_M}", f"{gcd}"], font_size=60)
        result \
            .set_color_by_tex(f"{ORIGIN_N}", GREEN_B) \
            .set_color_by_tex(f"{ORIGIN_M}", BLUE_B) \
            .set_color_by_tex(f"{gcd}", GOLD_B)
        self.play(Transform(m_text, result), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(m_text))
        

    def recursive_gcd(self, n: int, m: int) -> int:
        if n == 0: return m
        return self.recursive_gcd(m%n, n)
    
    def iterative_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

class FullScreenWidthLine(Line):
    def __init__(self, buff = 0, padding = 0, path_arc = None, **kwargs):
        start = LEFT * config.frame_width / 2
        end = RIGHT * config.frame_width / 2
        super().__init__(start, end, buff, path_arc, **kwargs)

    
class BoarderSquare(Square):
    def __init__(self, side_length = 2, 
                 fill_color: ManimColor = BLACK, 
                 stroke_color: Optional[ManimColor] = None,
                 stroke_width: Optional[float] = None,
                 **kwargs):
        super().__init__(side_length, **kwargs)   
        self.set_fill(fill_color, opacity=1)
        if stroke_width is not None and stroke_color is not None:
            self.set_stroke(color=stroke_color, width=stroke_width)