snake1_head_x = 0
snake1_head_y = 0
snake1_body_coords = [(0, 0)]
snake1_direction = "RIGHT"

snake2_head_x = 10
snake2_head_y = 10
snake2_body_coords = [(10, 10)]
snake2_direction = "LEFT"

def move_snake1():
    global snake1_head_x, snake1_head_y, snake1_body_coords
    global snake1_direction

    if snake1_direction == "UP":
        snake1_head_y -= 1
    elif snake1_direction == "DOWN":
        snake1_head_y += 1
    elif snake1_direction == "LEFT":
        snake1_head_x -= 1
    elif snake1_direction == "RIGHT":
        snake1_head_x += 1

    snake1_body_coords.insert(0, (snake1_head_x, snake1_head_y))

def move_snake2():
        global snake2_head_x, snake2_head_y, snake2_body_coords
        global snake2_direction

        if snake2_direction == "UP":
            snake2_head_y -= 1
        elif snake2_direction == "DOWN":
            snake2_head_y += 1
        elif snake2_direction == "LEFT":
            snake2_head_x -= 1
        elif snake2_direction == "RIGHT":
            snake2_head_x += 1

        snake2_body_coords.insert(0, (snake2_head_x, snake2_head_y))