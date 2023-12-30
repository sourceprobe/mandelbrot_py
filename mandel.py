#!/usr/bin/env python3

RESOLUTION_X = 150
RESOLUTION_Y = 60
OUTPUT_RES_X = 3.5
OUTPUT_RES_Y = 2
OUTPUT_OFFSET_X = -2.5
OUTPUT_OFFSET_Y = -1
MAX_ITERATIONS = 27

def calc(xi, yi):
    # return the number of iterations
    xi = xi / RESOLUTION_X * OUTPUT_RES_X + OUTPUT_OFFSET_X
    yi = yi / RESOLUTION_Y * OUTPUT_RES_Y + OUTPUT_OFFSET_Y
    x = 0.0;
    y = 0.0;
    iteration = 0
    while x*x + y*y < 4 and iteration < MAX_ITERATIONS: 
        xtemp = x*x - y*y + xi
        y = 2*x*y + yi;
        x = xtemp;
        iteration += 1;
    return iteration

def show(value):
    # int -> character for display
    if value <= 26:
        return chr(ord('A') + value - 1)
    return ' ';

def draw_window(w, h):
    for yi in range(0, h):
        for xi in range(0, w):
            value = show(calc(xi, yi))
            print(value, end='')
        print("")

if __name__ == "__main__":
  draw_window(RESOLUTION_X, RESOLUTION_Y)
