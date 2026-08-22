from manim import *

class logo(Scene):
    def construct(self):
        logo=ImageMobject("../Resources/Images/logo-nps.png")
        self.play(FadeIn(logo))
        self.wait(4)


