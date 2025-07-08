from manim import *
from custom_colors import DRACULA_BG
from styled_code import StyledCode
import random

config.background_color = DRACULA_BG

class Intro(Scene):
    def construct(self):
        student_code = StyledCode(
            "code_snippets/Student.java",
            language="java",
            background_stroke_width=1
        )
        wojak = ImageMobject("assets/smug_wojak.png")
        laptop = ImageMobject("assets/laptop.png")
        bad_code = ImageMobject("assets/bad_code.png")
        pointing_wojak = ImageMobject("assets/pointing_wojak.png")
        uml = ImageMobject("assets/uml.png")
        num_squares: int = 10
        squares = VGroup(*[
            Square(
            side_length=1,
            fill_color=random_color(),
            fill_opacity=1
            ).move_to([
            random.uniform(-3, 3),
            random.uniform(-3, 3),
            0
            ]) for _ in range(num_squares)
        ])
        square_colors: List = [square.fill_color for square in squares]
        aligned_squares = VGroup(*[
            Square(
                side_length=1,
                fill_color=square_colors[i % num_squares],
                fill_opacity=1
            ).move_to([
                i % 5 - 2,
                i // 5 - 1,
                0
            ]) for i in range(num_squares)
        ])   

        student_code.remove(student_code.background_mobject)

        student_code.scale(0.6)
        laptop.scale(1.75)
        bad_code.scale(2)

        laptop.shift(RIGHT * 2, DOWN)

        self.play(FadeIn(student_code))
        self.wait(1)
        self.play(FadeOut(student_code))
        self.play(FadeIn(wojak))
        self.wait(1)
        self.play(FadeIn(laptop))
        self.wait(1)
        self.play(FadeOut(wojak, laptop), run_time=0.5)
        self.wait(1)
        self.play(FadeIn(bad_code))
        self.wait(1)
        self.play(FadeOut(bad_code))
        self.wait(1)
        self.play(FadeIn(pointing_wojak))
        self.wait(1)
        self.play(FadeIn(uml))
        self.wait(1)
        self.play(FadeOut(uml, pointing_wojak))
        self.wait(1)
        self.play(FadeIn(squares))
        self.wait(1)
        self.play(Transform(squares, aligned_squares))
        self.wait(1)