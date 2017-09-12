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

from afrl.cmasi import EntityState


class SurfaceVehicleState(EntityState.EntityState):

    def __init__(self):
        EntityState.EntityState.__init__(self)
        self.LMCP_TYPE = 41
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.BankAngle = 0   #real32
        self.Speed = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(EntityState.EntityState.pack(self))
        buffer.append(struct.pack(">f", self.BankAngle))
        buffer.append(struct.pack(">f", self.Speed))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = EntityState.EntityState.unpack(self, buffer, _pos)
        self.BankAngle = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.Speed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_BankAngle(self):
        return self.BankAngle

    def set_BankAngle(self, value):
        self.BankAngle = float( value )

    def get_Speed(self):
        return self.Speed

    def set_Speed(self, value):
        self.Speed = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = EntityState.EntityState.toString(self)
        buf += "From SurfaceVehicleState:\n"
        buf +=    "BankAngle = " + str( self.BankAngle ) + "\n" 
        buf +=    "Speed = " + str( self.Speed ) + "\n" 

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
        str = ws + "<SurfaceVehicleState>\n";
        #str +=EntityState.EntityState.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</SurfaceVehicleState>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += EntityState.EntityState.toXMLMembersStr(self, ws)
        buf += ws + "<BankAngle>" + str(self.BankAngle) + "</BankAngle>\n"
        buf += ws + "<Speed>" + str(self.Speed) + "</Speed>\n"

        return buf
        
