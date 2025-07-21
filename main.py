from manim import *
from custom_colors import *
from styled_code import StyledCode
import random

config.background_color = DRACULA_BG

class Intro(Scene):
    def construct(self):
        student_code = StyledCode(
            "code_snippets/Student.java",
            language="java"
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
        square_colors: list = [square.fill_color for square in squares]
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

        student_code.remove(student_code.background)

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

class SnakeExample(Scene):
    def construct(self):
        # Code mobjects
        ugly_snake_code = StyledCode("code_snippets/snake/snake1.py")
        better_snake_code = StyledCode(
            "code_snippets/snake/snake1_refactored.py"
        )
        tip1 = Text(
            "Pattern #1: Repetition in variable/function names.",
            color=DRACULA_COMMENT,
            font_size=30
        )
        ugly_multiplayer_code = StyledCode(
            "code_snippets/snake/snake2.py"
        )
        better_multiplyer_code = StyledCode(
            "code_snippets/snake/snake2_refactored.py"
        )
        before = Text("Before:", color=DRACULA_COMMENT, font_size=30)
        after = Text("After:", color=DRACULA_COMMENT, font_size=30)

        # Sizing
        SCALE_FACTOR = 0.5
        ugly_snake_code.scale(SCALE_FACTOR)
        better_snake_code.scale(SCALE_FACTOR)

        # Positioning
        tip1.to_edge(UP)
        # ugly_snake_code.to_edge(LEFT)
        better_snake_code.to_edge(RIGHT)
        before.next_to(ugly_snake_code, UP).to_edge(LEFT)
        after.next_to(better_snake_code, UP).align_to(better_snake_code, LEFT)

        # Bg removal
        ugly_snake_code.remove(ugly_snake_code.background)
        better_snake_code.remove(better_snake_code.background)

        # Rectangles
        variables_rectangle = SurroundingRectangle(
            ugly_snake_code.code_lines[0:4], color=DRACULA_COMMENT
        )
        function_rectangle = SurroundingRectangle(
            ugly_snake_code.code_lines[5], color=DRACULA_COMMENT
        )

        self.play(FadeIn(ugly_snake_code))
        self.wait(1)
        self.play(Create(variables_rectangle))
        self.play(FadeOut(variables_rectangle))
        self.play(Create(function_rectangle))
        self.play(FadeOut(function_rectangle))
        self.wait(1)
        self.play(FadeIn(tip1))
        self.wait(1)
        self.play(FadeOut(tip1))
        self.wait(1)
        self.play(
            ugly_snake_code.animate.to_edge(LEFT),
            FadeIn(before, after),
            Create(better_snake_code)
        )
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])