#!/usr/bin/env python
import pika
import sys
import pdb
import os

MESSAGE = os.environ.get("MESSAGE")
SEVERITY = os.environ.get("SEVERITY")
RABBIT_HOST = os.environ.get("RABBIT_HOST")

connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))
channel = connection.channel()

channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

channel.basic_publish(exchange="direct_logs", routing_key=SEVERITY, body=MESSAGE)

print(" [x] Sent %r:%r" % (SEVERITY, MESSAGE))
connection.close()
