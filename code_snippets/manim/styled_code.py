from manim import Code

class StyledCode(Code):
    def __init__(
        self, *args, 
        language,
        has_line_numbers=False,
        background_config={"stroke_width": 0},
        **kwargs
    ):
        super().__init__(
            *args,
            language=language,
            add_line_numbers=has_line_numbers,
            background_config=background_config,
            formatter_style="dracula",
            **kwargs
        )