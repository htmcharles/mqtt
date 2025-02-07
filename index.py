import paho.mqtt.client as mqtt

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/instructor_gabriel")  # Listening for messages from the Instructor

# Callback when a message is received
def on_message(client, userdata, msg):
    print("Instructor Gabriel: " + str(msg.payload.decode()))  # Display messages from the Instructor

# MQTT Client setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("82.165.97.169", 1883, 60)

# Start the network loop
client.loop_start()

# Message sending loop
while True:
    message = input("You: ")
    client.publish("/hatuma_charles", message)  # Send message to the instructor
