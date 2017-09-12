import sys
import zmq
from afrl.cmasi.AirVehicleState import AirVehicleState
from lmcp import LMCPFactory

port = "5560"
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect ("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)

topicfilter = ""
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
msg = LMCPFactory.LMCPFactory()

while True:
    buff = socket.recv(9000)
    print buff
    message = msg.getObject(buff)
    print message

      