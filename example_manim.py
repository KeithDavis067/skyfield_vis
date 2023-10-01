from manim import RIGHT, TAU, PINK, YELLOW_A, PURPLE_E, DEGREES, WHITE, YELLOW, GREEN, PI
from manim import Scene, ThreeDScene, Circle, Square, Create, Transform, FadeOut, FadeIn, Ellipse
from manim import Line, Cube, Write, Unwrite, Sphere, Dot3D, VGroup, MoveAlongPath, linear, Rotate, UpdateFromAlphaFunc


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class CircletoEllipse(Scene):
    def construct(self):
        self.camera.background_color = YELLOW_A
        circle = Circle().set_color(PURPLE_E)
        ellipse = Ellipse(2, 0.5).set_color(PURPLE_E)
        line = Line().set_color(PURPLE_E)

        self.play(Create(circle))
        self.play(Transform(circle, ellipse))
        self.play(Transform(ellipse, line))
        self.play(FadeOut(line))


class Rotation3DCube(ThreeDScene):
    def construct(self):
        cube = Cube(side_length=3, fill_opacity=1)

        self.begin_ambient_camera_rotation(about='gamma', rate=0.3)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.play(Write(cube), run_time=2)

        self.wait(3)

        self.play(Unwrite(cube), run_time=2)


class Rotation3DExample(ThreeDScene):
    def construct(self):
        sphere = Sphere(radius=3, fill_opacity=1)

        self.begin_ambient_camera_rotation(rate=0.3)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.play(Write(sphere), run_tme=2)

        self.wait(3)

        self.play(Unwrite(sphere), run_time=2)


class Rotation3DCircle(ThreeDScene):
    def construct(self):
        circle = Circle(radius=3, fill_opacity=1)

        self.begin_ambient_camera_rotation(about='phi', rate=0.5)

        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.play(Write(circle), run_time=2)

        self.wait(3)

        self.play(Unwrite(circle), run_time=2)


class Orbit_Motion(ThreeDScene):
    # Default aspect ration is 14 by 8
    # Note Ratefunction Linear.
    def construct(self):
        orbit = Circle(radius=3).set_color(WHITE)
        sun = Dot3D(radius=0.5).set_color(YELLOW)
        sun_group = VGroup(orbit, sun)

        earth = Dot3D(radius=0.4).set_color(GREEN)
        orbit_moon = Circle(radius=1).set_opacity(0)
        moon = Dot3D(radius=0.3).set_color(YELLOW_A)
        earth_group = VGroup(earth, orbit_moon)

        # earth_group.rotate_about_origin(720),
        def update_rotate_move(mob, alpha):
            mob.move_to(orbit_moon.point_from_proportion(alpha))
            mob.rotate(PI*alpha, about_point=earth.get_center())

        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # self.begin_ambient_camera_rotation(about='theta', rate = 0.2)
        self.begin_ambient_camera_rotation(about='phi', rate=1)

        self.add(sun_group, earth_group.shift(RIGHT*3), moon.shift(RIGHT*4))
        self.play(  # MoveAlongPath(moon,orbit_moon,rate_func = linear, run_time = 8),
            MoveAlongPath(earth_group, orbit, rate_func=linear, run_time=8),
            Rotate(moon, PI, about_point=earth.get_center(), rate_func=linear),
            UpdateFromAlphaFunc(moon, update_rotate_move, rate_func=linear),
            run_time=8
        )
        # self.wait(3)
