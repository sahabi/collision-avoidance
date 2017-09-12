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


class PlanningState(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 3
        self.SERIES_NAME = "UXTASK"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149757930721443840
        self.SERIES_VERSION = 7

        #Define message fields
        self.EntityID = 0   #int64
        self.PlanningPosition = Location3D.Location3D()   #Location3D
        self.PlanningHeading = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.EntityID))
        buffer.append(struct.pack("B", self.PlanningPosition != None ))
        if self.PlanningPosition != None:
            buffer.append(struct.pack(">q", self.PlanningPosition.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.PlanningPosition.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.PlanningPosition.SERIES_VERSION))
            buffer.append(self.PlanningPosition.pack())
        buffer.append(struct.pack(">f", self.PlanningHeading))

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
            self.PlanningPosition = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.PlanningPosition.unpack(buffer, _pos)
        else:
            self.PlanningPosition = None
        self.PlanningHeading = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_EntityID(self):
        return self.EntityID

    def set_EntityID(self, value):
        self.EntityID = int( value )

    def get_PlanningPosition(self):
        return self.PlanningPosition

    def set_PlanningPosition(self, value):
        self.PlanningPosition = value 

    def get_PlanningHeading(self):
        return self.PlanningHeading

    def set_PlanningHeading(self, value):
        self.PlanningHeading = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From PlanningState:\n"
        buf +=    "EntityID = " + str( self.EntityID ) + "\n" 
        buf +=    "PlanningPosition = " + str( self.PlanningPosition ) + "\n" 
        buf +=    "PlanningHeading = " + str( self.PlanningHeading ) + "\n" 

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
        str = ws + "<PlanningState>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</PlanningState>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<EntityID>" + str(self.EntityID) + "</EntityID>\n"
        buf += ws + "<PlanningPosition>\n"
        if self.PlanningPosition == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.PlanningPosition.toXMLStr(ws + "    ") 
        buf += ws + "</PlanningPosition>\n"
        buf += ws + "<PlanningHeading>" + str(self.PlanningHeading) + "</PlanningHeading>\n"

        return buf
        
