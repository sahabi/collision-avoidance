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



class TaskOptionCost(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 17
        self.SERIES_NAME = "UXTASK"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149757930721443840
        self.SERIES_VERSION = 7

        #Define message fields
        self.VehicleID = 0   #int64
        self.IntialTaskID = 0   #int64
        self.IntialTaskOption = 0   #int64
        self.DestinationTaskID = 0   #int64
        self.DestinationTaskOption = 0   #int64
        self.TimeToGo = 0   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.VehicleID))
        buffer.append(struct.pack(">q", self.IntialTaskID))
        buffer.append(struct.pack(">q", self.IntialTaskOption))
        buffer.append(struct.pack(">q", self.DestinationTaskID))
        buffer.append(struct.pack(">q", self.DestinationTaskOption))
        buffer.append(struct.pack(">q", self.TimeToGo))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.VehicleID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.IntialTaskID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.IntialTaskOption = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.DestinationTaskID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.DestinationTaskOption = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.TimeToGo = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        return _pos


    def get_VehicleID(self):
        return self.VehicleID

    def set_VehicleID(self, value):
        self.VehicleID = int( value )

    def get_IntialTaskID(self):
        return self.IntialTaskID

    def set_IntialTaskID(self, value):
        self.IntialTaskID = int( value )

    def get_IntialTaskOption(self):
        return self.IntialTaskOption

    def set_IntialTaskOption(self, value):
        self.IntialTaskOption = int( value )

    def get_DestinationTaskID(self):
        return self.DestinationTaskID

    def set_DestinationTaskID(self, value):
        self.DestinationTaskID = int( value )

    def get_DestinationTaskOption(self):
        return self.DestinationTaskOption

    def set_DestinationTaskOption(self, value):
        self.DestinationTaskOption = int( value )

    def get_TimeToGo(self):
        return self.TimeToGo

    def set_TimeToGo(self, value):
        self.TimeToGo = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From TaskOptionCost:\n"
        buf +=    "VehicleID = " + str( self.VehicleID ) + "\n" 
        buf +=    "IntialTaskID = " + str( self.IntialTaskID ) + "\n" 
        buf +=    "IntialTaskOption = " + str( self.IntialTaskOption ) + "\n" 
        buf +=    "DestinationTaskID = " + str( self.DestinationTaskID ) + "\n" 
        buf +=    "DestinationTaskOption = " + str( self.DestinationTaskOption ) + "\n" 
        buf +=    "TimeToGo = " + str( self.TimeToGo ) + "\n" 

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
        str = ws + "<TaskOptionCost>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</TaskOptionCost>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<VehicleID>" + str(self.VehicleID) + "</VehicleID>\n"
        buf += ws + "<IntialTaskID>" + str(self.IntialTaskID) + "</IntialTaskID>\n"
        buf += ws + "<IntialTaskOption>" + str(self.IntialTaskOption) + "</IntialTaskOption>\n"
        buf += ws + "<DestinationTaskID>" + str(self.DestinationTaskID) + "</DestinationTaskID>\n"
        buf += ws + "<DestinationTaskOption>" + str(self.DestinationTaskOption) + "</DestinationTaskOption>\n"
        buf += ws + "<TimeToGo>" + str(self.TimeToGo) + "</TimeToGo>\n"

        return buf
        
