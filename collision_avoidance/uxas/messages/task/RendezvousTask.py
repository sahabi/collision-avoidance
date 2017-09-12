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
from uxas.messages.task import PlanningState


class RendezvousTask(Task.Task):

    def __init__(self):
        Task.Task.__init__(self)
        self.LMCP_TYPE = 2
        self.SERIES_NAME = "UXTASK"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149757930721443840
        self.SERIES_VERSION = 7

        #Define message fields
        self.NumberOfParticipants = 0   #byte
        self.Location = None   #Location3D
        self.Heading = 0   #real32
        self.MultiLocationRendezvous = False   #bool
        self.RendezvousStates = []   #PlanningState


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(Task.Task.pack(self))
        buffer.append(struct.pack(">B", self.NumberOfParticipants))
        buffer.append(struct.pack("B", self.Location != None ))
        if self.Location != None:
            buffer.append(struct.pack(">q", self.Location.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.Location.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.Location.SERIES_VERSION))
            buffer.append(self.Location.pack())
        buffer.append(struct.pack(">f", self.Heading))
        buffer.append(struct.pack(">B", self.MultiLocationRendezvous))
        buffer.append(struct.pack(">H", len(self.RendezvousStates) ))
        for x in self.RendezvousStates:
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
        _pos = Task.Task.unpack(self, buffer, _pos)
        self.NumberOfParticipants = struct.unpack_from(">B", buffer, _pos)[0]
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
            self.Location = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.Location.unpack(buffer, _pos)
        else:
            self.Location = None
        self.Heading = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        self.MultiLocationRendezvous = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.RendezvousStates = [None] * _arraylen
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
                self.RendezvousStates[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.RendezvousStates[x].unpack(buffer, _pos)
            else:
                self.RendezvousStates[x] = None
        return _pos


    def get_NumberOfParticipants(self):
        return self.NumberOfParticipants

    def set_NumberOfParticipants(self, value):
        self.NumberOfParticipants = int( value )

    def get_Location(self):
        return self.Location

    def set_Location(self, value):
        self.Location = value 

    def get_Heading(self):
        return self.Heading

    def set_Heading(self, value):
        self.Heading = float( value )

    def get_MultiLocationRendezvous(self):
        return self.MultiLocationRendezvous

    def set_MultiLocationRendezvous(self, value):
        self.MultiLocationRendezvous = bool( value )

    def get_RendezvousStates(self):
        return self.RendezvousStates



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = Task.Task.toString(self)
        buf += "From RendezvousTask:\n"
        buf +=    "NumberOfParticipants = " + str( self.NumberOfParticipants ) + "\n" 
        buf +=    "Location = " + str( self.Location ) + "\n" 
        buf +=    "Heading = " + str( self.Heading ) + "\n" 
        buf +=    "MultiLocationRendezvous = " + str( self.MultiLocationRendezvous ) + "\n" 
        buf +=    "RendezvousStates = " + str( self.RendezvousStates ) + "\n" 

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
        str = ws + "<RendezvousTask>\n";
        #str +=Task.Task.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</RendezvousTask>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += Task.Task.toXMLMembersStr(self, ws)
        buf += ws + "<NumberOfParticipants>" + str(self.NumberOfParticipants) + "</NumberOfParticipants>\n"
        buf += ws + "<Location>\n"
        if self.Location == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.Location.toXMLStr(ws + "    ") 
        buf += ws + "</Location>\n"
        buf += ws + "<Heading>" + str(self.Heading) + "</Heading>\n"
        buf += ws + "<MultiLocationRendezvous>" + str(self.MultiLocationRendezvous) + "</MultiLocationRendezvous>\n"
        buf += ws + "<RendezvousStates>\n"
        for x in self.RendezvousStates:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</RendezvousStates>\n"

        return buf
        
