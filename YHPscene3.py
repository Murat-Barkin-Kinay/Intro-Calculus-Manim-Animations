from manim import *

class RiemannSums(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 9, 1], y_range=[0, 7, 1], x_length=7, y_length=5,
                    axis_config={"include_tip": True, "numbers_to_exclude": [0]}).add_coordinates().shift(2 * LEFT)
        axis_labels = axes.get_axis_labels(x_label="t", y_label="v(t)")
        graph = axes.plot(lambda x: (x - 1) * (x - 4) * (x - 6) * 0.1 + 3, x_range=[0, 7.8])
        dx_list = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
        rectangles = VGroup(
            *[
                axes.get_riemann_rectangles(
                    graph = graph,
                    x_range = [0, 7],
                    stroke_width= 0.1,
                    dx = dx,
                    input_sample_type= "center"
                )
                for dx in dx_list
            ]
        )
        first_area = axes.get_riemann_rectangles(
                    graph = graph,
                    x_range = [0, 6],
                    stroke_width= 0.1,
                    dx = 1,
                    input_sample_type= "center"
                )
        areay = axes.get_riemann_rectangles(
            graph = graph,
            x_range = [0, 7],
            stroke_width= 0.1,
            dx = 1,
            color = YELLOW,
            input_sample_type= "center"
        )
        first_area.z_index = 1
        area = axes.get_area(graph = graph, opacity = 1, x_range = [0, 7])
        areay2 = axes.get_area(graph=graph, color = YELLOW, opacity = 1, x_range=[6.9, 7.2])
        area.z_index = 3
        areay2.z_index = 2

        label1 = MathTex("{\\Delta}t").shift(3.3*DOWN).shift(0.45*LEFT)
        arrow = Arrow(start = RIGHT, end = LEFT).shift(1*DOWN).shift(0.3*RIGHT)
        label2 = MathTex("{\\Delta}s").shift(1*DOWN).shift(1.85 * RIGHT)
        areay.z_index = 0
        arrow2 = arrow.shift(0.45*RIGHT)
        label5 = MathTex("dt").shift(3.3*DOWN)
        label6 = MathTex("ds").shift(1*DOWN).shift(1.95*RIGHT)


        label3 = MathTex("{\\Delta}s \\approx {\\Sigma}v(t){\\cdot}{\\Delta}t}").shift(4*RIGHT)
        label4 = MathTex("{\\Delta}s = \\int_{0}^{t}v(t)\\,dt\\").shift(4*RIGHT)


        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Create(graph))

        self.play(Create(first_area))
        self.wait(1)
        self.play(Create(areay))
        self.wait(0.5)
        self.play(Create(label1), Create(arrow), Create(label2))
        self.wait(5)
        self.play(Create(label3))
        self.remove(label1, arrow, label2)
        self.play(Transform(first_area, rectangles[0]))
        self.remove(areay)
        self.wait(2)
        for i in range(1, len(dx_list)) :
            new_area = rectangles[i]
            self.play(Transform(first_area, new_area, run_time = 1.5))
            self.wait(1.5)
        self.play(ReplacementTransform(first_area, area), ReplacementTransform(label3, label4))
        self.wait(2)
        self.play(Create(areay2), run_time = 1.5)
        self.wait(0.5)
        self.play(Create(label5), Create(arrow2), Create(label6))
        self.wait(5)

