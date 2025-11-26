# Virtual LED Matrix // Examples

* [random-leds-1.py](./random-leds-1.py)
    - Code that uses the `LEDMatrix` class directly (defnining it's own event loop) to light random colored LEDs on the screen.
    - Demonstrates using the `LEDMatrix` class directly.
* [random-leds-2.py](./random-leds-2.py)
    - A LED Matrix Program, defined as a single function and executed with the `Program.exec_func` class method, that lights random colored LEDs on the screen.
    - Demonstrates using the `Program.exec_func` method to run a simple program.
* [random-leds-3.py](./random-leds-3.py)
    - A LED Matrix Program, defined as a sub-class of `Program`, that lights random colored LEDs on the screen.
    - Demonstrates using a sub-class of the `Program` class for more complex programs.
* [led-walker.py](./led-walker.py)
    - A LED Matrix Program that "walks" across the LED Matrix, lighting each LED in turn.
    - Useful for testing different LED colors, shapes, sizes and spacing.
