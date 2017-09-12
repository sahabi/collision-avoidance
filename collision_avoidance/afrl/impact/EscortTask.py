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

from afrl.cmasi import SearchTask
from afrl.cmasi import Waypoint


class EscortTask(SearchTask.SearchTask):

    def __init__(self):
        SearchTask.SearchTask.__init__(self)
        self.LMCP_TYPE = 34
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.SupportedEntityID = 0   #int64
        self.RouteID = 0   #int64
        self.PrescribedWaypoints = []   #Waypoint
        self.StandoffDistance = 100   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(SearchTask.SearchTask.pack(self))
        buffer.append(struct.pack(">q", self.SupportedEntityID))
        buffer.append(struct.pack(">q", self.RouteID))
        buffer.append(struct.pack(">H", len(self.PrescribedWaypoints) ))
        for x in self.PrescribedWaypoints:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">f", self.StandoffDistance))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = SearchTask.SearchTask.unpack(self, buffer, _pos)
        self.SupportedEntityID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.RouteID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.PrescribedWaypoints = [None] * _arraylen
        _pos += 2
        for x in range(_arraylen):
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
                self.PrescribedWaypoints[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.PrescribedWaypoints[x].unpack(buffer, _pos)
            else:
                self.PrescribedWaypoints[x] = None
        self.StandoffDistance = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_SupportedEntityID(self):
        return self.SupportedEntityID

    def set_SupportedEntityID(self, value):
        self.SupportedEntityID = int( value )

    def get_RouteID(self):
        return self.RouteID

    def set_RouteID(self, value):
        self.RouteID = int( value )

    def get_PrescribedWaypoints(self):
        return self.PrescribedWaypoints

    def get_StandoffDistance(self):
        return self.StandoffDistance

    def set_StandoffDistance(self, value):
        self.StandoffDistance = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = SearchTask.SearchTask.toString(self)
        buf += "From EscortTask:\n"
        buf +=    "SupportedEntityID = " + str( self.SupportedEntityID ) + "\n" 
        buf +=    "RouteID = " + str( self.RouteID ) + "\n" 
        buf +=    "PrescribedWaypoints = " + str( self.PrescribedWaypoints ) + "\n" 
        buf +=    "StandoffDistance = " + str( self.StandoffDistance ) + "\n" 

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
        str = ws + "<EscortTask>\n";
        #str +=SearchTask.SearchTask.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</EscortTask>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += SearchTask.SearchTask.toXMLMembersStr(self, ws)
        buf += ws + "<SupportedEntityID>" + str(self.SupportedEntityID) + "</SupportedEntityID>\n"
        buf += ws + "<RouteID>" + str(self.RouteID) + "</RouteID>\n"
        buf += ws + "<PrescribedWaypoints>\n"
        for x in self.PrescribedWaypoints:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</PrescribedWaypoints>\n"
        buf += ws + "<StandoffDistance>" + str(self.StandoffDistance) + "</StandoffDistance>\n"

        return buf
        
