from confluent_kafka import Consumer, KafkaError

consumer = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'None', 'auto.offset.reset': 'earliest'})

consumer.subscribe(['noduco-task'])  # Subscribe to the topic you want to consume from

while True:
    msg = consumer.poll(3.0)

    if msg is None:
        print("No message received.")
        # continue
        break

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print(f'Error while consuming message: {msg.error()}')

    else:
        print(f'Received message: {msg.value().decode("utf-8")}')

print("No new messages.")

consumer.close()
