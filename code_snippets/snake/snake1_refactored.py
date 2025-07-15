class Snake:
    def __init__(self, head_x, head_y, body_coords, direction):
        self.head_x = head_x
        self.head_y = head_y
        self.body_coords = body_coords
        self.direction = direction

    def move(self):
        if self.direction == "UP":
            self.head_y -= 1
        elif self.direction == "DOWN":
            self.head_y += 1
        elif self.direction == "LEFT":
            self.head_x -= 1
        elif self.direction == "RIGHT":
            self.head_x += 1

        self.body_coords.insert(0, (self.head_x, self.head_y))