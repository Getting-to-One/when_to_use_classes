from manim import Scene, Code
from StyledCode import StyledCode

class Foo(Scene):
    def construct(self):
        student_code = StyledCode(
            "code_snippets/Student.java",
            language="java"
        )
        bad_snake_code = StyledCode(
            "code_snippets/bad_snake.py",
            language="python"
        )
        good_snake_code = StyledCode(
            "code_snippets/good_snake.py",
            language="python"
        )