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


class GraphNode(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 1
        self.SERIES_NAME = "ROUTE"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5931053054693474304
        self.SERIES_VERSION = 3

        #Define message fields
        self.NodeID = 0   #int64
        self.Coordinates = Location3D.Location3D()   #Location3D
        self.AssociatedEdges = []   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.NodeID))
        buffer.append(struct.pack("B", self.Coordinates != None ))
        if self.Coordinates != None:
            buffer.append(struct.pack(">q", self.Coordinates.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Coordinates.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Coordinates.SERIES_VERSION))
            buffer.append(self.Coordinates.pack())
        buffer.append(struct.pack(">H", len(self.AssociatedEdges) ))
        for x in self.AssociatedEdges:
            buffer.append(struct.pack(">q", x ))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.NodeID = struct.unpack_from(">q", buffer, _pos)[0]
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
            self.Coordinates = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.Coordinates.unpack(buffer, _pos)
        else:
            self.Coordinates = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.AssociatedEdges = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.AssociatedEdges = struct.unpack_from(">" + `_arraylen` + "q", buffer, _pos )
            _pos += 8 * _arraylen
        return _pos


    def get_NodeID(self):
        return self.NodeID

    def set_NodeID(self, value):
        self.NodeID = int( value )

    def get_Coordinates(self):
        return self.Coordinates

    def set_Coordinates(self, value):
        self.Coordinates = value 

    def get_AssociatedEdges(self):
        return self.AssociatedEdges



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From GraphNode:\n"
        buf +=    "NodeID = " + str( self.NodeID ) + "\n" 
        buf +=    "Coordinates = " + str( self.Coordinates ) + "\n" 
        buf +=    "AssociatedEdges = " + str( self.AssociatedEdges ) + "\n" 

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
        str = ws + "<GraphNode>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</GraphNode>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<NodeID>" + str(self.NodeID) + "</NodeID>\n"
        buf += ws + "<Coordinates>\n"
        if self.Coordinates == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Coordinates.toXMLStr(ws + "    ") 
        buf += ws + "</Coordinates>\n"
        buf += ws + "<AssociatedEdges>\n"
        for x in self.AssociatedEdges:
            buf += ws + "<int64>" + str(x) + "</int64>\n"
        buf += ws + "</AssociatedEdges>\n"

        return buf
        
