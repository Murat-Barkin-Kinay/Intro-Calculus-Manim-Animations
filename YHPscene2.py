import numpy as np
from manim import *

class SlopePosition(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 9, 1], y_range=[0, 7, 1], x_length=7, y_length=5,
                    axis_config={"include_tip": True, "numbers_to_exclude": [0]}).add_coordinates().shift(2*LEFT)
        axis_labels = axes.get_axis_labels(x_label="t", y_label="s(t)")
        graph = axes.plot(lambda x: (x-1)*(x-4)*(x-6)*0.1 + 3, x_range=[0, 7.8])
        x = ValueTracker(5.5)
        dx = ValueTracker(2)
        secant = always_redraw(
            lambda: axes.get_secant_slope_group(
                x = x.get_value(),
                graph = graph,
                dx = dx.get_value(),
                dx_line_color = YELLOW,
                dy_line_color = ORANGE,
                dx_label = "{\\Delta}t",
                dy_label = "{\\Delta}s",
                secant_line_color = GREEN,
                secant_line_length = 4
            )
        )
        doti = always_redraw(
            lambda: Dot().scale(0.7).move_to(axes.c2p(x.get_value(), graph.underlying_function(x.get_value())))
        )
        dotf = always_redraw(
            lambda: Dot().scale(0.7).move_to(axes.c2p(x.get_value() + dx.get_value(), graph.underlying_function(x.get_value() + dx.get_value())))
        )
        v1 = VGroup(secant, doti, dotf)
        label_1 =  always_redraw(
            lambda: MathTex("\\frac{{\\Delta}s}{{\\Delta}t} = ", ((graph.underlying_function(x.get_value() + dx.get_value()) - graph.underlying_function(x.get_value()))/(dx.get_value())).round(3)).shift(4*RIGHT)
        )
        label_2 = always_redraw(
            lambda: MathTex("\\frac{ds}{dt}(", x.get_value().round(3), ") = ", ((graph.underlying_function(
                x.get_value() + dx.get_value()) - graph.underlying_function(x.get_value())) / (dx.get_value())).round(
                3)).shift(4 * RIGHT)
        )

        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Create(graph))
        self.play(Create(v1))
        self.add(label_1)
        self.play(dx.animate.set_value(1.5), run_time = 2.5)
        self.wait(2)
        self.play(dx.animate.set_value(1), run_time = 2.5)
        self.wait(2)
        self.play(dx.animate.set_value(0.001), ReplacementTransform(label_1, label_2), run_time = 2.5)
        self.wait(2)
        self.play(x.animate.set_value(1), run_time = 4)

