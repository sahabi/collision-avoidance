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



class BatchSummaryRequest(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 12
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.RequestID = 0   #int64
        self.Vehicles = []   #int64
        self.TaskList = []   #int64
        self.InterTaskPercentage = []   #real32
        self.OperatingRegion = 0   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.RequestID))
        buffer.append(struct.pack(">H", len(self.Vehicles) ))
        for x in self.Vehicles:
            buffer.append(struct.pack(">q", x ))
        buffer.append(struct.pack(">H", len(self.TaskList) ))
        for x in self.TaskList:
            buffer.append(struct.pack(">q", x ))
        buffer.append(struct.pack(">H", len(self.InterTaskPercentage) ))
        for x in self.InterTaskPercentage:
            buffer.append(struct.pack(">f", x ))
        buffer.append(struct.pack(">q", self.OperatingRegion))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.RequestID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.Vehicles = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.Vehicles = struct.unpack_from(">" + `_arraylen` + "q", buffer, _pos )
            _pos += 8 * _arraylen
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.TaskList = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.TaskList = struct.unpack_from(">" + `_arraylen` + "q", buffer, _pos )
            _pos += 8 * _arraylen
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.InterTaskPercentage = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.InterTaskPercentage = struct.unpack_from(">" + `_arraylen` + "f", buffer, _pos )
            _pos += 4 * _arraylen
        self.OperatingRegion = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        return _pos


    def get_RequestID(self):
        return self.RequestID

    def set_RequestID(self, value):
        self.RequestID = int( value )

    def get_Vehicles(self):
        return self.Vehicles

    def get_TaskList(self):
        return self.TaskList

    def get_InterTaskPercentage(self):
        return self.InterTaskPercentage

    def get_OperatingRegion(self):
        return self.OperatingRegion

    def set_OperatingRegion(self, value):
        self.OperatingRegion = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From BatchSummaryRequest:\n"
        buf +=    "RequestID = " + str( self.RequestID ) + "\n" 
        buf +=    "Vehicles = " + str( self.Vehicles ) + "\n" 
        buf +=    "TaskList = " + str( self.TaskList ) + "\n" 
        buf +=    "InterTaskPercentage = " + str( self.InterTaskPercentage ) + "\n" 
        buf +=    "OperatingRegion = " + str( self.OperatingRegion ) + "\n" 

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
        str = ws + "<BatchSummaryRequest>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</BatchSummaryRequest>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<RequestID>" + str(self.RequestID) + "</RequestID>\n"
        buf += ws + "<Vehicles>\n"
        for x in self.Vehicles:
            buf += ws + "<int64>" + str(x) + "</int64>\n"
        buf += ws + "</Vehicles>\n"
        buf += ws + "<TaskList>\n"
        for x in self.TaskList:
            buf += ws + "<int64>" + str(x) + "</int64>\n"
        buf += ws + "</TaskList>\n"
        buf += ws + "<InterTaskPercentage>\n"
        for x in self.InterTaskPercentage:
            buf += ws + "<real32>" + str(x) + "</real32>\n"
        buf += ws + "</InterTaskPercentage>\n"
        buf += ws + "<OperatingRegion>" + str(self.OperatingRegion) + "</OperatingRegion>\n"

        return buf
        
