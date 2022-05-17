from manim import *
import math
import numpy as np
from math_equations import * 

class OscilatorsMath(Scene):
    def construct(self):

        slide_title = Text("Simple Harmonic Oscillators", font_size=48).to_edge(UP, buff=0.5).set_color(ORANGE)
        spring_diagram = SVGMobject("src/assets/spring.svg").scale(2.0)
        pendulum_diagram = SVGMobject("src/assets/pendulum.svg").scale(2.0)

        # Spring Diagram
        self.add(slide_title)
        self.wait()
        self.play(Write(spring_title))
        self.wait()
        self.play(Write(spring_eqs[8].next_to(spring_title, DOWN)))
        self.wait()
        self.play(FadeIn(spring_diagram.next_to(spring_eqs[8], DOWN, buff=0.5)))
        self.wait()
        x = spring_eqs[8][7].copy()
        self.play(x.animate.move_to(spring_diagram).shift(1.4*RIGHT))
        self.wait()
        m = spring_eqs[8][0].copy()
        self.play(m.animate.move_to(spring_diagram).shift(1.3*LEFT))
        self.wait()
        k = spring_eqs[8][6].copy()
        self.play(k.animate.move_to(spring_diagram).shift(1.4*DOWN+0.8*LEFT))
        self.wait()
        self.play(FadeOut(x,m,k))
        self.play(FadeOut(spring_eqs[8], spring_diagram))
        self.wait()

        # Spring Equations
        self.play(Write(spring_eqs[0].next_to(spring_title, DOWN), runtime=2))
        self.wait()
        self.play(TransformMatchingTex(spring_eqs[0].copy(), spring_eqs[1].next_to(spring_eqs[0], DOWN, buff=0.5), path_arc=90*DEGREES))
        self.wait()
        self.play(TransformMatchingTex(spring_eqs[1].copy(), spring_eqs[2].next_to(spring_eqs[1], DOWN, buff=0.5)))
        self.wait()
        self.remove(spring_eqs[0],spring_eqs[1])
        self.wait()
        self.play(spring_eqs[2].animate.shift(2*LEFT))
        self.wait()
        self.play(Write(spring_eqs[3].next_to(spring_eqs[2], RIGHT, buff=1).shift(UP)))
        self.wait()
        self.play(Write(spring_eqs[4].next_to(spring_eqs[3], DOWN, buff=0.8)))
        self.wait()
        self.play(spring_eqs[4].animate.become(spring_eqs[5]. next_to(spring_eqs[3], DOWN, buff=0.8)))
        self.wait()
        self.play(spring_eqs[2][0].animate.become(spring_eqs[3][1].copy()).move_to(spring_eqs[2][0]))
        self.wait()
        self.play(spring_eqs[2][2].animate.become(spring_eqs[5][0]).move_to(spring_eqs[2][2]))
        self.wait()
        self.play(ReplacementTransform(spring_eqs[2],spring_eqs[6].scale(1.5)), FadeOut(spring_eqs[3],spring_eqs[4],spring_eqs[5]))
        self.wait()
        self.play(TransformMatchingTex(spring_eqs[6].copy(), spring_eqs[7].scale(1.5).next_to(spring_eqs[6], DOWN, buff=0.5), path_arc=90*DEGREES))
        self.wait()
        self.play(FadeOut(spring_eqs[6]), spring_eqs[7].animate.shift(UP))
        self.wait()
        self.play(FadeOut(spring_eqs[7], spring_title))
        self.wait()

        # Penulum Diagram
        self.play(Write(pendulum_title))
        self.wait()
        self.play(Write(pendulum_eqs[5].next_to(pendulum_title,DOWN)))
        self.wait()
        self.play(FadeIn(pendulum_diagram.next_to(pendulum_eqs[5],DOWN,buff=0.5)))
        self.wait()
        theta = pendulum_eqs[5][9].copy()
        self.play(theta.animate.move_to(pendulum_diagram).shift(1.2*UP+0.2*RIGHT))
        self.wait()
        l = pendulum_eqs[5][0].copy()
        self.play(l.animate.move_to(pendulum_diagram).shift(0.3*LEFT+0.2*DOWN))
        self.wait()
        g = pendulum_eqs[5][7].copy()
        self.play(g.animate.move_to(pendulum_diagram).shift(2*RIGHT+UP))
        self.wait()
        self.play(FadeOut(theta,l,g))
        self.play(FadeOut(pendulum_diagram,pendulum_eqs[5]))
        self.wait()
        
        # Pendulum Equations
        self.play(Write(pendulum_eqs[0].to_edge(ORIGIN)))
        self.wait()
        self.play(pendulum_eqs[0].animate.shift(2*LEFT+0.8*DOWN))
        self.wait()
        self.play(Write(pendulum_eqs[1].next_to(pendulum_eqs[0], RIGHT, buff=1).shift(UP)))
        self.wait()
        self.play(Write(pendulum_eqs[2].next_to(pendulum_eqs[1], DOWN, buff=0.8)))
        self.wait()
        self.play(pendulum_eqs[2].animate.become(pendulum_eqs[3].next_to(pendulum_eqs[1], DOWN, buff=0.8)))
        self.wait()
        self.play(pendulum_eqs[0][0].animate.become(pendulum_eqs[1][2].copy().move_to(pendulum_eqs[0][0])))
        self.wait()
        self.play(pendulum_eqs[0][3].animate.become(pendulum_eqs[3][0].move_to(pendulum_eqs[0][3])))
        self.wait()
        self.play(ReplacementTransform(pendulum_eqs[0], pendulum_eqs[4].scale(1.5)), FadeOut(pendulum_eqs[1],pendulum_eqs[2],pendulum_eqs[3]))
        self.wait()
        self.play(FadeIn(spring_eqs[7].next_to(pendulum_eqs[4], DOWN, buff=0.8)))
        self.wait()