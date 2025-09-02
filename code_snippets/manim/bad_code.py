from manim import Scene, Code

class Foo(Scene):
    def construct(self):
        student_code = Code(
            "code_snippets/Student.java",
            language="java",
            add_line_numbers=False,
            background_config={"stroke_width": 0},
            formatter_style="dracula"
        )
        bad_snake_code = Code(
            "code_snippets/bad_snake.py",
            language="python",
            add_line_numbers=False,
            background_config={"stroke_width": 0},
            formatter_style="dracula"
        )
        good_snake_code = Code(
            "code_snippets/good_snake.py",
            language="python",
            add_line_numbers=False,
            background_config={"stroke_width": 0},
            formatter_style="dracula"
        )