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


class BlockadeTask(Task.Task):

    def __init__(self):
        Task.Task.__init__(self)
        self.LMCP_TYPE = 33
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.BlockedEntityID = 0   #int64
        self.StandoffDistance = 0   #real32
        self.NumberVehicles = 1   #byte
        self.ProtectedLocation = None   #Location3D


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(Task.Task.pack(self))
        buffer.append(struct.pack(">q", self.BlockedEntityID))
        buffer.append(struct.pack(">f", self.StandoffDistance))
        buffer.append(struct.pack(">B", self.NumberVehicles))
        buffer.append(struct.pack("B", self.ProtectedLocation != None ))
        if self.ProtectedLocation != None:
            buffer.append(struct.pack(">q", self.ProtectedLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.ProtectedLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.ProtectedLocation.SERIES_VERSION))
            buffer.append(self.ProtectedLocation.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = Task.Task.unpack(self, buffer, _pos)
        self.BlockedEntityID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.StandoffDistance = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.NumberVehicles = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
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
            self.ProtectedLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.ProtectedLocation.unpack(buffer, _pos)
        else:
            self.ProtectedLocation = None
        return _pos


    def get_BlockedEntityID(self):
        return self.BlockedEntityID

    def set_BlockedEntityID(self, value):
        self.BlockedEntityID = int( value )

    def get_StandoffDistance(self):
        return self.StandoffDistance

    def set_StandoffDistance(self, value):
        self.StandoffDistance = float( value )

    def get_NumberVehicles(self):
        return self.NumberVehicles

    def set_NumberVehicles(self, value):
        self.NumberVehicles = int( value )

    def get_ProtectedLocation(self):
        return self.ProtectedLocation

    def set_ProtectedLocation(self, value):
        self.ProtectedLocation = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = Task.Task.toString(self)
        buf += "From BlockadeTask:\n"
        buf +=    "BlockedEntityID = " + str( self.BlockedEntityID ) + "\n" 
        buf +=    "StandoffDistance = " + str( self.StandoffDistance ) + "\n" 
        buf +=    "NumberVehicles = " + str( self.NumberVehicles ) + "\n" 
        buf +=    "ProtectedLocation = " + str( self.ProtectedLocation ) + "\n" 

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
        str = ws + "<BlockadeTask>\n";
        #str +=Task.Task.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</BlockadeTask>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += Task.Task.toXMLMembersStr(self, ws)
        buf += ws + "<BlockedEntityID>" + str(self.BlockedEntityID) + "</BlockedEntityID>\n"
        buf += ws + "<StandoffDistance>" + str(self.StandoffDistance) + "</StandoffDistance>\n"
        buf += ws + "<NumberVehicles>" + str(self.NumberVehicles) + "</NumberVehicles>\n"
        buf += ws + "<ProtectedLocation>\n"
        if self.ProtectedLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.ProtectedLocation.toXMLStr(ws + "    ") 
        buf += ws + "</ProtectedLocation>\n"

        return buf
        
