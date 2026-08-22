from manim import *

class logo(Scene):
    def construct(self):
        logo=SVGMobject("../Resources/Images/logo.svg")
        self.play(Write(logo))
        self.wait(4)


