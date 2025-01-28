from manim import *
from default_value import *

class Intro2Animation(Scene):
    def construct(self):
        self.camera.background_color = GRAY_E
        # Display Gremo icon
        gremo_icon = ImageMobject("assets/gremo_icon.png")
        gremo_icon \
            .scale(0.4) \
            .shift(LEFT * 3)
            
        gremo_text = Text("Gremo", font_size=DESCRIPTION_TEXT_SIZE)
        gremo_text \
            .next_to(gremo_icon, DOWN)
        
        descripion = Text("用於記錄在校成績，實時計算輸入成績、\n可自訂出現科目、加權分等\n目前僅支援iOS", font_size=DESCRIPTION_TEXT_SIZE)
        descripion \
            .set_color(GRAY_B) \
            .next_to(gremo_icon, RIGHT, buff=0.6)
        
        description2 = Text("全程由我自主開發，有興趣的話可以去\nAppStore下載來玩玩，在GitHub上也有。\n但畢竟是我第一個專案，寫的有點醜，還請小力噴", font_size=DESCRIPTION_TEXT_SIZE - 5)
        description2 \
            .set_color(GRAY) \
            .next_to(descripion, DOWN) \
            .shift(RIGHT * 0.3) \
            
        self.play(FadeIn(gremo_icon, gremo_text, descripion, description2))
        self.wait(3)
        self.play(FadeOut(gremo_icon, gremo_text, descripion, description2))

        # Display lot of defination of recurrence relation
        def1 = ImageMobject("assets/recurrence_relation_defination.png") \
            .scale(0.25) \
            
        def2 = ImageMobject("assets/recurrence_relation_solution.jpeg")
        text = Text("資料來源：網路", font_size=DESCRIPTION_TEXT_SIZE-10)
        text \
            .to_corner(DR) \
            .set_color(GRAY)
        
        def3 = ImageMobject("assets/recurrence_relation_topic.jpeg")
        def4 = ImageMobject("assets/recurrence_relation_solution2.jpeg") 
        def4 \
            .scale(1.8)

        self.play(FadeIn(def1))
        self.wait()
        self.play(FadeOut(def1))
        self.play(FadeIn(def2, text))
        self.wait()
        self.play(FadeOut(def2))
        self.play(FadeIn(def3))
        self.wait()
        self.play(FadeOut(def3))
        self.play(FadeIn(def4))
        self.wait()
