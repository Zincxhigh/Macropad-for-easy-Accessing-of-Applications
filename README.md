# Macropad V4

A 6-key macropad with a rotary encoder and OLED display, built around the **XIAO smd21** and powered by **KMK firmware**.
---

# Features

* 6 keys 
* Rotary encoder for volume control
* Encoder press for mute
* OLED display
* Shows **volume bar when Changing volume**
* Shows **date and time when it is doing nothing**
* **KMK firmware**

---
## BOM

* 6 × switches
* 5 × diode_SMD
* 2 x diode_THT
* 1 × EC11 rotary encoder
* 1 × OLED Conn_01x04

---
| Component             | Function         | Microcontroller Pin |
| -------------------- | ---------------- | ------------------ |
| Key 1                 | Macro key input  | D0                  |
| Key 2                 | Macro key input  | D1                  |
| Key 3                 | Macro key input  | D2                  |
| Key 4                 | Macro key input  | D3                  |
| Key 5                 | Macro key input  | D4                  |
| Key 6                 | Macro key input  | D5                  |
| Rotary Encoder A      | Encoder signal A | D6                  |
| Rotary Encoder B      | Encoder signal B | D7                  |
| Rotary Encoder Button | Push switch      | D8                  |
| OLED SDA              | Conn_01x04 Data  | SDA                 |
| OLED SCL              | Conn_01x04 Clock | SCL                 |
| VCC                   | Power            | 3.3V                |
| GND                   | Ground           | GND                 |

# Layout for board

| COL0   | COL1    | COL2            |
| ------ | ------- | --------------- |
| KiCad  | Discord | Next Desktop    |
| VSCode | Browser | Current Desktop |

Rotary Encoder:

* Rotate → Volume up/down
* Press → Mute

---

# Firmware

Firmware is written using **KMK**.
I will do debugging when parts arrive
Thanks to hackclub

# refrences

## Schematic

<img width="895" height="523" alt="Snipaste_2026-03-11_21-36-41" src="https://github.com/user-attachments/assets/a15294f9-c35f-4a2a-b99a-a37072bbe631" />


## PCB


<img src="./images/pcb-layout.png" width="750">


## #D model Board

<img width="932" height="843" alt="Snipaste_2026-03-11_22-33-47" src="https://github.com/user-attachments/assets/fe522403-476a-413f-a31b-830b27049232" />

<img width="932" height="843" alt="Snipaste_2026-03-11_22-34-20" src="https://github.com/user-attachments/assets/0c2ed6b3-4bf7-4a28-9770-e7a932b1f6f2" />

<img width="932" height="843" alt="Snipaste_2026-03-11_22-34-40" src="https://github.com/user-attachments/assets/f2683331-d87f-4d4f-85e0-13c76444b356" />


# Structure

```
macropad/
│
├── firmware/
│   └── code.py
│
├── CAD/
│   ├── schematic.kicad_sch
│   ├── pcb.kicad_pcb
│   └── macropad.step
│
├── Production/
│   ├── Top.STEP
│   ├── Bottom.STEP
│   └── gerber.zip
│ 
├── PCB/
│   ├── macropad.kicad_sch
│   ├── macropad.kicad_pcb
│   └── macropad.kicad_pro
│
└── README.md
```





