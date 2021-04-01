#!/usr/bin/env python
import pika
import sys
import os
import pdb

MESSAGE = os.environ.get("MESSAGE")
SEVERITY = os.environ.get("SEVERITY")

pdb.set_trace()

connection = pika.BlockingConnection(pika.ConnectionParameters(host="0.0.0.0"))
channel = connection.channel()

channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

channel.basic_publish(exchange="direct_logs", routing_key=SEVERITY, body=MESSAGE)

print(" [x] Sent %r:%r" % (SEVERITY, MESSAGE))
connection.close()
