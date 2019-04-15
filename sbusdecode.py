# -*- coding: utf-8 -*-
import time
sbusbytes=[0,0,0,0,0,0]
sbusbytes[0]=0x0
sbusbytes[1]=0x04
sbusbytes[2]=0x20
sbusbytes[3]=0x00
sbusbytes[4]=0x41
sbusbytes[5]=0x0d
sbuschs=[0,0,0,0]



sbuschs[0]=sbusbytes[0] | ((sbusbytes[1] & 0x7)<<8)
sbuschs[1]=((sbusbytes[1]>>3) | ((sbusbytes[2]&0x3F)<<5))
sbuschs[2]=(sbusbytes[2]>>6) | (sbusbytes[3]<<2) | ((sbusbytes[4] & 0x1)<<10)
sbuschs[3]=((sbusbytes[4]>>1) | ((sbusbytes[5]&0x0F)<<7))
for i in range(4):
    print (hex(sbuschs[i]))


# hover
#
# ser.write(chr(0x00))
# ser.write(chr(0x04))
# ser.write(chr(0x20))
# ser.write(chr(0x00))
# ser.write(chr(0x01))
# ser.write(chr(0x08))
