import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

def receive_message(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(f" [*] Waiting for messages in {queue_name}. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == '__main__':
    receive_message('file_notifications')
