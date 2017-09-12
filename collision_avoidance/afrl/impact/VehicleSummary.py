#! /usr/bin/python

import struct
from lmcp import LMCPObject

## ===============================================================================
## Authors: AFRL/RQQA
## Organization: Air Force Research Laboratory, Aerospace Systems Directorate, Power and Control Division
## 
## Copyright (c) 2017 Government of the United State of America, as represented by
## the Secretary of the Air Force.  No copyright is claimed in the United States under
## Title 17, U.S. Code.  All Other Rights Reserved.
## ===============================================================================

## This file was auto-created by LmcpGen. Modifications will be overwritten.



class VehicleSummary(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 15
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.VehicleID = 0   #int64
        self.DestinationTaskID = 0   #int64
        self.InitialTaskID = 0   #int64
        self.InitialTaskPercentage = 0   #real32
        self.EstimateTimeToTaskPercentage = 0   #int64
        self.TimeToArrive = 0   #int64
        self.TimeOnTask = 0   #int64
        self.EnergyRemaining = 0   #real32
        self.BeyondCommRange = False   #bool


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.VehicleID))
        buffer.append(struct.pack(">q", self.DestinationTaskID))
        buffer.append(struct.pack(">q", self.InitialTaskID))
        buffer.append(struct.pack(">f", self.InitialTaskPercentage))
        buffer.append(struct.pack(">q", self.EstimateTimeToTaskPercentage))
        buffer.append(struct.pack(">q", self.TimeToArrive))
        buffer.append(struct.pack(">q", self.TimeOnTask))
        buffer.append(struct.pack(">f", self.EnergyRemaining))
        buffer.append(struct.pack(">B", self.BeyondCommRange))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.VehicleID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.DestinationTaskID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.InitialTaskID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.InitialTaskPercentage = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.EstimateTimeToTaskPercentage = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.TimeToArrive = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.TimeOnTask = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.EnergyRemaining = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.BeyondCommRange = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        return _pos


    def get_VehicleID(self):
        return self.VehicleID

    def set_VehicleID(self, value):
        self.VehicleID = int( value )

    def get_DestinationTaskID(self):
        return self.DestinationTaskID

    def set_DestinationTaskID(self, value):
        self.DestinationTaskID = int( value )

    def get_InitialTaskID(self):
        return self.InitialTaskID

    def set_InitialTaskID(self, value):
        self.InitialTaskID = int( value )

    def get_InitialTaskPercentage(self):
        return self.InitialTaskPercentage

    def set_InitialTaskPercentage(self, value):
        self.InitialTaskPercentage = float( value )

    def get_EstimateTimeToTaskPercentage(self):
        return self.EstimateTimeToTaskPercentage

    def set_EstimateTimeToTaskPercentage(self, value):
        self.EstimateTimeToTaskPercentage = int( value )

    def get_TimeToArrive(self):
        return self.TimeToArrive

    def set_TimeToArrive(self, value):
        self.TimeToArrive = int( value )

    def get_TimeOnTask(self):
        return self.TimeOnTask

    def set_TimeOnTask(self, value):
        self.TimeOnTask = int( value )

    def get_EnergyRemaining(self):
        return self.EnergyRemaining

    def set_EnergyRemaining(self, value):
        self.EnergyRemaining = float( value )

    def get_BeyondCommRange(self):
        return self.BeyondCommRange

    def set_BeyondCommRange(self, value):
        self.BeyondCommRange = bool( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From VehicleSummary:\n"
        buf +=    "VehicleID = " + str( self.VehicleID ) + "\n" 
        buf +=    "DestinationTaskID = " + str( self.DestinationTaskID ) + "\n" 
        buf +=    "InitialTaskID = " + str( self.InitialTaskID ) + "\n" 
        buf +=    "InitialTaskPercentage = " + str( self.InitialTaskPercentage ) + "\n" 
        buf +=    "EstimateTimeToTaskPercentage = " + str( self.EstimateTimeToTaskPercentage ) + "\n" 
        buf +=    "TimeToArrive = " + str( self.TimeToArrive ) + "\n" 
        buf +=    "TimeOnTask = " + str( self.TimeOnTask ) + "\n" 
        buf +=    "EnergyRemaining = " + str( self.EnergyRemaining ) + "\n" 
        buf +=    "BeyondCommRange = " + str( self.BeyondCommRange ) + "\n" 

        return buf;

    def getLMCPType(self):
        return self.LMCP_TYPE

    def getSeriesName(self):
        return self.SERIES_NAME

    def getSeriesNameID(self):
        return self.SERIES_NAME_ID

    def getSeriesVersion(self):
        return self.SERIES_VERSION

    def toXMLStr(self, ws):
        str = ws + "<VehicleSummary>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</VehicleSummary>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<VehicleID>" + str(self.VehicleID) + "</VehicleID>\n"
        buf += ws + "<DestinationTaskID>" + str(self.DestinationTaskID) + "</DestinationTaskID>\n"
        buf += ws + "<InitialTaskID>" + str(self.InitialTaskID) + "</InitialTaskID>\n"
        buf += ws + "<InitialTaskPercentage>" + str(self.InitialTaskPercentage) + "</InitialTaskPercentage>\n"
        buf += ws + "<EstimateTimeToTaskPercentage>" + str(self.EstimateTimeToTaskPercentage) + "</EstimateTimeToTaskPercentage>\n"
        buf += ws + "<TimeToArrive>" + str(self.TimeToArrive) + "</TimeToArrive>\n"
        buf += ws + "<TimeOnTask>" + str(self.TimeOnTask) + "</TimeOnTask>\n"
        buf += ws + "<EnergyRemaining>" + str(self.EnergyRemaining) + "</EnergyRemaining>\n"
        buf += ws + "<BeyondCommRange>" + str(self.BeyondCommRange) + "</BeyondCommRange>\n"

        return buf
        
