from manim import *

class DrawFunction(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 0.5,
            }
        )
        # create a function
        func_graph = plane.plot(lambda x: x**2, 
                                    color=RED,
                                    x_range=[-2, 2]
                                    )
        # create a dot
        dot = Dot().move_to(plane.c2p(-4, 0 ))

        # show animation
        self.add(plane, func_graph, dot)
        self.wait(1)
        self.play(dot.animate.move_to(plane.c2p(4, 0)), run_time=3)
        self.wait(1)


        self.play(FadeOut(dot))
        self.wait(1)



