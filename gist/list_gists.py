#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from requests.auth import HTTPBasicAuth
class list_gists:
    def get_all(self, key):
        r = requests.get("https://api.github.com/gists", 
                          auth=(key,'x-oauth-basic'))
        return r.json()
    def get(self, username):
        """docstring for get_pub"""
        r = requests.get("https://api.github.com/users/"+username+"/gists")
        return r.json()
    def get_pub(self, key):
        """docstring for get_pub"""
        r = requests.get("https://api.github.com/gists/public",
                         auth=(key,'x-oauth-basic'))
        return r.json()
    def get_pri(self, key):
        pass
    def get_starred(self, key):
        r = requests.get("https://api.github.com/gists/starred",
                        auth=(key,'x-oauth-basic'))
        return r.json()
