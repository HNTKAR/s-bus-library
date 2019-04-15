# -*- coding: utf-8 -*-
import time

sbuschs=[0,0,0,0]
sbuschs[0]=0x550
sbuschs[1]=0x400
sbuschs[2]=0x400
sbuschs[3]=0x400
sbusbytes=[0,0,0,0,0,0]

sbusbytes[0]=sbuschs[0] & 0xFF
sbusbytes[1]=(sbuschs[0]>>8) | ((sbuschs[1]&0x1F)<<3)
# print (hex(sbusbytes[0]))
sbusbytes[2]=(sbuschs[1]>>5) | ((sbuschs[2]&0x03)<<6)
sbusbytes[3]=((sbuschs[2]&0x3FC)>>2)
sbusbytes[4]=(sbuschs[2]>>10) | ((sbuschs[3]&0x7F)<<1)
sbusbytes[5]=(sbuschs[3]>>7) | 00000000
for i in range(6):
    print (hex(sbusbytes[i]))
