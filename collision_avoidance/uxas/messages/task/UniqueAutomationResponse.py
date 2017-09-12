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

from afrl.cmasi import AutomationResponse
from uxas.messages.task import PlanningState


class UniqueAutomationResponse(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 9
        self.SERIES_NAME = "UXTASK"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149757930721443840
        self.SERIES_VERSION = 7

        #Define message fields
        self.ResponseID = 0   #int64
        self.OriginalResponse = AutomationResponse.AutomationResponse()   #AutomationResponse
        self.FinalStates = []   #PlanningState


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.ResponseID))
        buffer.append(struct.pack("B", self.OriginalResponse != None ))
        if self.OriginalResponse != None:
            buffer.append(struct.pack(">q", self.OriginalResponse.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.OriginalResponse.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.OriginalResponse.SERIES_VERSION))
            buffer.append(self.OriginalResponse.pack())
        buffer.append(struct.pack(">H", len(self.FinalStates) ))
        for x in self.FinalStates:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.ResponseID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _valid = struct.unpack_from("B", buffer, _pos )[0]
        _pos += 1
        if _valid:
            _series = struct.unpack_from(">q", buffer, _pos)[0]
            _pos += 8
            _type = struct.unpack_from(">I", buffer, _pos)[0]
            _pos += 4
            _version = struct.unpack_from(">H", buffer, _pos)[0]
            _pos += 2
            from lmcp import LMCPFactory
            self.OriginalResponse = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.OriginalResponse.unpack(buffer, _pos)
        else:
            self.OriginalResponse = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.FinalStates = [None] * _arraylen
        _pos += 2
        for x in range(_arraylen):
            _valid = struct.unpack_from("B", buffer, _pos )[0]
            _pos += 1
            if _valid:
                _series = struct.unpack_from(">q", buffer, _pos)[0]
                _pos += 8
                _type = struct.unpack_from(">I", buffer, _pos)[0]
                _pos += 4
                _version = struct.unpack_from(">H", buffer, _pos)[0]
                _pos += 2
                from lmcp import LMCPFactory
                self.FinalStates[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.FinalStates[x].unpack(buffer, _pos)
            else:
                self.FinalStates[x] = None
        return _pos


    def get_ResponseID(self):
        return self.ResponseID

    def set_ResponseID(self, value):
        self.ResponseID = int( value )

    def get_OriginalResponse(self):
        return self.OriginalResponse

    def set_OriginalResponse(self, value):
        self.OriginalResponse = value 

    def get_FinalStates(self):
        return self.FinalStates



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From UniqueAutomationResponse:\n"
        buf +=    "ResponseID = " + str( self.ResponseID ) + "\n" 
        buf +=    "OriginalResponse = " + str( self.OriginalResponse ) + "\n" 
        buf +=    "FinalStates = " + str( self.FinalStates ) + "\n" 

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
        str = ws + "<UniqueAutomationResponse>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</UniqueAutomationResponse>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<ResponseID>" + str(self.ResponseID) + "</ResponseID>\n"
        buf += ws + "<OriginalResponse>\n"
        if self.OriginalResponse == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.OriginalResponse.toXMLStr(ws + "    ") 
        buf += ws + "</OriginalResponse>\n"
        buf += ws + "<FinalStates>\n"
        for x in self.FinalStates:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</FinalStates>\n"

        return buf
        
