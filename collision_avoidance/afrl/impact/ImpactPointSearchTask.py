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

from afrl.cmasi import SearchTask
from afrl.cmasi import Location3D
from afrl.cmasi import Wedge
from afrl.cmasi import LoiterAction


class ImpactPointSearchTask(SearchTask.SearchTask):

    def __init__(self):
        SearchTask.SearchTask.__init__(self)
        self.LMCP_TYPE = 25
        self.SERIES_NAME = "IMPACT"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 5281966179208134656
        self.SERIES_VERSION = 11

        #Define message fields
        self.SearchLocationID = 0   #int64
        self.SearchLocation = None   #Location3D
        self.StandoffDistance = 0   #real32
        self.ViewAngleList = []   #Wedge
        self.DesiredAction = None   #LoiterAction


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(SearchTask.SearchTask.pack(self))
        buffer.append(struct.pack(">q", self.SearchLocationID))
        buffer.append(struct.pack("B", self.SearchLocation != None ))
        if self.SearchLocation != None:
            buffer.append(struct.pack(">q", self.SearchLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.SearchLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.SearchLocation.SERIES_VERSION))
            buffer.append(self.SearchLocation.pack())
        buffer.append(struct.pack(">f", self.StandoffDistance))
        buffer.append(struct.pack(">H", len(self.ViewAngleList) ))
        for x in self.ViewAngleList:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack("B", self.DesiredAction != None ))
        if self.DesiredAction != None:
            buffer.append(struct.pack(">q", self.DesiredAction.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.DesiredAction.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.DesiredAction.SERIES_VERSION))
            buffer.append(self.DesiredAction.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = SearchTask.SearchTask.unpack(self, buffer, _pos)
        self.SearchLocationID = struct.unpack_from(">q", buffer, _pos)[0]
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
            self.SearchLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.SearchLocation.unpack(buffer, _pos)
        else:
            self.SearchLocation = None
        self.StandoffDistance = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.ViewAngleList = [None] * _arraylen
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
                self.ViewAngleList[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.ViewAngleList[x].unpack(buffer, _pos)
            else:
                self.ViewAngleList[x] = None
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
            self.DesiredAction = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.DesiredAction.unpack(buffer, _pos)
        else:
            self.DesiredAction = None
        return _pos


    def get_SearchLocationID(self):
        return self.SearchLocationID

    def set_SearchLocationID(self, value):
        self.SearchLocationID = int( value )

    def get_SearchLocation(self):
        return self.SearchLocation

    def set_SearchLocation(self, value):
        self.SearchLocation = value 

    def get_StandoffDistance(self):
        return self.StandoffDistance

    def set_StandoffDistance(self, value):
        self.StandoffDistance = float( value )

    def get_ViewAngleList(self):
        return self.ViewAngleList

    def get_DesiredAction(self):
        return self.DesiredAction

    def set_DesiredAction(self, value):
        self.DesiredAction = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = SearchTask.SearchTask.toString(self)
        buf += "From ImpactPointSearchTask:\n"
        buf +=    "SearchLocationID = " + str( self.SearchLocationID ) + "\n" 
        buf +=    "SearchLocation = " + str( self.SearchLocation ) + "\n" 
        buf +=    "StandoffDistance = " + str( self.StandoffDistance ) + "\n" 
        buf +=    "ViewAngleList = " + str( self.ViewAngleList ) + "\n" 
        buf +=    "DesiredAction = " + str( self.DesiredAction ) + "\n" 

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
        str = ws + "<ImpactPointSearchTask>\n";
        #str +=SearchTask.SearchTask.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</ImpactPointSearchTask>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += SearchTask.SearchTask.toXMLMembersStr(self, ws)
        buf += ws + "<SearchLocationID>" + str(self.SearchLocationID) + "</SearchLocationID>\n"
        buf += ws + "<SearchLocation>\n"
        if self.SearchLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.SearchLocation.toXMLStr(ws + "    ") 
        buf += ws + "</SearchLocation>\n"
        buf += ws + "<StandoffDistance>" + str(self.StandoffDistance) + "</StandoffDistance>\n"
        buf += ws + "<ViewAngleList>\n"
        for x in self.ViewAngleList:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</ViewAngleList>\n"
        buf += ws + "<DesiredAction>\n"
        if self.DesiredAction == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.DesiredAction.toXMLStr(ws + "    ") 
        buf += ws + "</DesiredAction>\n"

        return buf
        
