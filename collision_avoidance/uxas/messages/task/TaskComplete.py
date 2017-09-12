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



class TaskComplete(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 28
        self.SERIES_NAME = "UXTASK"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149757930721443840
        self.SERIES_VERSION = 7

        #Define message fields
        self.TaskID = 0   #int64
        self.EntitiesInvolved = []   #int64
        self.TimeTaskCompleted = 0   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.TaskID))
        buffer.append(struct.pack(">H", len(self.EntitiesInvolved) ))
        for x in self.EntitiesInvolved:
            buffer.append(struct.pack(">q", x ))
        buffer.append(struct.pack(">q", self.TimeTaskCompleted))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.TaskID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.EntitiesInvolved = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.EntitiesInvolved = struct.unpack_from(">" + `_arraylen` + "q", buffer, _pos )
            _pos += 8 * _arraylen
        self.TimeTaskCompleted = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        return _pos


    def get_TaskID(self):
        return self.TaskID

    def set_TaskID(self, value):
        self.TaskID = int( value )

    def get_EntitiesInvolved(self):
        return self.EntitiesInvolved

    def get_TimeTaskCompleted(self):
        return self.TimeTaskCompleted

    def set_TimeTaskCompleted(self, value):
        self.TimeTaskCompleted = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From TaskComplete:\n"
        buf +=    "TaskID = " + str( self.TaskID ) + "\n" 
        buf +=    "EntitiesInvolved = " + str( self.EntitiesInvolved ) + "\n" 
        buf +=    "TimeTaskCompleted = " + str( self.TimeTaskCompleted ) + "\n" 

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
        str = ws + "<TaskComplete>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</TaskComplete>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<TaskID>" + str(self.TaskID) + "</TaskID>\n"
        buf += ws + "<EntitiesInvolved>\n"
        for x in self.EntitiesInvolved:
            buf += ws + "<int64>" + str(x) + "</int64>\n"
        buf += ws + "</EntitiesInvolved>\n"
        buf += ws + "<TimeTaskCompleted>" + str(self.TimeTaskCompleted) + "</TimeTaskCompleted>\n"

        return buf
        
