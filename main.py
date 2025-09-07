from manim import *
from custom_colors import *
from styled_code import StyledCode
from styled_code_window import StyledCodeWindow
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
            "Pattern #1: Repetition in variable/function names",
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
        CIRCUMSCRIBE_TIME: int = 6
        SCALE_FACTOR = 0.5

        ugly_code = StyledCode("code_snippets/database/database.py")
        mid_code = StyledCode("code_snippets/database/database_mid.py")
        lines_with_connection: list[int] = [0, 7, 16, 34] # in mid
        lines_with_cursor: list[int] = [1, 6, 8, 12, 21, 26, 28] # in mid
        good_code = StyledCode("code_snippets/database/database_refactored.py")
        database_class = StyledCodeWindow(
            "code_snippets/database/database_class.py",
            "Database.py"
        )
        main_file = StyledCodeWindow("code_snippets/database/main.py")
        docstring_image = ImageMobject("assets/docstring.png")
        pattern = Text(
            "Pattern #2: Similar/related functions",
            color=DRACULA_COMMENT,
            font_size=30
        )

        # Bg removal
        ugly_code.remove(ugly_code.background)
        mid_code.remove(mid_code.background)
        good_code.remove(good_code.background)

        # Scaling
        ugly_code.scale(SCALE_FACTOR)
        mid_code.scale(SCALE_FACTOR)
        good_code.scale(SCALE_FACTOR)
        database_class.scale(SCALE_FACTOR)
        main_file.scale(SCALE_FACTOR)

        # Positioning
        docstring_image.to_edge(DOWN)
        database_class.to_edge(LEFT)
        main_file.to_edge(RIGHT)
        pattern.to_corner(DR)

        self.play(FadeIn(ugly_code))
        self.wait(1)
        self.add(docstring_image)
        self.play(
            Circumscribe(
                ugly_code.code_lines[4],
                color=DRACULA_YELLOW,
                time_width=CIRCUMSCRIBE_TIME
            ),
            Circumscribe(
                ugly_code.code_lines[10],
                color=DRACULA_YELLOW,
                time_width=CIRCUMSCRIBE_TIME
            ),
            Circumscribe(
                ugly_code.code_lines[18],
                color=DRACULA_YELLOW,
                time_width=CIRCUMSCRIBE_TIME
            )
        )
        self.remove(docstring_image)
        self.wait(1)
        self.play(FadeIn(pattern))
        self.wait(1)
        self.play(FadeOut(pattern))
        self.wait(1)
        self.play(Transform(ugly_code, mid_code))
        self.wait(1)
        circumscribe_lines_with_connection = [
            Circumscribe(
                ugly_code.code_lines[i],
                color=DRACULA_YELLOW,
                time_width=CIRCUMSCRIBE_TIME
            ) for i in lines_with_connection
        ]
        self.play(
            *circumscribe_lines_with_connection
        )
        circumscribe_lines_with_cursor = [
            Circumscribe(
                ugly_code.code_lines[i],
                color=DRACULA_YELLOW,
                time_width=CIRCUMSCRIBE_TIME
            ) for i in lines_with_cursor
        ]
        self.play(*circumscribe_lines_with_cursor)
        self.wait(1)
        self.play(Transform(ugly_code, good_code))
        self.wait(1)
        self.play(ApplyWave(ugly_code.code_lines[0:37]))
        self.play(FadeOut(ugly_code.code_lines[0:37]), run_time=0.5)
        self.wait(1)
        self.play(
            FadeIn(database_class),
            ReplacementTransform(ugly_code.code_lines[38], main_file)
        )
        self.wait(1)
        self.play(FadeOut(database_class), main_file.animate.center())
        self.wait(1)

