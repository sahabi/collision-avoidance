import sys
import zmq
from lmcp import LMCPFactory
from afrl.cmasi.VehicleActionCommand import VehicleActionCommand

port = "5555"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print( "Collecting updates from weather server...")
socket.connect ("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)

# Subscribe to zipcode, default is NYC, 10001
topicfilter = ""
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
msg = LMCPFactory.LMCPFactory()
# Process 5 updates
total_value = 0
for update_nbr in range (500):
    string = socket.recv()
    obj = msg.getObject(string)
    if isinstance(obj, VehicleActionCommand):
        print (obj.toString())
    # if isinstance(obj ,SessionStatus):
    # print string

print ("Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr))
      