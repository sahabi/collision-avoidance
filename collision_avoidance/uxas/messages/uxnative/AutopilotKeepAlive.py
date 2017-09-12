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



class AutopilotKeepAlive(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 11
        self.SERIES_NAME = "UXNATIVE"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149751333668345413
        self.SERIES_VERSION = 3

        #Define message fields
        self.AutopilotEnabled = True   #bool
        self.GimbalEnabled = True   #bool
        self.TimeSent = 0   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">B", self.AutopilotEnabled))
        buffer.append(struct.pack(">B", self.GimbalEnabled))
        buffer.append(struct.pack(">q", self.TimeSent))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.AutopilotEnabled = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        self.GimbalEnabled = struct.unpack_from(">B", buffer, _pos)[0]
        _pos += 1
        self.TimeSent = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        return _pos


    def get_AutopilotEnabled(self):
        return self.AutopilotEnabled

    def set_AutopilotEnabled(self, value):
        self.AutopilotEnabled = bool( value )

    def get_GimbalEnabled(self):
        return self.GimbalEnabled

    def set_GimbalEnabled(self, value):
        self.GimbalEnabled = bool( value )

    def get_TimeSent(self):
        return self.TimeSent

    def set_TimeSent(self, value):
        self.TimeSent = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From AutopilotKeepAlive:\n"
        buf +=    "AutopilotEnabled = " + str( self.AutopilotEnabled ) + "\n" 
        buf +=    "GimbalEnabled = " + str( self.GimbalEnabled ) + "\n" 
        buf +=    "TimeSent = " + str( self.TimeSent ) + "\n" 

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
        str = ws + "<AutopilotKeepAlive>\n";
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</AutopilotKeepAlive>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<AutopilotEnabled>" + str(self.AutopilotEnabled) + "</AutopilotEnabled>\n"
        buf += ws + "<GimbalEnabled>" + str(self.GimbalEnabled) + "</GimbalEnabled>\n"
        buf += ws + "<TimeSent>" + str(self.TimeSent) + "</TimeSent>\n"

        return buf
        
