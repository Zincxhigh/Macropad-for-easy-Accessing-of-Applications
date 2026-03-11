import board
import busio
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

from kmk.modules.encoder import EncoderHandler
from kmk.extensions.oled import OLED
from kmk.extensions.oled.display import Display

keyboard = KMKKeyboard()

# ---------------- MATRIX ----------------

keyboard.row_pins = (board.D0, board.D1)
keyboard.col_pins = (board.D4, board.D5, board.D6)

keyboard.diode_orientation = DiodeOrientation.COL2ROW


# ---------------- KEYMAP ----------------

keyboard.keymap = [
    [
        KC.F13, KC.F14, KC.NO,
        KC.F15, KC.F16, KC.F17
    ]
]

# Assign
# F13 → KiCad
# F14 → Discord
# F15 → VSCode
# F16 → Browser
# F17 → Desktop switching


# ---------------- ENCODER ----------------

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

volume_level = 50
last_volume_change = 0


def vol_up():
    global volume_level, last_volume_change
    volume_level = min(100, volume_level + 2)
    last_volume_change = time.monotonic()
    return KC.VOLU


def vol_down():
    global volume_level, last_volume_change
    volume_level = max(0, volume_level - 2)
    last_volume_change = time.monotonic()
    return KC.VOLD


encoder_handler.pins = ((board.D7, board.D8, board.D9),)

encoder_handler.map = [
    ((vol_down, vol_up, KC.MUTE),)
]


# ---------------- OLED ----------------

i2c = busio.I2C(board.SCL, board.SDA)

oled_ext = OLED(
    Display(
        width=128,
        height=64,
        i2c=i2c,
        address=0x3C
    )
)

keyboard.extensions.append(oled_ext)


# ---------------- OLED DISPLAY LOGIC ----------------

def oled_task():

    if time.monotonic() - last_volume_change < 3:

        oled_ext.display.clear()

        oled_ext.display.text("Volume", 0, 0)

        oled_ext.display.text(
            str(volume_level) + "%",
            0,
            20
        )

        bar = int(volume_level / 5)

        oled_ext.display.text(
            "[" + "#" * bar + "]",
            0,
            40
        )

    else:

        t = time.localtime()

        oled_ext.display.clear()

        oled_ext.display.text("Macropad", 0, 0)

        oled_ext.display.text(
            f"{t.tm_hour}:{t.tm_min:02}",
            0,
            20
        )

        oled_ext.display.text(
            f"{t.tm_mday}/{t.tm_mon}/{t.tm_year}",
            0,
            40
        )


keyboard.before_matrix_scan = oled_task

if __name__ == "__main__":
    keyboard.go()