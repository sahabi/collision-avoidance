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


class MultiVehicleWatchTask(SearchTask.SearchTask):

    def __init__(self):
        SearchTask.SearchTask.__init__(self)
        self.LMCP_TYPE = 30
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.WatchedEntityID = 0   #int64
        self.NumberVehicles = 1   #byte


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(SearchTask.SearchTask.pack(self))
        buffer.append(struct.pack(">q", self.WatchedEntityID))
        buffer.append(struct.pack(">B", self.NumberVehicles))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = SearchTask.SearchTask.unpack(self, buffer, _pos)
        self.WatchedEntityID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.NumberVehicles = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        return _pos


    def get_WatchedEntityID(self):
        return self.WatchedEntityID

    def set_WatchedEntityID(self, value):
        self.WatchedEntityID = int( value )

    def get_NumberVehicles(self):
        return self.NumberVehicles

    def set_NumberVehicles(self, value):
        self.NumberVehicles = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = SearchTask.SearchTask.toString(self)
        buf += "From MultiVehicleWatchTask:\n"
        buf +=    "WatchedEntityID = " + str( self.WatchedEntityID ) + "\n" 
        buf +=    "NumberVehicles = " + str( self.NumberVehicles ) + "\n" 

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
        str = ws + "<MultiVehicleWatchTask>\n";
        #str +=SearchTask.SearchTask.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</MultiVehicleWatchTask>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += SearchTask.SearchTask.toXMLMembersStr(self, ws)
        buf += ws + "<WatchedEntityID>" + str(self.WatchedEntityID) + "</WatchedEntityID>\n"
        buf += ws + "<NumberVehicles>" + str(self.NumberVehicles) + "</NumberVehicles>\n"

        return buf
        
