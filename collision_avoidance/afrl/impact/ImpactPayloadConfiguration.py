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

from afrl.cmasi import PayloadConfiguration
from afrl.impact import ImpactPayloadType


class ImpactPayloadConfiguration(PayloadConfiguration.PayloadConfiguration):

    def __init__(self):
        PayloadConfiguration.PayloadConfiguration.__init__(self)
        self.LMCP_TYPE = 6
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.AvailablePayloads = []   #ImpactPayloadType


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(PayloadConfiguration.PayloadConfiguration.pack(self))
        buffer.append(struct.pack(">H", len(self.AvailablePayloads) ))
        for x in self.AvailablePayloads:
            buffer.append(struct.pack(">i", x ))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = PayloadConfiguration.PayloadConfiguration.unpack(self, buffer, _pos)
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.AvailablePayloads = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.AvailablePayloads = struct.unpack_from(">" + `_arraylen` + "i", buffer, _pos )
            _pos += 4 * _arraylen
        return _pos


    def get_AvailablePayloads(self):
        return self.AvailablePayloads



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = PayloadConfiguration.PayloadConfiguration.toString(self)
        buf += "From ImpactPayloadConfiguration:\n"
        buf +=    "AvailablePayloads = " + str( self.AvailablePayloads ) + "\n" 

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
        str = ws + "<ImpactPayloadConfiguration>\n";
        #str +=PayloadConfiguration.PayloadConfiguration.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</ImpactPayloadConfiguration>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += PayloadConfiguration.PayloadConfiguration.toXMLMembersStr(self, ws)
        buf += ws + "<AvailablePayloads>\n"
        for x in self.AvailablePayloads:
            buf += ws + "<ImpactPayloadType>" + ImpactPayloadType.get_ImpactPayloadType_int(x) + "</ImpactPayloadType>\n"
        buf += ws + "</AvailablePayloads>\n"

        return buf
        
