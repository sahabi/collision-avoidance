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

from afrl.cmasi import Task
from afrl.cmasi import Location3D


class CommRelayTask(Task.Task):

    def __init__(self):
        Task.Task.__init__(self)
        self.LMCP_TYPE = 31
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.SupportedEntityID = 0   #int64
        self.DestinationLocation = None   #Location3D
        self.TowerID = 0   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(Task.Task.pack(self))
        buffer.append(struct.pack(">q", self.SupportedEntityID))
        buffer.append(struct.pack("B", self.DestinationLocation != None ))
        if self.DestinationLocation != None:
            buffer.append(struct.pack(">q", self.DestinationLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.DestinationLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.DestinationLocation.SERIES_VERSION))
            buffer.append(self.DestinationLocation.pack())
        buffer.append(struct.pack(">q", self.TowerID))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = Task.Task.unpack(self, buffer, _pos)
        self.SupportedEntityID = struct.unpack_from(">q", buffer, _pos)[0]
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
            self.DestinationLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.DestinationLocation.unpack(buffer, _pos)
        else:
            self.DestinationLocation = None
        self.TowerID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        return _pos


    def get_SupportedEntityID(self):
        return self.SupportedEntityID

    def set_SupportedEntityID(self, value):
        self.SupportedEntityID = int( value )

    def get_DestinationLocation(self):
        return self.DestinationLocation

    def set_DestinationLocation(self, value):
        self.DestinationLocation = value 

    def get_TowerID(self):
        return self.TowerID

    def set_TowerID(self, value):
        self.TowerID = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = Task.Task.toString(self)
        buf += "From CommRelayTask:\n"
        buf +=    "SupportedEntityID = " + str( self.SupportedEntityID ) + "\n" 
        buf +=    "DestinationLocation = " + str( self.DestinationLocation ) + "\n" 
        buf +=    "TowerID = " + str( self.TowerID ) + "\n" 

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
        str = ws + "<CommRelayTask>\n";
        #str +=Task.Task.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</CommRelayTask>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += Task.Task.toXMLMembersStr(self, ws)
        buf += ws + "<SupportedEntityID>" + str(self.SupportedEntityID) + "</SupportedEntityID>\n"
        buf += ws + "<DestinationLocation>\n"
        if self.DestinationLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.DestinationLocation.toXMLStr(ws + "    ") 
        buf += ws + "</DestinationLocation>\n"
        buf += ws + "<TowerID>" + str(self.TowerID) + "</TowerID>\n"

        return buf
        
