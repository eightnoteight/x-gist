#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import requests

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--login',
						dest='login',
						default=False,
						action='store_true',
						help="login with github account")
	parser.add_argument('')
def main():
	'''
	'''
	args = parse_args()
if __name__ == '__main__':
	main()