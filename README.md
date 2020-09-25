# CS 4287-01 Assignment 1
### How to run:
For the following, the names of the VM's are `jacob-quinnVM#` where # is the number of the VM (2 or 3)

1. Open up an ssh connnection to VM2.
2. Start up the zookeeper server on VM2. Run the following from the Kafka directory in a shell: `bin/zookeeper-server-start.sh  config/zookeeper.properties`.  
3. In new shell windows, open up another ssh connection to VM2 and one to VM3 (separate windows).
4. Start up the Kafka servers on VM2 and VM3. `bin/kafka-server-start.sh config/server.properties`. Do this from the respective kafka directories on each VM.  
5. Open another shell window on VM2. Run `bin/kafka-topics.sh --create --topic utilization1 --bootstrap-server  129.114.25.52:9092`.  
6. In the same shell after the previous command completes, also run `bin/kafka-topics.sh --create --topic utilization2 --bootstrap-server  129.114.25.52:9092`.  
7. Start up the producers on VM1.1 and VM1.2 (the local VirtualBox VM's). `python3 producer.py`  
8. Open another ssh connection to VM3 and run the consumer code. `python3 consumer.py`  
