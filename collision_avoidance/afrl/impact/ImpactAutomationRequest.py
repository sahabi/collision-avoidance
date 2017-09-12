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

from afrl.cmasi import AutomationRequest
from afrl.impact import SpeedAltPair


class ImpactAutomationRequest(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 20
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.RequestID = 0   #int64
        self.TrialRequest = AutomationRequest.AutomationRequest()   #AutomationRequest
        self.OverridePlanningConditions = []   #SpeedAltPair
        self.PlayID = 0   #int64
        self.SolutionID = 0   #int64
        self.Sandbox = False   #bool


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.RequestID))
        buffer.append(struct.pack("B", self.TrialRequest != None ))
        if self.TrialRequest != None:
            buffer.append(struct.pack(">q", self.TrialRequest.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.TrialRequest.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.TrialRequest.SERIES_VERSION))
            buffer.append(self.TrialRequest.pack())
        buffer.append(struct.pack(">H", len(self.OverridePlanningConditions) ))
        for x in self.OverridePlanningConditions:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">q", self.PlayID))
        buffer.append(struct.pack(">q", self.SolutionID))
        buffer.append(struct.pack(">B", self.Sandbox))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.RequestID = struct.unpack_from(">q", buffer, _pos)[0]
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
            self.TrialRequest = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.TrialRequest.unpack(buffer, _pos)
        else:
            self.TrialRequest = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.OverridePlanningConditions = [None] * _arraylen
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
                self.OverridePlanningConditions[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.OverridePlanningConditions[x].unpack(buffer, _pos)
            else:
                self.OverridePlanningConditions[x] = None
        self.PlayID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.SolutionID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.Sandbox = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        return _pos


    def get_RequestID(self):
        return self.RequestID

    def set_RequestID(self, value):
        self.RequestID = int( value )

    def get_TrialRequest(self):
        return self.TrialRequest

    def set_TrialRequest(self, value):
        self.TrialRequest = value 

    def get_OverridePlanningConditions(self):
        return self.OverridePlanningConditions

    def get_PlayID(self):
        return self.PlayID

    def set_PlayID(self, value):
        self.PlayID = int( value )

    def get_SolutionID(self):
        return self.SolutionID

    def set_SolutionID(self, value):
        self.SolutionID = int( value )

    def get_Sandbox(self):
        return self.Sandbox

    def set_Sandbox(self, value):
        self.Sandbox = bool( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From ImpactAutomationRequest:\n"
        buf +=    "RequestID = " + str( self.RequestID ) + "\n" 
        buf +=    "TrialRequest = " + str( self.TrialRequest ) + "\n" 
        buf +=    "OverridePlanningConditions = " + str( self.OverridePlanningConditions ) + "\n" 
        buf +=    "PlayID = " + str( self.PlayID ) + "\n" 
        buf +=    "SolutionID = " + str( self.SolutionID ) + "\n" 
        buf +=    "Sandbox = " + str( self.Sandbox ) + "\n" 

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
        str = ws + "<ImpactAutomationRequest>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</ImpactAutomationRequest>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<RequestID>" + str(self.RequestID) + "</RequestID>\n"
        buf += ws + "<TrialRequest>\n"
        if self.TrialRequest == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.TrialRequest.toXMLStr(ws + "    ") 
        buf += ws + "</TrialRequest>\n"
        buf += ws + "<OverridePlanningConditions>\n"
        for x in self.OverridePlanningConditions:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</OverridePlanningConditions>\n"
        buf += ws + "<PlayID>" + str(self.PlayID) + "</PlayID>\n"
        buf += ws + "<SolutionID>" + str(self.SolutionID) + "</SolutionID>\n"
        buf += ws + "<Sandbox>" + str(self.Sandbox) + "</Sandbox>\n"

        return buf
        
