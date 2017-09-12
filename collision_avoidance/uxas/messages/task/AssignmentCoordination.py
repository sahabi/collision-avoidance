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

from uxas.messages.task import PlanningState


class AssignmentCoordination(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 4
        self.SERIES_NAME = "UXTASK"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149757930721443840
        self.SERIES_VERSION = 7

        #Define message fields
        self.CoordinatedAutomationRequestID = 0   #int64
        self.PlanningState = PlanningState.PlanningState()   #PlanningState


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.CoordinatedAutomationRequestID))
        buffer.append(struct.pack("B", self.PlanningState != None ))
        if self.PlanningState != None:
            buffer.append(struct.pack(">q", self.PlanningState.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.PlanningState.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.PlanningState.SERIES_VERSION))
            buffer.append(self.PlanningState.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.CoordinatedAutomationRequestID = struct.unpack_from(">q", buffer, _pos)[0]
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
            self.PlanningState = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.PlanningState.unpack(buffer, _pos)
        else:
            self.PlanningState = None
        return _pos


    def get_CoordinatedAutomationRequestID(self):
        return self.CoordinatedAutomationRequestID

    def set_CoordinatedAutomationRequestID(self, value):
        self.CoordinatedAutomationRequestID = int( value )

    def get_PlanningState(self):
        return self.PlanningState

    def set_PlanningState(self, value):
        self.PlanningState = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From AssignmentCoordination:\n"
        buf +=    "CoordinatedAutomationRequestID = " + str( self.CoordinatedAutomationRequestID ) + "\n" 
        buf +=    "PlanningState = " + str( self.PlanningState ) + "\n" 

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
        str = ws + "<AssignmentCoordination>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</AssignmentCoordination>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<CoordinatedAutomationRequestID>" + str(self.CoordinatedAutomationRequestID) + "</CoordinatedAutomationRequestID>\n"
        buf += ws + "<PlanningState>\n"
        if self.PlanningState == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.PlanningState.toXMLStr(ws + "    ") 
        buf += ws + "</PlanningState>\n"

        return buf
        
