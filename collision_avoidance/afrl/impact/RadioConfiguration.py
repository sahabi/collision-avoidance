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
from afrl.cmasi import Location3D


class RadioConfiguration(PayloadConfiguration.PayloadConfiguration):

    def __init__(self):
        PayloadConfiguration.PayloadConfiguration.__init__(self)
        self.LMCP_TYPE = 2
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.Range = 1500.0   #real32
        self.RallyPoint = None   #Location3D
        self.Timeout = 120000   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(PayloadConfiguration.PayloadConfiguration.pack(self))
        buffer.append(struct.pack(">f", self.Range))
        buffer.append(struct.pack("B", self.RallyPoint != None ))
        if self.RallyPoint != None:
            buffer.append(struct.pack(">q", self.RallyPoint.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.RallyPoint.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.RallyPoint.SERIES_VERSION))
            buffer.append(self.RallyPoint.pack())
        buffer.append(struct.pack(">q", self.Timeout))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = PayloadConfiguration.PayloadConfiguration.unpack(self, buffer, _pos)
        self.Range = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
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
            self.RallyPoint = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.RallyPoint.unpack(buffer, _pos)
        else:
            self.RallyPoint = None
        self.Timeout = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        return _pos


    def get_Range(self):
        return self.Range

    def set_Range(self, value):
        self.Range = float( value )

    def get_RallyPoint(self):
        return self.RallyPoint

    def set_RallyPoint(self, value):
        self.RallyPoint = value 

    def get_Timeout(self):
        return self.Timeout

    def set_Timeout(self, value):
        self.Timeout = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = PayloadConfiguration.PayloadConfiguration.toString(self)
        buf += "From RadioConfiguration:\n"
        buf +=    "Range = " + str( self.Range ) + "\n" 
        buf +=    "RallyPoint = " + str( self.RallyPoint ) + "\n" 
        buf +=    "Timeout = " + str( self.Timeout ) + "\n" 

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
        str = ws + "<RadioConfiguration>\n";
        #str +=PayloadConfiguration.PayloadConfiguration.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</RadioConfiguration>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += PayloadConfiguration.PayloadConfiguration.toXMLMembersStr(self, ws)
        buf += ws + "<Range>" + str(self.Range) + "</Range>\n"
        buf += ws + "<RallyPoint>\n"
        if self.RallyPoint == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.RallyPoint.toXMLStr(ws + "    ") 
        buf += ws + "</RallyPoint>\n"
        buf += ws + "<Timeout>" + str(self.Timeout) + "</Timeout>\n"

        return buf
        
