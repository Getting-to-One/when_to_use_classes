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
        ugly_snake_code = StyledCode("code_snippets/snake/snake1.py")
        better_snake_code = StyledCode(
            "code_snippets/snake/snake1_refactored.py"
        )
        tip1 = Text(
            "Pattern #1: Repetition in variable/function names.",
            color=DRACULA_COMMENT,
            font_size=30
        )
        before = Text("Before:", color=DRACULA_COMMENT, font_size=30)
        after = Text("After:", color=DRACULA_COMMENT, font_size=30)
        pros = Text("Pros:", color=DRACULA_COMMENT, font_size=30)
        pros_list = BulletedList(
            "No global variables",
            "Scalable"
        )

        # Color
        pros_list.set_color(DRACULA_COMMENT)

        # Sizing
        SCALE_FACTOR = 0.5
        ugly_snake_code.scale(SCALE_FACTOR)
        better_snake_code.scale(SCALE_FACTOR)
        pros_list.scale(0.7)

        # Positioning
        tip1.to_edge(UP)
        better_snake_code.to_edge(RIGHT)
        before.next_to(ugly_snake_code, UP).to_edge(LEFT)
        after.next_to(better_snake_code, UP).align_to(better_snake_code, LEFT)
        pros.next_to(better_snake_code, DOWN).align_to(better_snake_code,LEFT)
        pros_list.next_to(pros, DOWN).align_to(better_snake_code, LEFT)

        # Bg removal
        ugly_snake_code.remove(ugly_snake_code.background)
        better_snake_code.remove(better_snake_code.background)

        # Emphasis
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
        x = Cross(ugly_snake_code.code_lines[0:5], color=DRACULA_RED).scale(0.5)
        self.wait(1)
        self.play(FadeIn(pros))
        self.play(FadeIn(pros_list[0]), Create(x))
        self.play(FadeIn(pros_list[1]))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class MultiplayerSnake(Scene):
    def construct(self):
        TEXT_SIZE = 30
        ugly_code = StyledCode("code_snippets/snake/snake2.py")
        without_classes = Text(
            "Without classes:",
            color=DRACULA_COMMENT,
            font_size=TEXT_SIZE,
        )
        classless_group = VGroup(without_classes, ugly_code)
        better_code = StyledCode("code_snippets/snake/snake2_refactored.py")
        with_classes = Text(
            "With classes:",
            color=DRACULA_COMMENT,
            font_size=TEXT_SIZE
        )

        # Bg removal
        ugly_code.remove(ugly_code.background)
        better_code.remove(better_code.background)

        # Sizing
        SCALE_FACTOR = 0.45
        ugly_code.scale(SCALE_FACTOR)
        better_code.scale(SCALE_FACTOR)

        # Positioning
        better_code.to_edge(RIGHT)
        without_classes.next_to(ugly_code, UP).align_to(ugly_code, LEFT)
        with_classes.next_to(better_code, UP).align_to(better_code, LEFT)

        move_snake1_emphasis = SurroundingRectangle(
            ugly_code.code_lines[10],
            color=DRACULA_COMMENT
        )
        move_snake2_emphasis = SurroundingRectangle(
            ugly_code.code_lines[25],
            color=DRACULA_COMMENT
        )
        move_snake_emphasis = VGroup(
            move_snake1_emphasis, move_snake2_emphasis
        )

        self.play(FadeIn(classless_group))
        self.wait(1)
        self.play(Create(move_snake_emphasis))
        self.wait(1)
        self.play(FadeOut(move_snake_emphasis))
        self.wait(1)
        self.play(
            classless_group.animate.to_edge(LEFT),
            FadeIn(with_classes),
            Create(better_code)
        )
        self.wait(1)

class Database(Scene):
    def construct(self):
        ugly_code = StyledCode("code_snippets/database/database.py")
        mid_code = StyledCode("code_snippets/database/database_mid.py")
        good_code = StyledCode("code_snippets/database/database_refactored.py")

        # Bg removal
        ugly_code.remove(ugly_code.background)
        mid_code.remove(mid_code.background)
        good_code.remove(good_code.background)

        # Scaling
        SCALE_FACTOR = 0.5
        ugly_code.scale(SCALE_FACTOR)

        self.play(FadeIn(ugly_code))