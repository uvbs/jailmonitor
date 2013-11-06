#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'xiaoghu@cisco.com'

import os
import time
import socket
import SocketServer
import traceback
from binascii import hexlify, unhexlify
from SocketServer import (TCPServer as TCP,
                          StreamRequestHandler as SRH,
                          ThreadingMixIn as TMI)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jailMonitor.settings")

from jailMonitor.settings import *
from persons.models import *
from positions.models import *
from lines.models import *
from schedules.models import *


def parse_temperature(data):
    """
    @param data: data is a hex string like "01040400dc01977a40", then return
    @return: temperature in float
    """
    temperature = -300

    try:
        read_value_hex = data[4]+data[5]+data[2]+data[3]
        read_value_int = int(read_value_hex, 16)

        temperature = float(read_value_int)/100.0
        pass
    except Exception as e:
        print e
        print traceback.format_exc()

    return temperature
    pass


def parse_humidity(data):
    """
    @param data: data is a hex string like "01040400dc01977a40", then return
    @return: humidity in float
    """
    humidity = -1

    try:
        read_value_hex = data[8]+data[9]+data[6]+data[7]
        read_value_int = int(read_value_hex, 16)

        humidity = float(read_value_int)/1000.0
        pass
    except Exception as e:
        print e
        print traceback.format_exc()

    return humidity
    pass


def insert_temperature_and_humidity(client_ip, data):
    device_no = int(data[0:2], 16)
    temperature = parse_temperature(data)
    humidity = parse_humidity(data)

    print "time:%s, client_ip:%s, device_no:%d, temperature:%s, humidity:%s" % (time.time(), client_ip, device_no, str(temperature), str(humidity), )

    try:
        # TODO: insert temperature and humidity here

        pass
    except Exception as e:
        print e
        print traceback.format_exc()
    pass


class TemperatureHumidityServer(TMI, TCP):
    """
    This server can serve multiple client at a same time.
    """
    pass


class TemperatureHumidityTCPHandler(SRH):
    def handle(self):
        while True:
            try:
                # self.request is the TCP socket connected to the client
                self.data = self.request.recv(1024).strip()
                client_ip = self.client_address[0]

                print self.data
                insert_temperature_and_humidity(client_ip, self.data)
                pass
            except Exception as e:
                print e
                print traceback.format_exc()


# class TemperatureTCPHandler(SocketServer.BaseRequestHandler):
#     """
#     The TemperatureTCPHandler class for our server.
#     It will break the connection to only receive one copy of data sent from a client.
#     It is instantiated once per connection to the server, and must
#     override the handle() method to implement communication to the
#     client.
#     """
#     def handle(self):
#         # self.request is the TCP socket connected to the client
#         self.data = self.request.recv(1024).strip()
#         print "{} wrote:".format(self.client_address[0])
#         print self.data
#
#         insert_temperature_and_humidity(self.data)
#
#         # just send back the same data, but upper-cased
#         # self.request.sendall(self.data.upper())
#
#     # def handle(self):
#     #     while True:
#     #         # self.request is the TCP socket connected to the client
#     #         self.data = self.request.recv(1024).strip()
#     #         print "{} wrote:".format(self.client_address[0])
#     #         print self.data
#     #
#     #         insert_temperature_and_humidity(self.data)
#     #
#     #         # just send back the same data, but upper-cased
#     #         # self.request.sendall(self.data.upper())


def get_temperature_humidity():
    """
    cmd = '01040000000271CB'

    start
    got connected from ('192.168.1.52', 57525)
    01040400dc01977a40
    end

    cmd = '01040000000131CA'
    start
    got connected from ('192.168.1.52', 32075)
    01040200de3968
    end
    """
    HOST, PORT = "localhost", 8888
    ADDR = (HOST, PORT)
    tcpServ = TemperatureHumidityServer(ADDR, TemperatureHumidityTCPHandler)
    tcpServ.serve_forever()

    # server = SocketServer.TCPServer((HOST, PORT), TemperatureTCPHandler)
    # server.serve_forever()
    pass


def parse_patrol_data(data):
    """
    @param data: a hex string like this aa3300fb000000a00f00000f17d60c0000790d00008fa61a00008d1500eda32800008d150000000000000000000000000000000000c64a086d03
    @return:
    """
    patrol = 0

    return patrol
    pass


def insert_patrol_data(data):

    try:
        pass
    except Exception as e:
        print e
        print traceback.format_exc()
        pass
    pass


class PatrolServer(TMI, TCP):
    """
    This server can serve multiple client at a same time.
    """
    pass


class PatrolTCPHandler(SRH):
    def handle(self):
        while True:
            try:
                # self.request is the TCP socket connected to the client
                self.data = self.request.recv(1024).strip()
                print "{} wrote:".format(self.client_address[0])
                print self.data
                insert_patrol_data(self.data)
                pass
            except Exception as e:
                print e
                print traceback.format_exc()


# class PatrolTCPHandler(SocketServer.BaseRequestHandler):
#     """
#     The RequestHandler class for our server.
#
#     It is instantiated once per connection to the server, and must
#     override the handle() method to implement communication to the
#     client.
#     """
#
#     def handle(self):
#         while True:
#             # self.request is the TCP socket connected to the client
#             self.data = self.request.recv(1024).strip()
#             print "{} wrote:".format(self.client_address[0])
#             print self.data
#
#             insert_temperature_and_humidity(self.data)
#
#             # just send back the same data, but upper-cased
#             # self.request.sendall(self.data.upper())


def get_patrol_data():
    """
    aa3300fb000000a00f00000f17d60c0000790d00008fa61a00008d1500eda32800008d150000000000000000000000000000000000c64a086d03
    got connected from ('192.168.1.51', 34387)
    aa3300fc000000a00f00000f18d60c00007a0d00008fa61a00008d1500eda32800008d150000000000000000000000000000000000c34a08ec03
    got connected from ('192.168.1.51', 34771)
    aa3300fd000000a00f00000f17d60c00007b0d00008fa61a00008d1500eda32800008d150000000000000000000000000000000000c34b081a04
    got connected from ('192.168.1.51', 35155)
    aa3300fe000000a00f00000f18d60c00007c0d00008fa61a00008d1500eda32800008d150000000000000000000000000000000000c95408a204
    """
    HOST, PORT = "localhost", 8889
    ADDR = (HOST, PORT)
    tcpServ = PatrolServer(ADDR, PatrolTCPHandler)
    tcpServ.serve_forever()
    pass
#
#
# def getTemperature1():
#
#     addr = ('0.0.0.0', 8888)
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # s = socket.socket()
#     s.bind(addr)
#     s.listen(3)
#
#     # ss, addr = s.accept()
#     # print 'got connected from', addr
#     cmd = '01040000000271CB'
#     print cmd
#
#     while True:
#         try:
#             s.send(unhexlify(cmd))
#             time.sleep(1)
#             data = s.recv(512)
#             print data
#             data = s.recv(4096)
#             pass
#         except Exception as e:
#             print e
#             print traceback.format_exc()
#             pass
#         pass
#     s.close()
#
#
#     """
#     # s.connect(addr)
#     time.sleep(1)
#     s.send('0x01040000000271cb')
#     time.sleep(1)
#     data = s.recv(512)
#     print data
#     s.close()
#     """
#     pass


if __name__ == "__main__":
    print 'start'
    get_temperature_humidity()
    # getPatrolData()
    print 'end'

"""
需要沟通的问题：
    1. 返回结果如何计算温度和湿度值？
    2. mac地址为什么为4*8=32位？
"""