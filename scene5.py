from manim import *
from scipy.optimize import fsolve
from sympy import diff, Symbol
from math import atan, tan

class Reflect(Scene):
    def construct(self):
        self.axes = (
            Axes(
                x_range=[-5, 5],
                x_length=10,
                y_range=[-15, 15],                
                y_length=15,
                axis_config={"include_numbers": False, "include_tip": False},
            ).set_color(WHITE)
        )

        f = lambda x: 2 * x + 1
        g = lambda x: 0.5 * x + 1

        intersection_point = self.intersection(f, g)
        x_coord, _ = self.axes.point_to_coords(intersection_point)

        f_graph = self.axes.plot(f, x_range=[-10, x_coord], color=BLUE)
        g_graph = self.axes.plot(g, x_range=[-10, 10], color=YELLOW)

        tangent_line = self.tangent(g, intersection_point)

        reflection_line = self.reflection(f, tangent_line, intersection_point)

        self.play(Create(self.axes))
        self.play(Create(f_graph), Create(g_graph))
        self.play(Create(reflection_line))
        self.wait(5)

    def intersection(self, f, g):
        x_coord = fsolve(lambda x: f(x) - g(x), 0)[0]
        y_coord = f(x_coord)
        return self.axes.coords_to_point(x_coord, y_coord)

    def tangent(self, g, intersection_point):
        x = Symbol('x')
        derivative = diff(g(x), x).subs(x, intersection_point[0])
        tangent = lambda x: derivative * (x - intersection_point[0]) + intersection_point[1]
        return self.axes.plot(tangent, x_range=[0, 10], color=BLUE)

    def reflection(self, f, tangent_line, intersection_point):
        slope_f = (f(1) - f(0)) / (1 - 0)
        slope_tangent = (tangent_line.underlying_function(1) - tangent_line.underlying_function(0)) / (1 - 0)
        angle = atan((slope_tangent - slope_f) / (1 + slope_tangent * slope_f))
        slope_reflection = tan(2 * angle + atan(slope_f))
        x_coord, y_coord = self.axes.point_to_coords(intersection_point)
        y_intercept = y_coord - slope_reflection * x_coord
        reflection = lambda x: slope_reflection * x + y_intercept
        return self.axes.plot(reflection, x_range=[0, 10], color=GREEN)
