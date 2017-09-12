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

from afrl.cmasi import EntityConfiguration
from afrl.cmasi import Location3D


class RadioTowerConfiguration(EntityConfiguration.EntityConfiguration):

    def __init__(self):
        EntityConfiguration.EntityConfiguration.__init__(self)
        self.LMCP_TYPE = 3
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.Position = Location3D.Location3D()   #Location3D
        self.Range = 1500.0   #real32
        self.Enabled = True   #bool


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(EntityConfiguration.EntityConfiguration.pack(self))
        buffer.append(struct.pack("B", self.Position != None ))
        if self.Position != None:
            buffer.append(struct.pack(">q", self.Position.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Position.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Position.SERIES_VERSION))
            buffer.append(self.Position.pack())
        buffer.append(struct.pack(">f", self.Range))
        buffer.append(struct.pack(">B", self.Enabled))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = EntityConfiguration.EntityConfiguration.unpack(self, buffer, _pos)
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
            self.Position = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.Position.unpack(buffer, _pos)
        else:
            self.Position = None
        self.Range = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.Enabled = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        return _pos


    def get_Position(self):
        return self.Position

    def set_Position(self, value):
        self.Position = value 

    def get_Range(self):
        return self.Range

    def set_Range(self, value):
        self.Range = float( value )

    def get_Enabled(self):
        return self.Enabled

    def set_Enabled(self, value):
        self.Enabled = bool( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = EntityConfiguration.EntityConfiguration.toString(self)
        buf += "From RadioTowerConfiguration:\n"
        buf +=    "Position = " + str( self.Position ) + "\n" 
        buf +=    "Range = " + str( self.Range ) + "\n" 
        buf +=    "Enabled = " + str( self.Enabled ) + "\n" 

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
        str = ws + "<RadioTowerConfiguration>\n";
        #str +=EntityConfiguration.EntityConfiguration.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</RadioTowerConfiguration>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += EntityConfiguration.EntityConfiguration.toXMLMembersStr(self, ws)
        buf += ws + "<Position>\n"
        if self.Position == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Position.toXMLStr(ws + "    ") 
        buf += ws + "</Position>\n"
        buf += ws + "<Range>" + str(self.Range) + "</Range>\n"
        buf += ws + "<Enabled>" + str(self.Enabled) + "</Enabled>\n"

        return buf
        
