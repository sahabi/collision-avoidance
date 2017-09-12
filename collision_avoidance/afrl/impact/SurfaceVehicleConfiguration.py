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

from afrl.cmasi import EntityConfiguration


class SurfaceVehicleConfiguration(EntityConfiguration.EntityConfiguration):

    def __init__(self):
        EntityConfiguration.EntityConfiguration.__init__(self)
        self.LMCP_TYPE = 40
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.WaterArea = 0   #int64
        self.MinimumSpeed = 0   #real32
        self.MaximumSpeed = 0   #real32
        self.EnergyRate = 0   #real32
        self.MaxBankAngle = 0   #real32
        self.MaxBankRate = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(EntityConfiguration.EntityConfiguration.pack(self))
        buffer.append(struct.pack(">q", self.WaterArea))
        buffer.append(struct.pack(">f", self.MinimumSpeed))
        buffer.append(struct.pack(">f", self.MaximumSpeed))
        buffer.append(struct.pack(">f", self.EnergyRate))
        buffer.append(struct.pack(">f", self.MaxBankAngle))
        buffer.append(struct.pack(">f", self.MaxBankRate))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = EntityConfiguration.EntityConfiguration.unpack(self, buffer, _pos)
        self.WaterArea = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.MinimumSpeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.MaximumSpeed = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.EnergyRate = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.MaxBankAngle = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.MaxBankRate = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def get_WaterArea(self):
        return self.WaterArea

    def set_WaterArea(self, value):
        self.WaterArea = int( value )

    def get_MinimumSpeed(self):
        return self.MinimumSpeed

    def set_MinimumSpeed(self, value):
        self.MinimumSpeed = float( value )

    def get_MaximumSpeed(self):
        return self.MaximumSpeed

    def set_MaximumSpeed(self, value):
        self.MaximumSpeed = float( value )

    def get_EnergyRate(self):
        return self.EnergyRate

    def set_EnergyRate(self, value):
        self.EnergyRate = float( value )

    def get_MaxBankAngle(self):
        return self.MaxBankAngle

    def set_MaxBankAngle(self, value):
        self.MaxBankAngle = float( value )

    def get_MaxBankRate(self):
        return self.MaxBankRate

    def set_MaxBankRate(self, value):
        self.MaxBankRate = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = EntityConfiguration.EntityConfiguration.toString(self)
        buf += "From SurfaceVehicleConfiguration:\n"
        buf +=    "WaterArea = " + str( self.WaterArea ) + "\n" 
        buf +=    "MinimumSpeed = " + str( self.MinimumSpeed ) + "\n" 
        buf +=    "MaximumSpeed = " + str( self.MaximumSpeed ) + "\n" 
        buf +=    "EnergyRate = " + str( self.EnergyRate ) + "\n" 
        buf +=    "MaxBankAngle = " + str( self.MaxBankAngle ) + "\n" 
        buf +=    "MaxBankRate = " + str( self.MaxBankRate ) + "\n" 

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
        str = ws + "<SurfaceVehicleConfiguration>\n";
        #str +=EntityConfiguration.EntityConfiguration.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</SurfaceVehicleConfiguration>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += EntityConfiguration.EntityConfiguration.toXMLMembersStr(self, ws)
        buf += ws + "<WaterArea>" + str(self.WaterArea) + "</WaterArea>\n"
        buf += ws + "<MinimumSpeed>" + str(self.MinimumSpeed) + "</MinimumSpeed>\n"
        buf += ws + "<MaximumSpeed>" + str(self.MaximumSpeed) + "</MaximumSpeed>\n"
        buf += ws + "<EnergyRate>" + str(self.EnergyRate) + "</EnergyRate>\n"
        buf += ws + "<MaxBankAngle>" + str(self.MaxBankAngle) + "</MaxBankAngle>\n"
        buf += ws + "<MaxBankRate>" + str(self.MaxBankRate) + "</MaxBankRate>\n"

        return buf
        
