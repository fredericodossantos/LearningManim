from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))
        

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, LEFT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square
        # create a triangle
        triangle = Triangle()

        self.play(Create(triangle))  # show the triangle on screen
        self.play(triangle.animate.shift(LEFT))  # move the triangle to the left
        self.play(triangle.animate.shift(RIGHT * 2))  # move the triangle to the right
        self.play(triangle.animate.rotate(PI / 2))  # rotate the triangle 90 degrees
        self.play(FadeOut(triangle))  # fade out animation



        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class RotatingSquare(Scene):
    def construct(self):
        square = Square().set_fill(BLUE_E, opacity=1)
        self.play(Create(square))
        self.play(Rotate(square, PI), run_time=2)
        self.wait() 


class MovingBox(Scene):
    def construct(self):
        
        box = Rectangle(stroke_color = GREEN_C, stroke_opacity= 0.7 , fill_color = RED_B,  fill_opacity = 0.5, height=1, width=1)

        self.add(box)  # show the box on screen
        self.play(box.animate.shift(RIGHT*2), run_time=2) # move the box to the right for 2 seconds
        self.play(box.animate.shift(UP*3), run_time=2) # move the box up for 2 seconds
        self.play(box.animate.shift(DOWN*5 + LEFT*5), run_time=2) # move the box down and to the left for 2 seconds
        self.play(box.animate.shift(UP*1.5 + RIGHT*1), run_time=2) # move the box up and to the right for 2 seconds
        self.play(box.animate.shift(DOWN*1.5 + LEFT*1), run_time=2) # move the box down and to the left for 2 seconds
        self.wait() # wait for the animation to finish

# FittingObjectsOnScreen
class FittingObjects(Scene):
    def construct(self):

        axes = Axes(x_range=[-3,3,.1], y_range=[-3,3,.1], x_length=6, y_length=6)
        axes.to_edge(LEFT, buff=0.5)

        circle = Circle(stroke_width = 6, stroke_color = BLUE, fill_color = BLUE, fill_opacity = 0.5)
        circle.set_width(2).to_edge(DR, buff=0)

        triangle = Triangle(stroke_width = 10, stroke_color = RED).shift(DOWN*3+RIGHT*3)

        self.play(Write(axes), run_time=2)
        self.play(DrawBorderThenFill(circle), run_time=2)
        self.play(circle.animate.set_width(1), run_time=2)
        self.play(Transform(circle, triangle), run_time=3)

        
