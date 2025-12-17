# You import all the IOs of your board
import board
import busio

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

i2c_bus = busio.I2C(board.GP7, board.GP6)
                    
driver = SSD1306(
    i2c=i2c_bus
)

encoder_handler = EncoderHandler()

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

keyboard.modules = [encoder_handler]

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.GP3, board.GP4, board.GP2, board.GP1, board.GP0, board.GP29]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

encoder_handler.pins = (board.GP27, board.GP26, board.GP28)  # A, B, BTN

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.N8, KC.N8, KC.N8, KC.N8, KC.N8, KC.N8]  # Will fill actual keymap later
]

encoder_handler.map = [
    (KC.VOLD, KC.VOLU, KC.MUTE)
]

display = Display(
    display=driver,
    width=128, # screen size
    height=64, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    brightness=1, # initial screen brightness level
    brightness_step=0.1, # used for brightness increase/decrease keycodes
    # dim_time=0, # time in seconds to reduce screen brightness
    # dim_target=1, # set level for brightness decrease
    # off_time=0, # time in seconds to turn off screen
    # powersave_dim_time=10, # time in seconds to reduce screen brightness
    # powersave_dim_target=0.1, # set level for brightness decrease
    # powersave_off_time=30, # time in seconds to turn off screen
)

display.entries = [
    ImageEntry(image="lightning.bmp", x=0, y=0),
    TextEntry(text="ZeusyBoy", x=40, y=20),
]
keyboard.extensions.append(display)

# Start kmk!
if __name__ == '__main__':
    keyboard.go()