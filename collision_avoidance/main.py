from uxas.messages.task.UniqueAutomationRequest import UniqueAutomationRequest as UAR
from lmcp import LMCPFactory
from afrl.cmasi import EntityState
from afrl.cmasi import AirVehicleState
from afrl.cmasi import AirVehicleConfiguration
from afrl.cmasi.VehicleActionCommand import VehicleActionCommand
# from afrl.cmasi import Play
from afrl.cmasi.SessionStatus import SessionStatus
from afrl.cmasi.MissionCommand import MissionCommand as MC
import socket

stateMap = {}
configMap = {}
playMap = {}
commandMap ={}
sc_time = 1

def message_received(obj):
    global stateMap
    global configMap
    global playMap
    global commandMap
    global sc_time
    if isinstance(obj ,SessionStatus):
        sc_time = obj.get_ScenarioTime()
    if isinstance(obj ,AirVehicleConfiguration.AirVehicleConfiguration):
        configMap[obj.get_ID()] = obj
    if isinstance(obj, AirVehicleState.AirVehicleState): 
        stateMap[obj.get_ID()] = obj
    if isinstance(obj, SessionStatus):
        ss = obj
    print(obj)

def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 5555)
    print("connecting to %s port %s") % (server_address)
    sock.connect(server_address)
    print("connected")
    return sock
cmd = MC()    
a = UAR()
sock = connect()
msg = LMCPFactory.LMCPFactory()
while True:
    message = msg.getObject(sock.recv(2224))
    # if isinstance(message, VehicleActionCommand):
    #     print (message.toString())
    message_received(message)
    this = LMCPFactory.packMessage(cmd, True)
    sock.send(this)
    print stateMap
