from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})


def delivery_report(err, msg):
    print("two")

    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


producer.produce('noduco-task', key='key', value='I did it!', callback=delivery_report)
print("one")
producer.flush()
