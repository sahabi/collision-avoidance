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
from afrl.impact import TaskSummary


class ImpactAutomationResponse(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 21
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.ResponseID = 0   #int64
        self.TrialResponse = AutomationResponse.AutomationResponse()   #AutomationResponse
        self.PlayID = 0   #int64
        self.SolutionID = 0   #int64
        self.Sandbox = False   #bool
        self.Summaries = []   #TaskSummary


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.ResponseID))
        buffer.append(struct.pack("B", self.TrialResponse != None ))
        if self.TrialResponse != None:
            buffer.append(struct.pack(">q", self.TrialResponse.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.TrialResponse.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.TrialResponse.SERIES_VERSION))
            buffer.append(self.TrialResponse.pack())
        buffer.append(struct.pack(">q", self.PlayID))
        buffer.append(struct.pack(">q", self.SolutionID))
        buffer.append(struct.pack(">B", self.Sandbox))
        buffer.append(struct.pack(">H", len(self.Summaries) ))
        for x in self.Summaries:
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
            self.TrialResponse = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.TrialResponse.unpack(buffer, _pos)
        else:
            self.TrialResponse = None
        self.PlayID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.SolutionID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.Sandbox = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.Summaries = [None] * _arraylen
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
                self.Summaries[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.Summaries[x].unpack(buffer, _pos)
            else:
                self.Summaries[x] = None
        return _pos


    def get_ResponseID(self):
        return self.ResponseID

    def set_ResponseID(self, value):
        self.ResponseID = int( value )

    def get_TrialResponse(self):
        return self.TrialResponse

    def set_TrialResponse(self, value):
        self.TrialResponse = value 

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

    def get_Summaries(self):
        return self.Summaries



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From ImpactAutomationResponse:\n"
        buf +=    "ResponseID = " + str( self.ResponseID ) + "\n" 
        buf +=    "TrialResponse = " + str( self.TrialResponse ) + "\n" 
        buf +=    "PlayID = " + str( self.PlayID ) + "\n" 
        buf +=    "SolutionID = " + str( self.SolutionID ) + "\n" 
        buf +=    "Sandbox = " + str( self.Sandbox ) + "\n" 
        buf +=    "Summaries = " + str( self.Summaries ) + "\n" 

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
        str = ws + "<ImpactAutomationResponse>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</ImpactAutomationResponse>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<ResponseID>" + str(self.ResponseID) + "</ResponseID>\n"
        buf += ws + "<TrialResponse>\n"
        if self.TrialResponse == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.TrialResponse.toXMLStr(ws + "    ") 
        buf += ws + "</TrialResponse>\n"
        buf += ws + "<PlayID>" + str(self.PlayID) + "</PlayID>\n"
        buf += ws + "<SolutionID>" + str(self.SolutionID) + "</SolutionID>\n"
        buf += ws + "<Sandbox>" + str(self.Sandbox) + "</Sandbox>\n"
        buf += ws + "<Summaries>\n"
        for x in self.Summaries:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</Summaries>\n"

        return buf
        
