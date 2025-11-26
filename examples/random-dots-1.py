#!/usr/bin/env python
import pygame
import random

from pixel_matrix.color import Color
from pixel_matrix.pixel_matrix import PixelMatrix

# Construct a PixelMatrix instance
matrix = PixelMatrix(
    title = "Standalone Random Dots",
    width = 1024, height = 768
)

# Define the event loop. Must interact with pygame directly to get events.
# Then use the PixelMatrix instance, `matrix`, to draw pixels.
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x = random.randint(0, matrix.width)
    y = random.randint(0, matrix.height)

    color = Color.random()

    matrix.set_pixel(x, y, color)
    matrix.update()

matrix.quit()
