# Stepper Motor Count-Off with MQTT

This project extends the Stepper Motor Hello World assignment by adding MQTT to trigger motion from an external message.

## How it works

- The Raspberry Pi listens for messages on the topic `stepper/control` using the `paho-mqtt` library.
- When it receives the message `"count-off"`, it runs a short movement pattern on the stepper motor.
- The motor mimics a drummer’s count-in — two slower hits (1, 2), then four fast taps (1, 2, 3, 4).

Each “hit” is a small forward motion and return, like a drumstick striking and bouncing off a pad.

## Why this

This setup shows how a motor can be controlled with live input using a simple message.  
It’s a playful way to connect rhythm and motion, and could be extended for other beat patterns, tempos, or sensors.

## 🎥 Demo Video

[Watch the demo](https://drive.google.com/file/d/1K3ljn8jwWorAKuQ-m9VV7T2ktBd9l5TL/view?usp=sharing)
