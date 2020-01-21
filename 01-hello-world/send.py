import pika


if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    channel = connection.channel()

    channel.queue_declare(queue="hello")

    channel.basic_publish(
        exchange="",
        routing_key="hello",
        body="Hello World! #2"
    )

    print("[x] Sent 'Hello World!")

    connection.close()


# docker run --name rabbitmq2 -p 5672:5672 rabbitmq 
