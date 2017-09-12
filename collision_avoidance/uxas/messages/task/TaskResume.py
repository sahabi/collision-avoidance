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

from uxas.messages.task import TaskAssignment


class TaskResume(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 23
        self.SERIES_NAME = "UXTASK"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149757930721443840
        self.SERIES_VERSION = 7

        #Define message fields
        self.TaskID = 0   #int64
        self.RestartCompletely = False   #bool
        self.ReAssign = None   #TaskAssignment


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.TaskID))
        buffer.append(struct.pack(">B", self.RestartCompletely))
        buffer.append(struct.pack("B", self.ReAssign != None ))
        if self.ReAssign != None:
            buffer.append(struct.pack(">q", self.ReAssign.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.ReAssign.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.ReAssign.SERIES_VERSION))
            buffer.append(self.ReAssign.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.TaskID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.RestartCompletely = struct.unpack_from(">B", buffer, _pos)[0]
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
            self.ReAssign = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.ReAssign.unpack(buffer, _pos)
        else:
            self.ReAssign = None
        return _pos


    def get_TaskID(self):
        return self.TaskID

    def set_TaskID(self, value):
        self.TaskID = int( value )

    def get_RestartCompletely(self):
        return self.RestartCompletely

    def set_RestartCompletely(self, value):
        self.RestartCompletely = bool( value )

    def get_ReAssign(self):
        return self.ReAssign

    def set_ReAssign(self, value):
        self.ReAssign = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From TaskResume:\n"
        buf +=    "TaskID = " + str( self.TaskID ) + "\n" 
        buf +=    "RestartCompletely = " + str( self.RestartCompletely ) + "\n" 
        buf +=    "ReAssign = " + str( self.ReAssign ) + "\n" 

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
        str = ws + "<TaskResume>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</TaskResume>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<TaskID>" + str(self.TaskID) + "</TaskID>\n"
        buf += ws + "<RestartCompletely>" + str(self.RestartCompletely) + "</RestartCompletely>\n"
        buf += ws + "<ReAssign>\n"
        if self.ReAssign == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.ReAssign.toXMLStr(ws + "    ") 
        buf += ws + "</ReAssign>\n"

        return buf
        
