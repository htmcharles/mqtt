import paho.mqtt.client as mqtt

# Define tester's topic
tester_topic = "/hatuma_charles"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribe to tester's topic to receive chatbot replies
    client.subscribe(tester_topic)
    print(f"📩 Listening for replies on {tester_topic}")

def on_message(client, userdata, msg):
    print(f"\n🤖 Instructor (bot): {msg.payload.decode()}")  # Display chatbot's response

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("82.165.97.169", 1883, 60)

# Start the network loop
client.loop_start()

while True:
    message = input("You: ")

    # Publish in the format "sender_topic: message"
    formatted_message = f"hatuma_charles: {message}"
    client.publish("/instructor_gabriel", formatted_message)  # Send message to instructor_gabriel
