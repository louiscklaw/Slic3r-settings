#!/usr/bin/env python3

import os,sys,re
import math


START_TEMP=210; END_TEMP=193

START_SPEED=65; END_SPEED=200
LAYER_START=3; LAYER_END=START_TEMP-(END_TEMP-1)
LAYER_END+=3

SCALE_SPEED = math.ceil((END_SPEED - START_SPEED)/(LAYER_END-LAYER_START))

RAMP_TEMP = list(range(START_TEMP,END_TEMP,-1))
RAMP_LAYER = list(range(LAYER_START, LAYER_END, 1))
RAMP_SPEED = list(range(START_SPEED, END_SPEED, SCALE_SPEED))

RAMP_TEMP.append(END_TEMP)
RAMP_SPEED.append(END_SPEED)
RAMP_LAYER.append(RAMP_LAYER[-1]+1)
from pprint import pprint
# pprint(len(list(RAMP_TEMP)))
# pprint(len(list(RAMP_LAYER)))
# pprint(len(list(RAMP_SPEED)))
# sys.exit()


print(';RAMP START')
print('{if layer_num < 2}')
print('   M220 S65')
print('   M104 S210')
for temperature, layer, speed in zip(RAMP_TEMP, RAMP_LAYER, RAMP_SPEED):
  print('{elsif layer_num < '+str(layer)+'}')
  print(f'   ; M118 setting change: T{temperature} L{layer} S{speed}')
  print('   M220 S'+str(speed))
  print('   M104 S'+str(temperature))
  print()

print('{else}')
print('   M118 RAMPING DONE')
print('{endif}')