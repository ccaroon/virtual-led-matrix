#!/usr/bin/env python
import pygame
import random

from led_matrix.color import Color
from led_matrix.led_matrix import LEDMatrix

# Construct a LEDMatrix instance
matrix = LEDMatrix(
    title = "Random LEDs #1",
    width = 1024, height = 768
)

# Define the event loop. Must interact with pygame directly to get events.
# Then use the LEDMatrix instance, `matrix`, to control the LEDs.
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x = random.randint(0, matrix.width)
    y = random.randint(0, matrix.height)

    color = Color.random()

    matrix.set_led(x, y, color)
    matrix.update()

matrix.quit()
