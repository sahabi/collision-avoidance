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

from uxas.messages.uxnative import EntityLocation


class BandwidthTest(EntityLocation.EntityLocation):

    def __init__(self):
        EntityLocation.EntityLocation.__init__(self)
        self.LMCP_TYPE = 7
        self.SERIES_NAME = "UXNATIVE"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149751333668345413
        self.SERIES_VERSION = 3

        #Define message fields
        self.MessageID = 0   #int64
        self.Payload = ""   #string


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(EntityLocation.EntityLocation.pack(self))
        buffer.append(struct.pack(">q", self.MessageID))
        buffer.append(struct.pack(">H", len(self.Payload) ))
        if len(self.Payload) > 0:
            buffer.append(struct.pack( `len(self.Payload)` + "s", self.Payload))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = EntityLocation.EntityLocation.unpack(self, buffer, _pos)
        self.MessageID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _strlen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        if _strlen > 0:
            self.Payload = struct.unpack_from( `_strlen` + "s", buffer, _pos )[0]
            _pos += _strlen
        else:
             self.Payload = ""
        return _pos


    def get_MessageID(self):
        return self.MessageID

    def set_MessageID(self, value):
        self.MessageID = int( value )

    def get_Payload(self):
        return self.Payload

    def set_Payload(self, value):
        self.Payload = str( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = EntityLocation.EntityLocation.toString(self)
        buf += "From BandwidthTest:\n"
        buf +=    "MessageID = " + str( self.MessageID ) + "\n" 
        buf +=    "Payload = " + str( self.Payload ) + "\n" 

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
        str = ws + "<BandwidthTest>\n";
        #str +=EntityLocation.EntityLocation.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</BandwidthTest>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += EntityLocation.EntityLocation.toXMLMembersStr(self, ws)
        buf += ws + "<MessageID>" + str(self.MessageID) + "</MessageID>\n"
        buf += ws + "<Payload>" + str(self.Payload) + "</Payload>\n"

        return buf
        
