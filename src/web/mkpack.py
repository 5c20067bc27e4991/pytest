#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct

structDataType = '!10sL'
headSize = struct.calcsize(structDataType)


def buildPack(dataType, dataBody):
    '''
    数据头结构: [ 数据类型 数据体长度 ]
    '''
    head = [dataType.encode('utf-8'), len(dataBody.encode('utf-8'))]
    headStruct = struct.pack(structDataType, *head)
    sendData = headStruct + dataBody.encode('utf-8')
    return sendData


def recvPack(dataBuf, headSize):
    while True:
        if len(dataBuf) < headSize:
            break
        dataType = struct.unpack(structDataType, dataBuf[:headSize])[0]
        bodySize = struct.unpack(structDataType, dataBuf[:headSize])[1]

        if len(dataBuf) < headSize + bodySize:
            print('Error!!!!!')
            print('############')
            print(dataBuf.decode())
            print('############')
            return None, None, dataBuf

        body = dataBuf[headSize:headSize + bodySize]

        # 粘包处理
        dataBuf = dataBuf[headSize + bodySize:]
        return dataType.decode(), body.decode(), dataBuf
