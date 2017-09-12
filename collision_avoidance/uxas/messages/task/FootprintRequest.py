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

from afrl.cmasi import WavelengthBand


class FootprintRequest(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 11
        self.SERIES_NAME = "UXTASK"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149757930721443840
        self.SERIES_VERSION = 7

        #Define message fields
        self.FootprintRequestID = 0   #int64
        self.VehicleID = 0   #int64
        self.EligibleWavelengths = []   #WavelengthBand
        self.GroundSampleDistances = []   #real32
        self.AglAltitudes = []   #real32
        self.ElevationAngles = []   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.FootprintRequestID))
        buffer.append(struct.pack(">q", self.VehicleID))
        buffer.append(struct.pack(">H", len(self.EligibleWavelengths) ))
        for x in self.EligibleWavelengths:
            buffer.append(struct.pack(">i", x ))
        buffer.append(struct.pack(">H", len(self.GroundSampleDistances) ))
        for x in self.GroundSampleDistances:
            buffer.append(struct.pack(">f", x ))
        buffer.append(struct.pack(">H", len(self.AglAltitudes) ))
        for x in self.AglAltitudes:
            buffer.append(struct.pack(">f", x ))
        buffer.append(struct.pack(">H", len(self.ElevationAngles) ))
        for x in self.ElevationAngles:
            buffer.append(struct.pack(">f", x ))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.FootprintRequestID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.VehicleID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.EligibleWavelengths = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.EligibleWavelengths = struct.unpack_from(">" + `_arraylen` + "i", buffer, _pos )
            _pos += 4 * _arraylen
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.GroundSampleDistances = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.GroundSampleDistances = struct.unpack_from(">" + `_arraylen` + "f", buffer, _pos )
            _pos += 4 * _arraylen
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.AglAltitudes = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.AglAltitudes = struct.unpack_from(">" + `_arraylen` + "f", buffer, _pos )
            _pos += 4 * _arraylen
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.ElevationAngles = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.ElevationAngles = struct.unpack_from(">" + `_arraylen` + "f", buffer, _pos )
            _pos += 4 * _arraylen
        return _pos


    def get_FootprintRequestID(self):
        return self.FootprintRequestID

    def set_FootprintRequestID(self, value):
        self.FootprintRequestID = int( value )

    def get_VehicleID(self):
        return self.VehicleID

    def set_VehicleID(self, value):
        self.VehicleID = int( value )

    def get_EligibleWavelengths(self):
        return self.EligibleWavelengths

    def get_GroundSampleDistances(self):
        return self.GroundSampleDistances

    def get_AglAltitudes(self):
        return self.AglAltitudes

    def get_ElevationAngles(self):
        return self.ElevationAngles



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From FootprintRequest:\n"
        buf +=    "FootprintRequestID = " + str( self.FootprintRequestID ) + "\n" 
        buf +=    "VehicleID = " + str( self.VehicleID ) + "\n" 
        buf +=    "EligibleWavelengths = " + str( self.EligibleWavelengths ) + "\n" 
        buf +=    "GroundSampleDistances = " + str( self.GroundSampleDistances ) + "\n" 
        buf +=    "AglAltitudes = " + str( self.AglAltitudes ) + "\n" 
        buf +=    "ElevationAngles = " + str( self.ElevationAngles ) + "\n" 

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
        str = ws + "<FootprintRequest>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</FootprintRequest>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<FootprintRequestID>" + str(self.FootprintRequestID) + "</FootprintRequestID>\n"
        buf += ws + "<VehicleID>" + str(self.VehicleID) + "</VehicleID>\n"
        buf += ws + "<EligibleWavelengths>\n"
        for x in self.EligibleWavelengths:
            buf += ws + "<WavelengthBand>" + WavelengthBand.get_WavelengthBand_int(x) + "</WavelengthBand>\n"
        buf += ws + "</EligibleWavelengths>\n"
        buf += ws + "<GroundSampleDistances>\n"
        for x in self.GroundSampleDistances:
            buf += ws + "<real32>" + str(x) + "</real32>\n"
        buf += ws + "</GroundSampleDistances>\n"
        buf += ws + "<AglAltitudes>\n"
        for x in self.AglAltitudes:
            buf += ws + "<real32>" + str(x) + "</real32>\n"
        buf += ws + "</AglAltitudes>\n"
        buf += ws + "<ElevationAngles>\n"
        for x in self.ElevationAngles:
            buf += ws + "<real32>" + str(x) + "</real32>\n"
        buf += ws + "</ElevationAngles>\n"

        return buf
        
