import time
import paho.mqtt.client as mqtt
from adafruit_crickit import crickit
from adafruit_motor import stepper

# Setup stepper motor via Crickit HAT
STEP_MOTOR = crickit.stepper_motor
INTERSTEP_DELAY = 0.01  # delay between microsteps

# Count-off sequence: mimics a drumstick striking and returning
def count_off_pattern():
    print("Starting count-off - drumstick mimic")

    # --- Beat 1: 1/4 rotation forward (hit) + return ---
    print("Beat 1 (1/8 rotation forward, return)")
    for _ in range(25):  # Hit
        STEP_MOTOR.onestep(direction=stepper.FORWARD)
        time.sleep(INTERSTEP_DELAY)
    for _ in range(25):  # Return
        STEP_MOTOR.onestep(direction=stepper.BACKWARD)
        time.sleep(INTERSTEP_DELAY)
    time.sleep(0.4)

    # --- Beat 2: 1/8 rotation forward (hit) + return ---
    print("Beat 2 (1/8 rotation forward, return)")
    for _ in range(25):
        STEP_MOTOR.onestep(direction=stepper.FORWARD)
        time.sleep(INTERSTEP_DELAY)
    for _ in range(25):
        STEP_MOTOR.onestep(direction=stepper.BACKWARD)
        time.sleep(INTERSTEP_DELAY)
    time.sleep(0.4)

    # --- Beats 3-6: 1/16 quick hits with fast return ---
    print("Beats 3-6 (1/16 rotation forward and return, fast)")
    for beat in [1, 2, 3, 4]:
        print(f"Beat {beat + 2} (1/16 forward, return)")
        for _ in range(12):  # Small forward tap
            STEP_MOTOR.onestep(direction=stepper.FORWARD)
            time.sleep(INTERSTEP_DELAY)
        for _ in range(12):  # Return
            STEP_MOTOR.onestep(direction=stepper.BACKWARD)
            time.sleep(INTERSTEP_DELAY)
        time.sleep(0.2)

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("stepper/control")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print("Received message:", payload)

    if payload == "count-off":
        count_off_pattern()

# MQTT setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
