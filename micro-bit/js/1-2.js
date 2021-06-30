let count = 0;
basic.showNumber(0);

input.onButtonPressed(Button.A, function button_a() {
    count++;
    basic.showNumber(count);
})

input.onButtonPressed(Button.B, function button_b() {
    count = 0;
    basic.showNumber(count);
})