import turtle

# Константы длин (в пикселях)
VERTICAL_LENGTH = 40    # все вертикальные линии одинаковые
HORIZONTAL_LENGTH = 10   # все горизонтальные линии одинаковые
STEP = 1                # шаг движения черепашки

def perform_switch_case(state, t):
    x = round(t.position()[0] / STEP)
    y = round(t.position()[1] / STEP)

    # Целевые координаты для поворотов
    v_steps = VERTICAL_LENGTH // STEP    # 15 шагов вниз/вверх
    h_steps = HORIZONTAL_LENGTH // STEP  # 5 шагов влево

    # 1. ВНИЗ
    if state == "INIT":
        state = "DOWN_1"
        t.setheading(270)
        return state

    if state == "DOWN_1":
        t.forward(STEP)
        if y <= -v_steps:
            state = "LEFT_1"
            t.setheading(180)
        return state

    # 2. ВЛЕВО
    if state == "LEFT_1":
        t.forward(STEP)
        if x <= -h_steps:
            state = "UP_1"
            t.setheading(90)
        return state

    # 3. ВВЕРХ
    if state == "UP_1":
        t.forward(STEP)
        if y >= 0:
            state = "LEFT_2"
            t.setheading(180)
        return state

    # 4. ВЛЕВО
    if state == "LEFT_2":
        t.forward(STEP)
        if x <= -h_steps * 2:
            state = "DOWN_2"
            t.setheading(270)
        return state

    # 5. ВНИЗ
    if state == "DOWN_2":
        t.forward(STEP)
        if y <= -v_steps:
            state = "LEFT_3"
            t.setheading(180)
        return state

    # 6. ВЛЕВО
    if state == "LEFT_3":
        t.forward(STEP)
        if x <= -h_steps * 3:
            state = "UP_2"
            t.setheading(90)
        return state

    # 7. ВВЕРХ
    if state == "UP_2":
        t.forward(STEP)
        if y >= 0:
            state = "LEFT_4"
            t.setheading(180)
        return state

    # 8. ВЛЕВО
    if state == "LEFT_4":
        t.forward(STEP)
        if x <= -h_steps * 4:
            state = "DOWN_FINAL"
            t.setheading(270)
        return state

    # 9. ВНИЗ (финальный)
    if state == "DOWN_FINAL":
        t.forward(STEP)
        if y <= -v_steps:
            state = "STOP"
        return state

    return state

def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state

    t = turtle.Turtle()
    t.speed(1)

    while curr_state != end_state:
        curr_state = perform_switch_case(curr_state, t)

    turtle.done()

if __name__ == "__main__":
    draw()