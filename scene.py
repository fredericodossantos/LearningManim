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

        axes = Axes(x_range=[-3,3,.1], y_range=[-3,3,.1], x_length=6, y_length=6) # create axes
        axes.to_edge(LEFT, buff=0.5)# move it to the left of the screen with a buffer space

        circle = Circle(stroke_width = 6, stroke_color = BLUE, fill_color = BLUE, fill_opacity = 0.5)
        circle.set_width(2).to_edge(DR, buff=0) # set width and move to bottom right of screen

        triangle = Triangle(stroke_width = 10, stroke_color = RED).shift(DOWN*3+RIGHT*3)

        self.play(Write(axes), run_time=2)
        self.play(DrawBorderThenFill(circle), run_time=2)
        self.play(circle.animate.set_width(1), run_time=2)
        self.play(Transform(circle, triangle), run_time=3)


class GraphingMovement(Scene):
    def construct(self):
        axes = Axes(x_range=[-2,2,1], y_range=[-2,2,1], x_length=4, y_length=4,
                    axis_config={"include_tip": True, "numbers_to_exclude": [0]}).add_coordinates()
        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        graph = axes.plot(lambda x : x**2, x_range = [-2,2],  color = YELLOW)
        graphing_stuff = VGroup(axes, graph, axis_labels)

        self.play(DrawBorderThenFill(axes),Write(axis_labels))
        self.play(Create(graph))
        self.play(graphing_stuff.animate.shift(DOWN*4))
        self.play(axes.animate.shift(LEFT*3), run_time=3)
        self.wait()

class Graphing(Scene):
    def construct(self):

        my_plane = NumberPlane(x_range=[-6,6], x_length=5, y_range=[-10,10], y_length=5)
        my_plane.add_coordinates()
        my_plane.shift(RIGHT*3)

        my_function = my_plane.plot(lambda x : 0.1*(x-5)*x*(x+5), x_range=[-6,6], color=GREEN_B)

        area = my_plane.get_area(my_function, x_range=[-5,5], color=[BLUE, YELLOW])
        
        label = MathTex("f(x) = 0.1(x-5)x(x+5)").next_to(my_plane, UP, buff=0.2)

        horizontal_line = Line(start=my_plane.c2p(0,my_function.underlying_function(-2)),
                               end=my_plane.c2p(-2, my_function.underlying_function(-2)), stroke_color = YELLOW, stroke_width =10)

        self.play(Create(my_plane), run_time=2)
        self.play(Create(my_function), Write(label), run_time=2)
        self.play(FadeIn(area), run_time=2)
        self.play(Create(horizontal_line), run_time=2)


        self.wait(3)

# Graphing Vectors
class Vectors(VectorScene):
    def construct(self):
        plane = self.add_plane(animate=True).add_coordinates()
        vector = self.add_vector([-3, -2], color=YELLOW)

        basis = self.get_basis_vectors()
        self.add(basis)
        self.vector_to_coords(vector = vector)

        vector2 = self.add_vector([2, 2], color=GREEN)
        self.write_vector_coordinates(vector = vector2)
        self.wait(2)
        self.vector_to_coords(vector = vector2)
        self.wait(2)

# Matrix Linear Transformation Scene
class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=True,
            leave_ghost_vectors=True,
        )

    def construct(self):

        matrix = [[1,-0.2], [0.2,1]]

        matrix_tex = MathTex(r"\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}").to_edge(UL).add_background_rectangle()
        unit_square = self.get_unit_square()
        text = always_redraw(lambda: Tex("Det(A)").set(width=0.7).next_to(unit_square.get_center()))

        vect = self.get_vector([1, -2], color = PURPLE_B)

        rect1 = Rectangle(height=2, width=1, stroke_color = BLUE_A, fill_color = BLUE_D, fill_opacity=0.6).shift(UP*2+LEFT*2)
        
        circ1 = Circle(radius=1, stroke_color = BLUE_D, fill_color = RED_D, fill_opacity=0.6).shift(DOWN*2+RIGHT*1)

        self.add_transformable_mobject(vect, unit_square, rect1, circ1)

        self.add_background_mobject(matrix_tex, text)
        # self.add_foreground_mobjects(matrix_tex, text)
        self.apply_matrix(matrix, run_time=5)
        
        self.wait(2)

# Tutorial 1

class Tutorial1(Scene):
    def construct(self):

        plane = NumberPlane(
            x_range=[-5, 5],
            y_range=[-4, 4, 1],
            x_length=10,
            y_length=10,
        )
        plane.add_coordinates()
        plane.shift(RIGHT*2)

        vect1 = Line(
            start=plane.c2p(0, 0),
            end=plane.c2p(1, 2),            
            stroke_color = YELLOW
        ).add_tip()

        vect1_name = MathTex(r"\vec{v}").next_to(vect1, RIGHT, buff=0.1).set_color(YELLOW)

        vect2 = Line(
            start=plane.c2p(0, 0),
            end=plane.c2p(-2, 1),            
            stroke_color = RED
        ).add_tip()

        vect2_name = MathTex(r"\vec{w}").next_to(vect2, LEFT, buff=0.1).set_color(RED)

        vect3 = Line(
            start=plane.c2p(3,2),
            end=plane.c2p(1, 3),            
            stroke_color = RED
        ).add_tip()

        vect4 = Line(
            start=plane.c2p(0,0),
            end=plane.c2p(1, 3),            
            stroke_color = GREEN
        ).add_tip()

        vect4_name = MathTex("\\vec{v} + \\vec{w}").next_to(vect4, LEFT, buff=0.1).set_color(GREEN)

        stuff = VGroup(plane, vect1, vect2, vect3, vect4, vect1_name, vect2_name, vect4_name)

        box = RoundedRectangle(height=1.5, width=1.5, corner_radius=0.1, stroke_color = PINK).to_edge(DL)

        self.play(DrawBorderThenFill(plane), run_time=2)
        self.wait(1)
        self.play(
            GrowFromPoint(vect1, point = vect1.get_start()), 
            Write(vect1_name), run_time=2
            )
        
        self.wait(1)
        self.play(
            GrowFromPoint(vect2, point = vect2.get_start()), 
            Write(vect2_name), run_time=2
            )
        
        self.wait(1)
        self.play(
            Transform(vect2, vect3),
            vect2_name.animate.next_to(vect3, UP, buff=0.1),
            run_time=2
            )
        
        self.wait(1)
        self.play(
            LaggedStart(
                GrowFromPoint(vect4, point = vect4.get_start()),
                Write(vect4_name),
                run_time=3,
                lag_ratio=1
            )
        )
        self.wait(1)
        self.add(box)
        self.wait(1)
        self.play(
            stuff.animate.move_to(box.get_center()).set(width=1.2),
            run_time=3
        )
        self.wait(1)
