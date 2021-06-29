count = 0
basic.show_number(0)

def button_a():
    global count
    count+=1
    basic.show_number(count)

def button_b():
    global count
    count = 0
    basic.show_number(count)

input.on_button_pressed(Button.A, button_a)
input.on_button_pressed(Button.B, button_b)