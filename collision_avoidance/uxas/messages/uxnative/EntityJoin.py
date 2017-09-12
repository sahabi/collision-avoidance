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



class EntityJoin(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 13
        self.SERIES_NAME = "UXNATIVE"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149751333668345413
        self.SERIES_VERSION = 3

        #Define message fields
        self.EntityID = 0   #int64
        self.Label = ""   #string


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.EntityID))
        buffer.append(struct.pack(">H", len(self.Label) ))
        if len(self.Label) > 0:
            buffer.append(struct.pack( `len(self.Label)` + "s", self.Label))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.EntityID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _strlen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        if _strlen > 0:
            self.Label = struct.unpack_from( `_strlen` + "s", buffer, _pos )[0]
            _pos += _strlen
        else:
             self.Label = ""
        return _pos


    def get_EntityID(self):
        return self.EntityID

    def set_EntityID(self, value):
        self.EntityID = int( value )

    def get_Label(self):
        return self.Label

    def set_Label(self, value):
        self.Label = str( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From EntityJoin:\n"
        buf +=    "EntityID = " + str( self.EntityID ) + "\n" 
        buf +=    "Label = " + str( self.Label ) + "\n" 

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
        str = ws + "<EntityJoin>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</EntityJoin>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<EntityID>" + str(self.EntityID) + "</EntityID>\n"
        buf += ws + "<Label>" + str(self.Label) + "</Label>\n"

        return buf
        
