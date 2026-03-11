# XIAO MacroPad

A compact 6-key macropad with a rotary encoder and OLED display, built around the **Seeed Studio XIAO SAMD21** and powered by **KMK firmware**.

The macropad is designed for productivity shortcuts such as launching apps, switching desktops, and controlling system volume.

---

# Features

* 6 programmable keys (3×2 matrix)
* Rotary encoder for volume control
* Encoder press for mute
* OLED display

  * Shows **volume bar when adjusting volume**
  * Shows **date and time when idle**
* Built using **KMK firmware (CircuitPython)**

---

# Hardware

## Microcontroller

* Seeed Studio XIAO SAMD21

## BOM

* 6 × Mechanical switches
* 6 × Diodes
* 1 × EC11 rotary encoder
* 1 × 128×64 SSD1306 OLED (I2C)

---

# Layout

| COL0   | COL1    | COL2            |
| ------ | ------- | --------------- |
| KiCad  | Discord | Next Desktop    |
| VSCode | Browser | Current Desktop |

Encoder:

* Rotate → Volume up/down
* Press → Mute

---

# Pin Mapping

## Matrix

Rows:

* D0 → Row0
* D1 → Row1

Columns:

* D4 → Col0
* D5 → Col1
* D6 → Col2

## Encoder

* D7 → Encoder A
* D8 → Encoder B
* D9 → Encoder Switch

## OLED (I2C)

* SDA → SDA
* SCL → SCL

---

# Firmware

Firmware is written using **KMK**.

Main features:

* Matrix scanning
* Encoder volume control
* OLED UI
* Application shortcuts

The firmware is located in:

```
firmware/code.py
```

---

# Images

## Schematic

<img width="895" height="523" alt="Snipaste_2026-03-11_21-36-41" src="https://github.com/user-attachments/assets/a15294f9-c35f-4a2a-b99a-a37072bbe631" />


## PCB


<img width="685" height="515" alt="Snipaste_2026-03-11_22-19-35" src="https://github.com/user-attachments/assets/96b823db-1e5e-4052-9c08-334d3b97b6b3" />

## 3D Model



## Assembled Board

<img width="932" height="843" alt="Snipaste_2026-03-11_22-33-47" src="https://github.com/user-attachments/assets/fe522403-476a-413f-a31b-830b27049232" />

<img width="932" height="843" alt="Snipaste_2026-03-11_22-34-20" src="https://github.com/user-attachments/assets/0c2ed6b3-4bf7-4a28-9770-e7a932b1f6f2" />

<img width="932" height="843" alt="Snipaste_2026-03-11_22-34-40" src="https://github.com/user-attachments/assets/f2683331-d87f-4d4f-85e0-13c76444b356" />


# Project Structure

```
macropad/
│
├── firmware/
│   └── code.py
│
├── hardware/
│   ├── schematic.kicad_sch
│   ├── pcb.kicad_pcb
│   └── macropad.step
│
├── images/
│   ├── schematic.png
│   ├── pcb.png
│   ├── 3d.png
│   └── board.png
│
└── README.md
```

---

# Software Setup

1. Install CircuitPython on the XIAO SAMD21
2. Copy the KMK firmware to the board
3. Upload `code.py`
4. Configure system shortcuts for F13–F17

---

# Future Improvements

* RGB underglow
* OLED animations
* Application icons
* Desktop indicator