class Subclass(Scene):
    def construct(self):
        SCALE_FACTOR = 0.5
        CIRCUMSCRIBE_TIME: int = 5

        bad_code = StyledCode("code_snippets/manim/bad_code.py")
        code_class = StyledCode("code_snippets/manim/styled_code.py")
        new_code = StyledCode("code_snippets/manim/new_code.py")
        same_args = VGroup(
            bad_code.code_lines[7:10],
            bad_code.code_lines[14:17],
            bad_code.code_lines[21:24]
        )
        pattern = Text(
            "Pattern #3: Repeat arguments in constructors",
            color=DRACULA_COMMENT,
            font_size=30
        )
        default_args_bad_code : list[int] = [7, 8, 14, 15, 22, 23]
        indicate_default_args_bad_code : list[Indicate] = [
            Indicate(
                bad_code.code_lines[i],
                color=DRACULA_YELLOW,
                scale_factor=1.1
            ) for i in default_args_bad_code
        ]
        default_args_code_class : list[int] = [6, 7, 13, 16]
        indicate_default_args_code_class : list[Indicate] = [
            Indicate(
                code_class.code_lines[i],
                color=DRACULA_YELLOW,
                scale_factor=1.1
            ) for i in default_args_code_class
        ]
        hard_coded_args : list[int] = [9, 16, 23]
        indicate_hard_coded_args : list[Indicate] = [
            Indicate(
                bad_code.code_lines[i],
                color=DRACULA_YELLOW,
                scale_factor=1.1
            ) for i in hard_coded_args
        ]

        # Bg removal
        bad_code.remove(bad_code.background)
        code_class.remove(code_class.background)
        new_code.remove(new_code.background)

        # Scaling
        bad_code.scale(SCALE_FACTOR)
        code_class.scale(SCALE_FACTOR)
        new_code.scale(SCALE_FACTOR)

        # Positioning
        pattern.to_edge(UP)
        code_class.to_edge(RIGHT)

        self.play(FadeIn(bad_code))
        self.wait(1)
        self.play(
            Circumscribe(
                bad_code.code_lines[4][13:17],
                color=DRACULA_YELLOW,
                time_width=CIRCUMSCRIBE_TIME
            ),
            Circumscribe(
                bad_code.code_lines[11][15:19],
                color=DRACULA_YELLOW,
                time_width=CIRCUMSCRIBE_TIME
            ),
            Circumscribe(
                bad_code.code_lines[18][16:20],
                color=DRACULA_YELLOW,
                time_width=CIRCUMSCRIBE_TIME
            )
        )
        self.wait(1)
        self.play(
            *[Circumscribe(
                arg, color=DRACULA_YELLOW, time_width=CIRCUMSCRIBE_TIME + 2
            ) for arg in same_args]
        )
        self.play(FadeIn(pattern))
        self.wait(1)
        self.play(FadeOut(pattern))
        self.wait(1)
        self.play(bad_code.animate.to_edge(LEFT), FadeIn(code_class))
        self.wait(1)
        self.play(
            *indicate_default_args_bad_code,
            *indicate_default_args_code_class
        )
        self.wait(1)
        self.play(
            *indicate_hard_coded_args,
            Indicate(
                code_class.code_lines[15],
                color=DRACULA_YELLOW,
                scale_factor=1.1
            )
        )
        self.wait(1)
        new_code.move_to(bad_code.get_center())
        self.play(FadeTransform(bad_code, new_code))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class Outro(Scene):
    def construct(self):
        FONT_SIZE=38
        red_flags = Text("Red flags:", color=DRACULA_RED)
        pattern1 = Text(
            "Repetition in function/variable names",
            color=DRACULA_FOREGROUND,
            font_size=FONT_SIZE
        )
        pattern2 = Text(
            "Similar/related functions",
            color=DRACULA_FOREGROUND,
            font_size=FONT_SIZE
        )
        pattern3 = Text(
            "Repeat arguments in constructors",
            color=DRACULA_FOREGROUND,
            font_size=FONT_SIZE
        )

        # Positioning
        red_flags.to_corner(UL).shift(DOWN * 2)
        pattern1.next_to(red_flags, DOWN, aligned_edge=LEFT)
        pattern2.next_to(pattern1, DOWN, aligned_edge=LEFT)
        pattern3.next_to(pattern2, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(red_flags))
        self.wait(1)
        self.play(FadeIn(pattern1))
        self.play(FadeIn(pattern2))
        self.play(FadeIn(pattern3))
        self.wait(1)