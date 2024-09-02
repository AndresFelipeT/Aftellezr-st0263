import pika

def send_message(queue_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    print(f" [x] Sent '{message}' to queue {queue_name}")
    connection.close()

if __name__ == '__main__':
    send_message('file_notifications', 'New file available')
