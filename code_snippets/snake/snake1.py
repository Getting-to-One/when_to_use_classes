snake_head_x = 0
snake_head_y = 0
snake_body_coords = [(0, 0)]
snake_direction = "RIGHT"

def move_snake():
    global snake_head_x, snake_head_y, snake_body_coords, snake_direction

    if snake_direction == "UP":
        snake_head_y -= 1
    elif snake_direction == "DOWN":
        snake_head_y += 1
    elif snake_direction == "LEFT":
        snake_head_x -= 1
    elif snake_direction == "RIGHT":
        snake_head_x += 1

    snake_body_coords.insert(0, (snake_head_x, snake_head_y))