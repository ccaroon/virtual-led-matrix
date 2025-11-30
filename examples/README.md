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
    - `led-walker.py --help`
* [display-message.py](./display-message.py)
    - Display a message on the LED Matrix
    - `display-message.py "Hello, World!"`
* [digital-clock.py](./digital-clock.py)
    - Display a digital clock on the LED Matrix
    - Uses the `noframe` option to make the clock window titleless & borderless
    - Press "Q" to exit.
    - `digital-clock.py --help`
* [binary-clock.py](./binary-clock.py)
    - Display a binary clock on the LED Matrix
    - Uses the `noframe` option to make the clock window titleless & borderless
    - Press "Q" to exit.
    - `binary-clock.py --help`
