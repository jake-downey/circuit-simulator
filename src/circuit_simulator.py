from manim import *
import math
import numpy as np
from utils import * 

# Electric Circuit Simulator
class RLC(Scene):
    r = ValueTracker(0)
    l = ValueTracker(0.2)
    C = ValueTracker(0.0001)

    EMF = 5
    I = 0
    Q = C.get_value() * EMF

    dt = .001
    time = ValueTracker(1)

    # Returns the Voltage and Current at frame
    def get_voltage_and_current(self):
        alpha = (self.Q / (self.l.get_value() * self.C.get_value())) - (self.I * self.r.get_value() / self.l.get_value())

        self.I = self.I + (alpha * self.dt)
        self.Q = self.Q - (self.I * self.dt)

        Vc = self.Q / self.C.get_value()
        return Vc, self.I

    # Generates the plot Volatage by Time
    def generate_voltage_plot(self, axes):
        self.Q = self.C.get_value() * self.EMF
        self.I = 0
        return axes.plot(lambda t: self.get_voltage_and_current()[0], [0, self.time.get_value(), self.dt]).set_color(YELLOW)

    # Generates the plot Current by Time
    def generate_current_plot(self, axes):
        self.Q = self.C.get_value() * self.EMF
        self.I = 0
        return axes.plot(lambda t: self.get_voltage_and_current()[1], [0, self.time.get_value(), self.dt]).set_color(BLUE)

    # Constructs the Scene
    def construct(self):
        axes = Axes(
                x_range=[0, self.time.get_value(), .1],
                y_range=[-6, 6, 1],
                x_length=10,
                axis_config={"color": WHITE},
                x_axis_config={"numbers_to_include": np.arange(0, self.time.get_value().round(1), .1)},
                y_axis_config={"numbers_to_include": np.arange(-6.01, 6.01, 1)},        
                tips=False,
            )
        axes.add_updater(lambda mob: mob.become(Axes(
                x_range=[0, self.time.get_value(), .1],
                y_range=[-6, 6, 1],
                x_length=10,
                axis_config={"color": WHITE},
                x_axis_config={"numbers_to_include": np.arange(0, self.time.get_value().round(1), .1)},
                y_axis_config={"numbers_to_include": np.arange(-6.01, 6.01, 1)},          
                tips=False,
            )))
        labels = axes.get_axis_labels('t', 'V,A')

        x_axis = axes.get_x_axis()
        x_axis.add_updater(lambda mob: mob.set(x_range = [0, self.time.get_value(), .1]))

        # generate plot of Voltage and Current and adds updater to be redrawn every frame
        voltage = self.generate_voltage_plot(axes)
        current = self.generate_current_plot(axes)
        voltage.add_updater(lambda mob: mob.become(self.generate_voltage_plot(axes)))
        current.add_updater(lambda mob: mob.become(self.generate_current_plot(axes)))

        # Create Resistance text
        r_text, r_number, r_units = r_label = VGroup(
            Text("R = ", font_size=36).set_color(RED),
            DecimalNumber(
                self.r.get_value(),
                num_decimal_places = 2,
                include_sign = True
            ),
            Tex("$\Omega$", font_size=44).set_color(WHITE)
        )
        r_label.arrange(RIGHT).next_to(axes, DOWN)
        
        # Create Inductance text
        l_text, l_number, l_units = l_label = VGroup(
            Text("L = ", font_size=36).set_color(GREEN),
            DecimalNumber(
                self.l.get_value(),
                num_decimal_places = 6
            ),
            Text("H", font_size=28, slant = ITALIC).set_color(WHITE)
        )
        l_label.arrange(RIGHT).next_to(r_label, LEFT)
        
        # Create Capacitance text
        c_text, c_number, c_units = c_label = VGroup(
            Text("C = ", font_size=36).set_color(PURPLE),
            DecimalNumber(
                self.C.get_value(),
                num_decimal_places = 6
            ),
            Text("F", font_size=28, slant = ITALIC).set_color(WHITE)
        )
        c_label.arrange(RIGHT).next_to(r_label, RIGHT)

        # Create Frequency Text
        frequency_text = Text("Frequency = ", font_size=36).set_color(ORANGE)
        frequency_number = DecimalNumber(
                    get_resonant_frequency(self.l, self.C),
                    num_decimal_places = 2
                )
        frequency_units = Text("Hz", font_size=28, slant = ITALIC)
        frequency_label = VGroup(frequency_text, frequency_number, frequency_units)
        frequency_label.arrange(RIGHT).next_to(axes, UP)

        # Create Voltage and Current Text
        voltage_label, current_label = va_label = VGroup(
            Text('VOLTAGE (V)', font_size=28).set_color(YELLOW),
            Text('CURRENT (I)', font_size=28).set_color(BLUE)
        ).arrange(RIGHT).next_to(r_label, UP)

        # add updaters to decimal numbers
        r_number.add_updater(lambda m: m.set_value(self.r.get_value()))
        l_number.add_updater(lambda m: m.set_value(self.l.get_value()))
        c_number.add_updater(lambda m: m.set_value(self.C.get_value()))
        frequency_number.add_updater(lambda m: m.set_value(get_resonant_frequency(self.l, self.C)))

        # add objects and animations
        self.add(r_label, l_label, c_label, frequency_label, va_label)
        self.add(axes, labels, voltage, current)

        # play animations
        self.wait()
        self.play(self.r.animate.set_value(6), run_time = 3)
        self.play(self.l.animate.set_value(0.5), run_time = 2)
        self.play(self.C.animate.set_value(0.002), run_time = 2)

        self.play(self.l.animate.set_value(0.2), run_time = 1)
        self.play(self.C.animate.set_value(0.0001), run_time = 1)
        self.play(self.r.animate.set_value(0), run_time = 2)

        self.play(self.time.animate.set_value(2))
        self.wait()
        self.play(self.time.animate.set_value(.5), run_time = 2)
       
        self.play(Indicate(voltage_label))
        self.play(Indicate(current_label))
        self.play(Indicate(r_label))
        self.play(Indicate(l_label))
        self.play(Indicate(c_label))
        self.wait()

        # graph = VGroup(axes, labels, r_label, l_label, c_label, frequency_label)
        # self.play(graph.animate.scale(.6).to_edge(DL))




