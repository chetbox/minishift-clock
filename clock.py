#!/usr/bin/env python

import minishift
import time
from argparse import ArgumentParser

def show_time(number_of_minishifts, offset):
	width = 8 * number_of_minishifts
	ms = minishift.Minishift(minishift.MCP2210Interface(0x04d8, 0xf517), width)

	while (True):
		for i in range(width):
			ms.canvas[i] = 0
		ms.canvas.write_text(offset, time.strftime('%H:%M'))
		ms.update()
		time.sleep(1)

if __name__ == '__main__':
	arg_parser = ArgumentParser(description='Show a clock on your Minishift')
	arg_parser.add_argument('number_of_minishifts', type=int, help='How many Minishifts you have connected')
	arg_parser.add_argument('--offset', type=int, default=0, help='Number of pixels of left padding')
	args = arg_parser.parse_args()

	show_time(args.number_of_minishifts, args.offset)
