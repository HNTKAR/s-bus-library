# -*- coding: utf-8 -*-
import time
import serial
import RPi.GPIO as GPIO

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=100000, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=1)

#GPIO設定
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN)#通信信号
GPIO.setup(26, GPIO.IN)#起動ピン
GPIO.setup(16, GPIO.IN)#下降判断
GPIO.setup(20, GPIO.IN)#lat
GPIO.setup(21, GPIO.IN)#lon



#数値固定
sys=0
a=0
latnum=0
latn=0
lats=0
lonnum=0
lone=0
lonw=0
lonlat=0
dupcount=350#上昇時間
ddowncount=700#下降時間
dhovercount=200#ホバリング時間
dgocount=10#移動時間

def usbus():#5ch以降のシグナル
    global a
    ser.write(chr(0x6A))
    ser.write(chr(0xB0))
    ser.write(chr(0x60))
    ser.write(chr(0x18))
    ser.write(chr(0x80))
    ser.write(chr(0x60))
    ser.write(chr(0x01))
    ser.write(chr(0x20))
    ser.write(chr(0x00))
    ser.write(chr(0x01))
    ser.write(chr(0x08))
    ser.write(chr(0x16))
    ser.write(chr(0x00))
    ser.write(chr(0x02))
    ser.write(chr(0x10))
    ser.write(chr(0x80))
    ser.write(chr(0x00))
    if a==0:
        ser.write(chr(0x04))
        a=1
        time.sleep(.0143)
    elif a==1:
        ser.write(chr(0x14))
        a=2
        time.sleep(.0143)
    elif a==2:
        ser.write(chr(0x24))
        a=3
        time.sleep(.0143)
    else:
        ser.write(chr(0x34))
        a=0
        time.sleep(.0143)

def dhover():#ホバリング
    ser.write(chr(0x0F))
    ser.write(chr(0x00))
    ser.write(chr(0x04))
    ser.write(chr(0x20))
    ser.write(chr(0x00))
    ser.write(chr(0x01))
    ser.write(chr(0x08))
    usbus()


def dgono():#北
    ser.write(chr(0x0F))
    ser.write(chr(0x00))
    ser.write(chr(0x84))
    ser.write(chr(0x15))
    ser.write(chr(0x00))
    ser.write(chr(0x01))
    ser.write(chr(0x08))
    usbus()


def dgoso():#南
    ser.write(chr(0x0F))
    ser.write(chr(0x00))
    ser.write(chr(0x84))
    ser.write(chr(0x2A))
    ser.write(chr(0x00))
    ser.write(chr(0x01))
    ser.write(chr(0x08))
    usbus()


def dgoea():#東
    ser.write(chr(0x0F))
    ser.write(chr(0x50))
    ser.write(chr(0x05))
    ser.write(chr(0x20))
    ser.write(chr(0x00))
    ser.write(chr(0x01))
    ser.write(chr(0x08))
    usbus()


def dgowe():#西
    ser.write(chr(0x0F))
    ser.write(chr(0xB0))
    ser.write(chr(0x02))
    ser.write(chr(0x20))
    ser.write(chr(0x00))
    ser.write(chr(0x01))
    ser.write(chr(0x08))
    usbus()


def ddown():

    ser.write(chr(0x0F))
    ser.write(chr(0x00))
    ser.write(chr(0x04))
    ser.write(chr(0x20))
    ser.write(chr(0x45))
    ser.write(chr(0x01))
    ser.write(chr(0x08))
    usbus()


def dup():
    ser.write(chr(0x0F))
    ser.write(chr(0x00))
    ser.write(chr(0x04))
    ser.write(chr(0x20))
    ser.write(chr(0xAC))
    ser.write(chr(0x00))
    ser.write(chr(0x08))
    usbus()


def don():
    ser.write(chr(0x0F))
    ser.write(chr(0x60))
    ser.write(chr(0x01))
    ser.write(chr(0x35))
    ser.write(chr(0xA8))
    ser.write(chr(0x41))
    ser.write(chr(0x0D))
    usbus()


while sys==0:
    if GPIO.input(26) == 1:
        sys=1#GPIOピンの26番に1が入力されたらsysに1を入れる
        for i in range(120):
            #起動信号を120回繰り返す
            don()

        for i in range(dupcount):
            #上昇信号を400回繰り返す
            dup()

while sys==1:
    latnum=latn+lats
    lonnum=lone+lonw
    lonlat=latnum+lonnum

    if lonlat==4:#両方向に移動後
        if GPIO.input(16) == 1:#下降
            for i in range(dhovercount):
                #ホバリング
                dhover()

            for i in range(dhovercount):
                #下降
                ddown()
        else:
            if GPIO.input(19) == 1:
                latnum=0
                latn=0
                lats=0
                lonnum=0
                lone=0
                lonw=0
                lonlat=0
            else:
                for i in range(dhovercount):
                    #ホバリング
                    dhover()
    else:
        if latnum == 2:
            latnum = 2
        elif GPIO.input(20) == 1:#北に行く
            latn=1
            for i in range(dgocount):
                dgono()
        else:#南行く
            lats=1
            for i in range(dgocount):
                dgoso()


        if lonnum==2:
            lonnum=2
        elif GPIO.input(21) == 1:#東に行く
            lone=1
            for i in range(dgocount):
                dgoea()
        else:#西に行く
            lonw=1
            for i in range(dgocount):
                dgowe()
