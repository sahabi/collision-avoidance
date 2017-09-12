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

from afrl.cmasi import Location3D


class EntityLocation(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 6
        self.SERIES_NAME = "UXNATIVE"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149751333668345413
        self.SERIES_VERSION = 3

        #Define message fields
        self.EntityID = 0   #int64
        self.Position = Location3D.Location3D()   #Location3D
        self.Time = 0   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.EntityID))
        buffer.append(struct.pack("B", self.Position != None ))
        if self.Position != None:
            buffer.append(struct.pack(">q", self.Position.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Position.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Position.SERIES_VERSION))
            buffer.append(self.Position.pack())
        buffer.append(struct.pack(">q", self.Time))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.EntityID = struct.unpack_from(">q", buffer, _pos)[0]
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
            self.Position = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.Position.unpack(buffer, _pos)
        else:
            self.Position = None
        self.Time = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        return _pos


    def get_EntityID(self):
        return self.EntityID

    def set_EntityID(self, value):
        self.EntityID = int( value )

    def get_Position(self):
        return self.Position

    def set_Position(self, value):
        self.Position = value 

    def get_Time(self):
        return self.Time

    def set_Time(self, value):
        self.Time = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From EntityLocation:\n"
        buf +=    "EntityID = " + str( self.EntityID ) + "\n" 
        buf +=    "Position = " + str( self.Position ) + "\n" 
        buf +=    "Time = " + str( self.Time ) + "\n" 

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
        str = ws + "<EntityLocation>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</EntityLocation>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<EntityID>" + str(self.EntityID) + "</EntityID>\n"
        buf += ws + "<Position>\n"
        if self.Position == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Position.toXMLStr(ws + "    ") 
        buf += ws + "</Position>\n"
        buf += ws + "<Time>" + str(self.Time) + "</Time>\n"

        return buf
        
