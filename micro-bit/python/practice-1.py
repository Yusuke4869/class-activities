def button_a():
    basic.show_arrow(ArrowNames.NORTH)
    basic.show_arrow(ArrowNames.NORTH_EAST)
    basic.show_arrow(ArrowNames.EAST)
    basic.show_arrow(ArrowNames.SOUTH_EAST)
    basic.show_arrow(ArrowNames.SOUTH)
    basic.show_arrow(ArrowNames.SOUTH_WEST)
    basic.show_arrow(ArrowNames.WEST)
    basic.show_arrow(ArrowNames.NORTH_WEST)

def button_b():
    basic.show_arrow(ArrowNames.NORTH)
    basic.show_arrow(ArrowNames.NORTH_WEST)
    basic.show_arrow(ArrowNames.WEST)
    basic.show_arrow(ArrowNames.SOUTH_WEST)
    basic.show_arrow(ArrowNames.SOUTH)
    basic.show_arrow(ArrowNames.SOUTH_EAST)
    basic.show_arrow(ArrowNames.EAST)
    basic.show_arrow(ArrowNames.NORTH_EAST)

input.on_button_pressed(Button.A, button_a)
input.on_button_pressed(Button.B, button_b)