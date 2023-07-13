from manim import *
# do not import matplotlib
# the class reflect reflects a line given by a function f(x)
# when it is reflected in the when it reach the graph of another function g(x)
# the reflected line is a perpendicular line to the tangent line to g(x) at the point of intersection

class Reflect(Scene):
    def construct(self):
        # prepare the axes
        axes = (
            Axes(
                x_range=[0, 10],
                x_length=8,
                y_range=[0, 10],                
                y_length=5,
                axis_config={"include_numbers": True, "include_tip": False},
            ).to_edge(DL)
            .set_color(WHITE)
        )

        f_x = axis.plot(
            lambda x: x**2,
            x_range=[0,10], 
            color=BLUE
        )

        self.play(Create(axes))  
        self.play(Create(f_x))
        
        self.wait()

        
