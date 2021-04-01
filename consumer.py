#!/usr/bin/env python
import pika
import sys
import os

SEVERITY = os.environ.get("SEVERITY")
RABBIT_HOST = os.environ.get("RABBIT_HOST")
print(SEVERITY)

connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))
channel = connection.channel()
channel.exchange_declare(exchange="direct_logs", exchange_type="direct")
result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
if not SEVERITY:
    sys.exit(1)

if SEVERITY:
    severities = SEVERITY.split(",")
    for severity in severities:
        print(severity)
        channel.queue_bind(
            exchange="direct_logs", queue=queue_name, routing_key=severity
        )

print(" [*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
connection.close()
