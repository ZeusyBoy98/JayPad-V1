# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys

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

# Start kmk!
if __name__ == '__main__':
    keyboard.go()