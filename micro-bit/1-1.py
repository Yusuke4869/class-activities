def button_a():
    basic.show_arrow(ArrowNames.EAST)

def button_b():
    basic.show_arrow(ArrowNames.WEST)

input.on_button_pressed(Button.A, button_a)
input.on_button_pressed(Button.B, button_b)