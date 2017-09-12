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

from afrl.cmasi import PayloadState


class RadioState(PayloadState.PayloadState):

    def __init__(self):
        PayloadState.PayloadState.__init__(self)
        self.LMCP_TYPE = 4
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.Enabled = True   #bool
        self.InRange = bool(0)   #bool


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(PayloadState.PayloadState.pack(self))
        buffer.append(struct.pack(">B", self.Enabled))
        buffer.append(struct.pack(">B", self.InRange))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = PayloadState.PayloadState.unpack(self, buffer, _pos)
        self.Enabled = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        self.InRange = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        return _pos


    def get_Enabled(self):
        return self.Enabled

    def set_Enabled(self, value):
        self.Enabled = bool( value )

    def get_InRange(self):
        return self.InRange

    def set_InRange(self, value):
        self.InRange = bool( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = PayloadState.PayloadState.toString(self)
        buf += "From RadioState:\n"
        buf +=    "Enabled = " + str( self.Enabled ) + "\n" 
        buf +=    "InRange = " + str( self.InRange ) + "\n" 

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
        str = ws + "<RadioState>\n";
        #str +=PayloadState.PayloadState.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</RadioState>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += PayloadState.PayloadState.toXMLMembersStr(self, ws)
        buf += ws + "<Enabled>" + str(self.Enabled) + "</Enabled>\n"
        buf += ws + "<InRange>" + str(self.InRange) + "</InRange>\n"

        return buf
        
