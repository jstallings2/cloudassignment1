#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, demonstrate Kafka streaming API to build a consumer.
#

import os   # need this for popen
import time # for sleep
import json
from kafka import KafkaConsumer  # consumer of events
import couchdb

# Set up server/db
couch = couchdb.Server()

db = couch.create('assignment1')

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the consumer
# (you will need to change this to your bootstrap server's IP addr)
consumer = KafkaConsumer (bootstrap_servers="192.168.15.3:9092")

# subscribe to topic
consumer.subscribe (topics=["utilizations"])

# we keep reading and printing
for msg in consumer:
    # what we get is a record. From this record, we are interested in printing
    # the contents of the value field. We are sure that we get only the
    # utilizations topic because that is the only topic we subscribed to.
    # Otherwise we will need to demultiplex the incoming data according to the
    # topic coming in.
    #
    # convert the value field into string (ASCII)

    # message = str(msg.value, 'ascii')

    # message is now a json serialized representation
    # go from json to database

    # json to python dict
    doc = json.loads(msg)

    # dump doc into db
    db.save(doc)

    

# we are done. As such, we are not going to get here as the above loop
# is a forever loop.
consumer.close ()
