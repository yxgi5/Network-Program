#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

HOST='127.0.0.1'
PORT=9998

sockaddr=(HOST,PORT)
ct=socket.socket()
ct.connect(sockaddr)
while True:
    inp=input("请输入要发送的内容: ")
    ct.sendall(bytes(inp,encoding='utf-8'))
    ret_bytes=ct.recv(1024)
    print(str(ret_bytes,encoding='utf-8'))
ct.close()