# -*- coding: utf-8 -*-
import time
import serial
import RPi.GPIO as GPIO

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=100000, bytesize=serial.EIGHTBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(16, GPIO.IN)
xo=0
xi=0
xa=0
yo=0
yi=0
ya=0
za=0
a=0
sys=0
#色々な設定
while sys==0:
    if GPIO.input(21) == 1:
        sys=1#GPIOピンの21番に1が入力されたらsysに1を入れる
        for i in range(120):
            #起動信号を690回繰り返す
            ser.write(chr(0x0F))
            ser.write(chr(0x60))
            ser.write(chr(0x01))
            ser.write(chr(0x35))
            ser.write(chr(0xA8))
            ser.write(chr(0x41))
            ser.write(chr(0x0D))
            ser.write(chr(0x16))
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
            ser.write(chr(0x40))
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
        for i in range(690):
            #上昇信号を69回繰り返す
            ser.write(chr(0x0F))
            ser.write(chr(0x00))
            ser.write(chr(0x04))
            ser.write(chr(0xE0))
            ser.write(chr(0xC0))
            ser.write(chr(0x00))
            ser.write(chr(0x08))
            ser.write(chr(0x16))
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
            ser.write(chr(0x40))
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
while sys==1:
    if GPIO.input(20) == 1:
        xo=1#GPIOピンの20番に1が入力されたらx0に1を入れる
    else:
        xi=1
    xa=xo+xi
    if GPIO.input(16) == 1:
        yo=1#GPIOピンの16番に1が入力されたらyoに1を入れる
    else:
        yi=1
    ya=yo+yi
    za=xa+ya
    if xa==2:
        xa=0
    elif xo==1:#xが1なら前(北)に進む
        for i in range(10):
            #前向き信号1/4を69回繰り返す
            ser.write(chr(0x0F))
            ser.write(chr(0x60))
            ser.write(chr(0x05))
            ser.write(chr(0x20))
            ser.write(chr(0x00))
            ser.write(chr(0x01))
            ser.write(chr(0x08))
            ser.write(chr(0x16))
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
            ser.write(chr(0x40))
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
    else:#xが1以外(0)なら後ろ(南)に進む
        for i in range(10):
            #後ろ向き信号1/4を69回繰り返す
            ser.write(chr(0x0F))
            ser.write(chr(0x9C))
            ser.write(chr(0x02))
            ser.write(chr(0x20))
            ser.write(chr(0x00))
            ser.write(chr(0x01))
            ser.write(chr(0x08))
            ser.write(chr(0x16))
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
            ser.write(chr(0x40))
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
    if ya==2:
        ya=0
    elif yo==1:#yが1なら右(東)に進む
        for i in range(10):
            #右向き信号1/4を69回繰り返す
            ser.write(chr(0x0F))
            ser.write(chr(0x00))
            ser.write(chr(0x04))
            ser.write(chr(0x2B))
            ser.write(chr(0x00))
            ser.write(chr(0x01))
            ser.write(chr(0x08))
            ser.write(chr(0x16))
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
            ser.write(chr(0x40))
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
    else:#yが1以外(0)なら左(西)に進む
        for i in range(10):
            #左向き信号1/4を69回繰り返す
            ser.write(chr(0x0F))
            ser.write(chr(0x00))
            ser.write(chr(0xE4))
            ser.write(chr(0x14))
            ser.write(chr(0x00))
            ser.write(chr(0x01))
            ser.write(chr(0x08))
            ser.write(chr(0x16))
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
            ser.write(chr(0x40))
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
    #if z==1:#zが1なら停止(ホバリング)する
    for i in range(100):
        #ホバリングを69回繰り返す
        ser.write(chr(0x0F))
        ser.write(chr(0x00))
        ser.write(chr(0x04))
        ser.write(chr(0x20))
        ser.write(chr(0x00))
        ser.write(chr(0x01))
        ser.write(chr(0x08))
        ser.write(chr(0x16))
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
        ser.write(chr(0x40))
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
    if za == 4:
        for i in range(690):
            #ホバリングを69回繰り返す
            ser.write(chr(0x0F))
            ser.write(chr(0x00))
            ser.write(chr(0x04))
            ser.write(chr(0x20))
            ser.write(chr(0x00))
            ser.write(chr(0x01))
            ser.write(chr(0x08))
            ser.write(chr(0x16))
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
            ser.write(chr(0x40))
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
        for i in range(900):
            #ホバリングを69回繰り返す
            ser.write(chr(0x0F))
            ser.write(chr(0x00))
            ser.write(chr(0x04))
            ser.write(chr(0x20))
            ser.write(chr(0x45))
            ser.write(chr(0x01))
            ser.write(chr(0x08))
            ser.write(chr(0x16))
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
            ser.write(chr(0x40))
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
