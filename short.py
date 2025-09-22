from manim import *
from custom_colors import *
from styled_code import StyledCode

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60
config.background_color = DRACULA_BG

class SnakeExample(Scene):
    def construct(self):
        ugly_snake_code = StyledCode("code_snippets/snake/snake1.py")
        better_snake_code = StyledCode(
            "code_snippets/snake/snake1_refactored.py"
        )

        # Sizing
        SCALE_FACTOR = 0.65
        ugly_snake_code.scale(SCALE_FACTOR)
        better_snake_code.scale(SCALE_FACTOR)

        # Positioning
        better_snake_code.shift(DOWN * 2)

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
        self.play(
            ugly_snake_code.animate.shift(UP * 4),
            Create(better_snake_code)
        )
        x = Cross(ugly_snake_code.code_lines[0:4], color=DRACULA_RED)
        self.wait(1)
        self.play(Create(x))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class MultiplayerSnake(Scene):
    def construct(self):
        ugly_code = StyledCode("code_snippets/snake/snake2.py")
        better_code = StyledCode("code_snippets/snake/snake2_refactored.py")

        # Bg removal
        ugly_code.remove(ugly_code.background)
        better_code.remove(better_code.background)

        # Sizing
        SCALE_FACTOR = 0.6
        ugly_code.scale(SCALE_FACTOR)
        better_code.scale(SCALE_FACTOR)

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

        self.play(FadeIn(ugly_code))
        self.wait(1)
        self.play(Create(move_snake_emphasis))
        self.wait(1)
        self.play(FadeOut(move_snake_emphasis))
        self.wait(1)
        self.play(
            ReplacementTransform(ugly_code, better_code)
        )
        self.wait(1)