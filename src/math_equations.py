from manim import *
import math
import numpy as np
from utils import * 

# Electric Circuit Simulator
class MathEquations(Scene):
    def construct(self):
        eq1 = MathTex(r"V_{T}=V_{L} + V_{R} + V_{C}")
        eq2 = MathTex(r"0=V_{L} + V_{R} + V_{C}")
        eq3 = MathTex(r"0=\frac{d^2 Q}{d t^2}L + \frac{d Q}{d t} R + \frac{Q}{C}")
        eq4 = MathTex(r"0=\frac{d I}{d t}L + I R + \frac{1}{C}\int I d t")
        eq5 = MathTex(r"0=\frac{d I}{d t}L_{o}(1+m\sin \theta ) + I R + \frac{1}{C}\int I d t")
        eq6 = MathTex(r"0=\frac{d I}{d t}(L_{o}+L_{o}m\sin \theta ) + I R + \frac{1}{C}\int I d t")
        eq7 = MathTex(r"0=\frac{d I}{d t}(L_{o}+L_{o}m\sin (2\pi f_{p}) ) + I R + \frac{1}{C}\int I d t")
        eq8 = MathTex(r"0=\frac{d I}{d t}(L_{o}+L_{o}m\sin (\omega _{p}) ) + I R + \frac{1}{C}\int I d t")
        resonant_freq_eq1 = MathTex(r"\omega_{res} =\frac{1}{\sqrt{LC}}")
        resonant_freq_eq2 = MathTex(r"\omega^2 =\frac{1}{LC}")
        parametric_freq_eq1 = MathTex(r"\omega_{par} = 2\cdot \omega_{res}")

        equations = VGroup(eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8,
                          resonant_freq_eq1,resonant_freq_eq2,parametric_freq_eq1).arrange(DOWN).scale(0.5)
        self.play(Write(equations), runtime=3)
