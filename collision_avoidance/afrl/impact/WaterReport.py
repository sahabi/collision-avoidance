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

from afrl.cmasi import AbstractGeometry


class WaterReport(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 38
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.Area = AbstractGeometry.AbstractGeometry()   #AbstractGeometry
        self.CurrentSpeed = 0   #real32
        self.CurrentDirection = 0   #real32
        self.WaveDirection = 0   #real32
        self.WaveHeight = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack("B", self.Area != None ))
        if self.Area != None:
            buffer.append(struct.pack(">q", self.Area.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Area.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Area.SERIES_VERSION))
            buffer.append(self.Area.pack())
        buffer.append(struct.pack(">f", self.CurrentSpeed))
        buffer.append(struct.pack(">f", self.CurrentDirection))
        buffer.append(struct.pack(">f", self.WaveDirection))
        buffer.append(struct.pack(">f", self.WaveHeight))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
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
            self.Area = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.Area.unpack(buffer, _pos)
        else:
            self.Area = None
        self.CurrentSpeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.CurrentDirection = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.WaveDirection = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.WaveHeight = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_Area(self):
        return self.Area

    def set_Area(self, value):
        self.Area = value 

    def get_CurrentSpeed(self):
        return self.CurrentSpeed

    def set_CurrentSpeed(self, value):
        self.CurrentSpeed = float( value )

    def get_CurrentDirection(self):
        return self.CurrentDirection

    def set_CurrentDirection(self, value):
        self.CurrentDirection = float( value )

    def get_WaveDirection(self):
        return self.WaveDirection

    def set_WaveDirection(self, value):
        self.WaveDirection = float( value )

    def get_WaveHeight(self):
        return self.WaveHeight

    def set_WaveHeight(self, value):
        self.WaveHeight = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From WaterReport:\n"
        buf +=    "Area = " + str( self.Area ) + "\n" 
        buf +=    "CurrentSpeed = " + str( self.CurrentSpeed ) + "\n" 
        buf +=    "CurrentDirection = " + str( self.CurrentDirection ) + "\n" 
        buf +=    "WaveDirection = " + str( self.WaveDirection ) + "\n" 
        buf +=    "WaveHeight = " + str( self.WaveHeight ) + "\n" 

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
        str = ws + "<WaterReport>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</WaterReport>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<Area>\n"
        if self.Area == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Area.toXMLStr(ws + "    ") 
        buf += ws + "</Area>\n"
        buf += ws + "<CurrentSpeed>" + str(self.CurrentSpeed) + "</CurrentSpeed>\n"
        buf += ws + "<CurrentDirection>" + str(self.CurrentDirection) + "</CurrentDirection>\n"
        buf += ws + "<WaveDirection>" + str(self.WaveDirection) + "</WaveDirection>\n"
        buf += ws + "<WaveHeight>" + str(self.WaveHeight) + "</WaveHeight>\n"

        return buf
        
