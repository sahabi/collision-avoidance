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

from uxas.messages.route import RouteConstraints


class RouteRequest(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 5
        self.SERIES_NAME = "ROUTE"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5931053054693474304
        self.SERIES_VERSION = 3

        #Define message fields
        self.RequestID = 0   #int64
        self.AssociatedTaskID = 0   #int64
        self.VehicleID = []   #int64
        self.OperatingRegion = 0   #int64
        self.RouteRequests = []   #RouteConstraints
        self.IsCostOnlyRequest = True   #bool


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.RequestID))
        buffer.append(struct.pack(">q", self.AssociatedTaskID))
        buffer.append(struct.pack(">H", len(self.VehicleID) ))
        for x in self.VehicleID:
            buffer.append(struct.pack(">q", x ))
        buffer.append(struct.pack(">q", self.OperatingRegion))
        buffer.append(struct.pack(">H", len(self.RouteRequests) ))
        for x in self.RouteRequests:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">B", self.IsCostOnlyRequest))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.RequestID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.AssociatedTaskID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.VehicleID = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.VehicleID = struct.unpack_from(">" + `_arraylen` + "q", buffer, _pos )
            _pos += 8 * _arraylen
        self.OperatingRegion = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.RouteRequests = [None] * _arraylen
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
                self.RouteRequests[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.RouteRequests[x].unpack(buffer, _pos)
            else:
                self.RouteRequests[x] = None
        self.IsCostOnlyRequest = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        return _pos


    def get_RequestID(self):
        return self.RequestID

    def set_RequestID(self, value):
        self.RequestID = int( value )

    def get_AssociatedTaskID(self):
        return self.AssociatedTaskID

    def set_AssociatedTaskID(self, value):
        self.AssociatedTaskID = int( value )

    def get_VehicleID(self):
        return self.VehicleID

    def get_OperatingRegion(self):
        return self.OperatingRegion

    def set_OperatingRegion(self, value):
        self.OperatingRegion = int( value )

    def get_RouteRequests(self):
        return self.RouteRequests

    def get_IsCostOnlyRequest(self):
        return self.IsCostOnlyRequest

    def set_IsCostOnlyRequest(self, value):
        self.IsCostOnlyRequest = bool( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From RouteRequest:\n"
        buf +=    "RequestID = " + str( self.RequestID ) + "\n" 
        buf +=    "AssociatedTaskID = " + str( self.AssociatedTaskID ) + "\n" 
        buf +=    "VehicleID = " + str( self.VehicleID ) + "\n" 
        buf +=    "OperatingRegion = " + str( self.OperatingRegion ) + "\n" 
        buf +=    "RouteRequests = " + str( self.RouteRequests ) + "\n" 
        buf +=    "IsCostOnlyRequest = " + str( self.IsCostOnlyRequest ) + "\n" 

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
        str = ws + "<RouteRequest>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</RouteRequest>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<RequestID>" + str(self.RequestID) + "</RequestID>\n"
        buf += ws + "<AssociatedTaskID>" + str(self.AssociatedTaskID) + "</AssociatedTaskID>\n"
        buf += ws + "<VehicleID>\n"
        for x in self.VehicleID:
            buf += ws + "<int64>" + str(x) + "</int64>\n"
        buf += ws + "</VehicleID>\n"
        buf += ws + "<OperatingRegion>" + str(self.OperatingRegion) + "</OperatingRegion>\n"
        buf += ws + "<RouteRequests>\n"
        for x in self.RouteRequests:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</RouteRequests>\n"
        buf += ws + "<IsCostOnlyRequest>" + str(self.IsCostOnlyRequest) + "</IsCostOnlyRequest>\n"

        return buf
        
