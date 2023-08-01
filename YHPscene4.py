from manim import *

class FTC(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 9, 1], y_range=[0, 7, 1], x_length=7, y_length=5,
                    axis_config={"include_tip": True, "numbers_to_exclude": [0]}).shift(2 * LEFT)
        axis_labels = axes.get_axis_labels(x_label="t", y_label="v(t)")
        graph = axes.plot(lambda x: (x - 1) * (x - 4) * (x - 6) * 0.1 + 3, x_range=[0, 7.8])
        T = ValueTracker(7)
        area = always_redraw(
            lambda: axes.get_area(graph = graph, opacity = 1, x_range = [0, T.get_value()])
        )
        t_label1 = always_redraw(
            lambda: axes.get_T_label(x_val = T.get_value(), graph=graph, label=MathTex("T"))
        )
        label1 = MathTex("A(T) = s(T) - s(0) = \\int_{0}^{T}v(t)\\,dt\\").shift(3.5 * RIGHT).shift(2*UP).scale(0.65)
        label2 = Text("{").rotate(PI/2).shift(2.7 * DOWN).scale(0.3).shift(0.7 * LEFT)
        label3 = MathTex("dT").shift(3 * DOWN).shift(0.7 * LEFT)
        label4 = MathTex("A(T)").shift(1.7*DOWN).shift(4.2*LEFT)
        increment = axes.get_riemann_rectangles(
                    graph = graph,
                    x_range = [6, 6.1],
                    stroke_width= 0.1,
                    dx = 0.2,
                    color = YELLOW,
                    input_sample_type= "left"
        )
        brace1 = BraceBetweenPoints([-0.7,-0.4,0], [-0.7,-2.5,0])
        label5 = MathTex("v(T)").shift(1.75*LEFT).shift(1.45 * DOWN)
        arrow = Arrow(start = 0.5 * RIGHT, end = 1 * LEFT).shift(1 * DOWN)
        label6 = MathTex("ds").shift(1 * DOWN).shift(0.7*RIGHT)
        label7 = MathTex("ds = v(T) \\cdot dT").shift(3.5 * RIGHT)
        label8 = MathTex("\\frac{ds}{dT} = v(T)").shift(3.5 * RIGHT)

        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Create(graph))
        self.play(Create(area), Create(label4))
        self.play(Create(t_label1))
        self.play(Create(label1))
        self.wait(2)
        self.play(T.animate.set_value(3))
        self.wait(2)
        self.play(T.animate.set_value(6))
        self.wait(4)
        self.remove(t_label1, label4)
        self.play(Create(increment))
        self.play(Create(label2), Create(label3))
        self.wait(0.5)
        self.play(Create(brace1), Create(label5))
        self.wait(0.5)
        self.play(Create(arrow), Create(label6))
        self.wait(1.5)
        self.play(Create(label7))
        self.wait(6)
        self.play(Transform(label7, label8))
        self.wait(8)