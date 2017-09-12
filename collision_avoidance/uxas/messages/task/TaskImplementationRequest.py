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
from uxas.messages.task import PlanningState


class TaskImplementationRequest(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 14
        self.SERIES_NAME = "UXTASK"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149757930721443840
        self.SERIES_VERSION = 7

        #Define message fields
        self.RequestID = 0   #int64
        self.CorrespondingAutomationRequestID = 0   #int64
        self.StartingWaypointID = 0   #int64
        self.VehicleID = 0   #int64
        self.StartPosition = Location3D.Location3D()   #Location3D
        self.StartHeading = 0   #real32
        self.StartTime = 0   #int64
        self.RegionID = 0   #int64
        self.TaskID = 0   #int64
        self.OptionID = 0   #int64
        self.TimeThreshold = 0   #int64
        self.NeighborLocations = []   #PlanningState


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.RequestID))
        buffer.append(struct.pack(">q", self.CorrespondingAutomationRequestID))
        buffer.append(struct.pack(">q", self.StartingWaypointID))
        buffer.append(struct.pack(">q", self.VehicleID))
        buffer.append(struct.pack("B", self.StartPosition != None ))
        if self.StartPosition != None:
            buffer.append(struct.pack(">q", self.StartPosition.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.StartPosition.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.StartPosition.SERIES_VERSION))
            buffer.append(self.StartPosition.pack())
        buffer.append(struct.pack(">f", self.StartHeading))
        buffer.append(struct.pack(">q", self.StartTime))
        buffer.append(struct.pack(">q", self.RegionID))
        buffer.append(struct.pack(">q", self.TaskID))
        buffer.append(struct.pack(">q", self.OptionID))
        buffer.append(struct.pack(">q", self.TimeThreshold))
        buffer.append(struct.pack(">H", len(self.NeighborLocations) ))
        for x in self.NeighborLocations:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.RequestID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.CorrespondingAutomationRequestID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.StartingWaypointID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.VehicleID = struct.unpack_from(">q", buffer, _pos)[0]
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
            self.StartPosition = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.StartPosition.unpack(buffer, _pos)
        else:
            self.StartPosition = None
        self.StartHeading = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.StartTime = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.RegionID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.TaskID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.OptionID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.TimeThreshold = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.NeighborLocations = [None] * _arraylen
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
                self.NeighborLocations[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.NeighborLocations[x].unpack(buffer, _pos)
            else:
                self.NeighborLocations[x] = None
        return _pos


    def get_RequestID(self):
        return self.RequestID

    def set_RequestID(self, value):
        self.RequestID = int( value )

    def get_CorrespondingAutomationRequestID(self):
        return self.CorrespondingAutomationRequestID

    def set_CorrespondingAutomationRequestID(self, value):
        self.CorrespondingAutomationRequestID = int( value )

    def get_StartingWaypointID(self):
        return self.StartingWaypointID

    def set_StartingWaypointID(self, value):
        self.StartingWaypointID = int( value )

    def get_VehicleID(self):
        return self.VehicleID

    def set_VehicleID(self, value):
        self.VehicleID = int( value )

    def get_StartPosition(self):
        return self.StartPosition

    def set_StartPosition(self, value):
        self.StartPosition = value 

    def get_StartHeading(self):
        return self.StartHeading

    def set_StartHeading(self, value):
        self.StartHeading = float( value )

    def get_StartTime(self):
        return self.StartTime

    def set_StartTime(self, value):
        self.StartTime = int( value )

    def get_RegionID(self):
        return self.RegionID

    def set_RegionID(self, value):
        self.RegionID = int( value )

    def get_TaskID(self):
        return self.TaskID

    def set_TaskID(self, value):
        self.TaskID = int( value )

    def get_OptionID(self):
        return self.OptionID

    def set_OptionID(self, value):
        self.OptionID = int( value )

    def get_TimeThreshold(self):
        return self.TimeThreshold

    def set_TimeThreshold(self, value):
        self.TimeThreshold = int( value )

    def get_NeighborLocations(self):
        return self.NeighborLocations



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From TaskImplementationRequest:\n"
        buf +=    "RequestID = " + str( self.RequestID ) + "\n" 
        buf +=    "CorrespondingAutomationRequestID = " + str( self.CorrespondingAutomationRequestID ) + "\n" 
        buf +=    "StartingWaypointID = " + str( self.StartingWaypointID ) + "\n" 
        buf +=    "VehicleID = " + str( self.VehicleID ) + "\n" 
        buf +=    "StartPosition = " + str( self.StartPosition ) + "\n" 
        buf +=    "StartHeading = " + str( self.StartHeading ) + "\n" 
        buf +=    "StartTime = " + str( self.StartTime ) + "\n" 
        buf +=    "RegionID = " + str( self.RegionID ) + "\n" 
        buf +=    "TaskID = " + str( self.TaskID ) + "\n" 
        buf +=    "OptionID = " + str( self.OptionID ) + "\n" 
        buf +=    "TimeThreshold = " + str( self.TimeThreshold ) + "\n" 
        buf +=    "NeighborLocations = " + str( self.NeighborLocations ) + "\n" 

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
        str = ws + "<TaskImplementationRequest>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</TaskImplementationRequest>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<RequestID>" + str(self.RequestID) + "</RequestID>\n"
        buf += ws + "<CorrespondingAutomationRequestID>" + str(self.CorrespondingAutomationRequestID) + "</CorrespondingAutomationRequestID>\n"
        buf += ws + "<StartingWaypointID>" + str(self.StartingWaypointID) + "</StartingWaypointID>\n"
        buf += ws + "<VehicleID>" + str(self.VehicleID) + "</VehicleID>\n"
        buf += ws + "<StartPosition>\n"
        if self.StartPosition == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.StartPosition.toXMLStr(ws + "    ") 
        buf += ws + "</StartPosition>\n"
        buf += ws + "<StartHeading>" + str(self.StartHeading) + "</StartHeading>\n"
        buf += ws + "<StartTime>" + str(self.StartTime) + "</StartTime>\n"
        buf += ws + "<RegionID>" + str(self.RegionID) + "</RegionID>\n"
        buf += ws + "<TaskID>" + str(self.TaskID) + "</TaskID>\n"
        buf += ws + "<OptionID>" + str(self.OptionID) + "</OptionID>\n"
        buf += ws + "<TimeThreshold>" + str(self.TimeThreshold) + "</TimeThreshold>\n"
        buf += ws + "<NeighborLocations>\n"
        for x in self.NeighborLocations:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</NeighborLocations>\n"

        return buf
        
