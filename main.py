import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    print(f'Connected with result code {reason_code}')

def on_message(client, userdata, msg):
    print(f'{msg.topic}: {msg.payload.decode()}')

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect('localhost')
mqttc.subscribe('test')

mqttc.loop_forever()
