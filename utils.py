import psycopg2
from confluent_kafka import Producer

message_delivered = False

def kafka_delivery_report(err, msg):
    global message_delivered
    message_delivered = False
    if err is not None:
        print('\nMessage delivery failed: {}'.format(err))
    else:
        print('\nMessage delivered to {} [{}]'.format(msg.topic(), msg.partition()))
        message_delivered = True

def is_message_delivered():
    return message_delivered

def create_producer(broker):
    producer_config = {
        'bootstrap.servers': broker
    }
    return Producer(producer_config)

def publish_message(producer, topic, message):
    try:
        while True:
            producer.produce(topic, key=None, value=message, callback=kafka_delivery_report)
            producer.flush()

            if is_message_delivered():
                break

    except KeyboardInterrupt:
        pass

def close_producer(producer):
    producer.flush()
    del producer

def connect_to_database(host, user, password, database_name):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )
        print("\nConnected to the database successfully!")
    except psycopg2.Error as e:
        print(f"\nError: {e}")
        exit()
    
    return connection

def fetch_one_row(cursor, query):
    cursor.execute(query)
    return cursor.fetchone()[0]
