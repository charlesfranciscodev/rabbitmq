import sys
import pika


if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="task_queue", durable=True)
    message = ' '.join(sys.argv[1:]) or "Hello World!"

    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2, # make message persistent
        )
    )

    print("[x] Sent {}".format(message))
    connection.close()


# docker run --name rabbitmq -p 5672:5672 rabbitmq 
