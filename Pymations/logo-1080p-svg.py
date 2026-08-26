from manim import *

class logo(Scene):
    def construct(self):
        logo = SVGMobject("~/Narayana-News/Resources/Images/logo.svg")
        text = Text("Narayana Public School", font_size=44)
        text.next_to(logo, DOWN)
        self.play(
            AnimationGroup(
                Write(logo),
                Write(text),
                lag_ratio=0
                        )
            )
        self.wait(4)


        #self.play(Write(text))
        #self.play(Write(logo))
        #self.wait(4)


