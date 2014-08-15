#!/usr/bin/env python
# -*- coding: utf-8 -*-

class create_gist:

    def create(self, fields):
        r = requests.post("https://api.github.com/gists",
                          data=json.dumps(fields),
                          headers={'user-agent':client.name})
        return r.json()
    def create(self, key, fields):
        r = requests.post("https://api.github.com/gists",
                           data=json.dumps(fields),
                           headers={'user-agent':client.name},
                           auth=(key,'x-oauth-basic'))
        return r.json()
