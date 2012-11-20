#!/usr/bin/env python

import argparse
import sys


def parseInput(in_type, in_num):
    if (in_type == 'bh' or in_type == 'bd'):
        try:
            int(in_num, 2)
            return True
        except ValueError:
            return False
    elif (in_type == 'hb' or in_type == 'hd'):
        try:
            int(in_num, 16)
            return True
        except ValueError:
            return False
    elif (in_type == 'dh' or in_type == 'db'):
        return True
    else:
        return False

parser = argparse.ArgumentParser(description="Converts bin/hex/dec numbers, does not work for negatives or floats   ")
parser.add_argument('direction',
    metavar='type',
    default='hd',
    help='Specifies the conversion method, decimal to binary (db), decimal to hex (db), hex to bin (hb), hex to dec (hd), bin to dec (bd), bin to hex (bh)')
parser.add_argument('input',
    metavar='input',
    type=int,
    help="Input number, must match the conversion-to base (don't need 0x for hex)")
args=parser.parse_args()

cnvt_type = args.direction


if (parseInput(cnvt_type, str(args.input))):
    if (cnvt_type == 'bh'):
        print 'IN (bin): ' + str(args.input)
        print 'OUT (hex): ' + hex(int(str(args.input), 2))
    elif (cnvt_type == 'bd'):
        print 'IN (bin): ' + str(args.input)
        print 'OUT (dec): ' + int(str(args.input), 2)
    elif (cnvt_type == 'dh'):
        print 'IN (dec): ' + str(args.input)
        print 'OUT (hex): ' + hex(args.input)
    elif (cnvt_type == 'db'):
        print 'IN (dec): ' + str(args.input)
        print 'OUT (bin): ' + bin(args.input)
    elif (cnvt_type == 'hd'):
        print 'IN (hex): ' + str(args.input)
        print 'OUT (dec): ' + str(int(str(args.input), 16))
    elif (cnvt_type == 'hb'):
        print 'IN (hex): ' + str(args.input)
        print 'OUT (bin): ' + str(int(str(args.input), 2))
else:
    sys.exit("Invalid conversion type")