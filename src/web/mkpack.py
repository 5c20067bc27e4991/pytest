#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct

structDataType = '!10sL'
headSize = struct.calcsize(structDataType)


def buildPack(dataType, dataBody):
    head = [dataType.encode('utf-8'), len(dataBody.encode('utf-8'))]
    headStruct = struct.pack(structDataType, *head)
    sendData = headStruct + dataBody.encode('utf-8')
    return sendData
