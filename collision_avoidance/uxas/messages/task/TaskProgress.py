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



class TaskProgress(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 24
        self.SERIES_NAME = "UXTASK"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149757930721443840
        self.SERIES_VERSION = 7

        #Define message fields
        self.ResponseID = 0   #int64
        self.TaskID = 0   #int64
        self.PercentComplete = 0   #real32
        self.EntitiesEngaged = []   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.ResponseID))
        buffer.append(struct.pack(">q", self.TaskID))
        buffer.append(struct.pack(">f", self.PercentComplete))
        buffer.append(struct.pack(">H", len(self.EntitiesEngaged) ))
        for x in self.EntitiesEngaged:
            buffer.append(struct.pack(">q", x ))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.ResponseID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.TaskID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.PercentComplete = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.EntitiesEngaged = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.EntitiesEngaged = struct.unpack_from(">" + `_arraylen` + "q", buffer, _pos )
            _pos += 8 * _arraylen
        return _pos


    def get_ResponseID(self):
        return self.ResponseID

    def set_ResponseID(self, value):
        self.ResponseID = int( value )

    def get_TaskID(self):
        return self.TaskID

    def set_TaskID(self, value):
        self.TaskID = int( value )

    def get_PercentComplete(self):
        return self.PercentComplete

    def set_PercentComplete(self, value):
        self.PercentComplete = float( value )

    def get_EntitiesEngaged(self):
        return self.EntitiesEngaged



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From TaskProgress:\n"
        buf +=    "ResponseID = " + str( self.ResponseID ) + "\n" 
        buf +=    "TaskID = " + str( self.TaskID ) + "\n" 
        buf +=    "PercentComplete = " + str( self.PercentComplete ) + "\n" 
        buf +=    "EntitiesEngaged = " + str( self.EntitiesEngaged ) + "\n" 

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
        str = ws + "<TaskProgress>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</TaskProgress>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<ResponseID>" + str(self.ResponseID) + "</ResponseID>\n"
        buf += ws + "<TaskID>" + str(self.TaskID) + "</TaskID>\n"
        buf += ws + "<PercentComplete>" + str(self.PercentComplete) + "</PercentComplete>\n"
        buf += ws + "<EntitiesEngaged>\n"
        for x in self.EntitiesEngaged:
            buf += ws + "<int64>" + str(x) + "</int64>\n"
        buf += ws + "</EntitiesEngaged>\n"

        return buf
        
