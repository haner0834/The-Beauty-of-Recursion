from manim import *
from default_value import *

class GCDCodeShowcase(Scene):
    def construct(self):
        self.camera.background_color = GRAY_E

        gcd_code_iterative = ImageMobject("assets/gcd_iterative.png")
        gcd_code_recursive = ImageMobject("assets/gcd_recursive.png")
        gcd_code_iterative \
            .scale(1.6) \
            .to_edge(LEFT, buff=1) \
            
        gcd_code_recursive \
            .scale(1.6) \
            .to_edge(RIGHT, buff=1) \
        
        description_iterative = Text("迴圈解", font_size=DESCRIPTION_TEXT_SIZE-5)
        description_iterative \
            .next_to(gcd_code_iterative, DOWN, buff=0.4) \
            .set_color(GRAY_B) \
            
        description_recursive = Text("遞迴解", font_size=DESCRIPTION_TEXT_SIZE-5)
        description_recursive \
            .next_to(gcd_code_recursive, DOWN, buff=0.4) \
            .set_color(GRAY_B)
                
        self.play(FadeIn(gcd_code_iterative, gcd_code_recursive, description_iterative, description_recursive))
        self.wait()