#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct
import hashlib

structDataType = '!10sL'
headSize = struct.calcsize(structDataType)


def cal_md5(file_path):
    with open(file_path, 'rb') as fr:
        md5 = hashlib.md5()
        md5.update(fr.read())
        md5 = md5.hexdigest()
        return md5


def buildPack(dataType, dataBody):
    '''
    数据头结构: [ 数据类型 数据体长度 ]
    '''
    if not dataType == 'file':
        dataBody = dataBody.encode('utf-8')
    head = [dataType.encode(), len(dataBody)]
    headStruct = struct.pack(structDataType, *head)
    sendData = headStruct + dataBody
    return sendData


def recvPack(dataBuf, headSize):
    dataType = struct.unpack(structDataType, dataBuf[:headSize])[0]
    bodySize = struct.unpack(structDataType, dataBuf[:headSize])[1]

    if len(dataBuf) < headSize + bodySize:
        return None, None, dataBuf

    body = dataBuf[headSize:headSize + bodySize]

    # 粘包处理
    dataBuf = dataBuf[headSize + bodySize:]
    return dataType.decode(), body.decode(), dataBuf