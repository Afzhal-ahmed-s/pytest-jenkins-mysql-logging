from confluent_kafka import Producer, Consumer, KafkaError


class Kafka_utility():
    def __init__(self):
        global producer
        producer = Producer({'bootstrap.servers': 'localhost:9092'})

        global consumer
        consumer = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'None', 'auto.offset.reset': 'earliest'})

        consumer.subscribe(['noduco-task'])  # Subscribe to the topic you want to consume from

    def produce_message_secondary(self, err, msg):
        if err is not None:
             print(f'Message delivery failed: {err}')
        else:
             print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    def produce_message(self, information, message):
        producer.produce('noduco-task', key='key', value=information + message, callback=self.produce_message_secondary)
        producer.flush()

    def consume_message(self):
        while True:
            msg = consumer.poll(3.0)

            if msg is None:
                print("No new message received.")
                break

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print('Reached end of partition')
                else:
                    print(f'Error while consuming message: {msg.error()}')

            else:
                print(f'Received kafka message: {msg.value().decode("utf-8")}')

        print("Closing kafka consumer.")
        consumer.close()
