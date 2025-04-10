import paho.mqtt.client as mqtt

# Set up publisher
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

# Publish the "count-off" command
client.publish("stepper/control", "count-off")
print("Sent 'count-off' command")
