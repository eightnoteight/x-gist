#!/usr/bin/env python
# -*- coding: utf-8 -*-

class struct(dict):
	def __init__(self, **kwargs):
		super(struct, self).__init__(**kwargs)
		self.__dict__ = self
client = struct(name="x-gist",
				url ="https://github.com/eightnoteight/x-gist")