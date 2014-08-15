#!/usr/bin/env python
# -*- coding: utf-8 -*-

class get_gist:

    def get(self, gist_id):
        r = requests.get("https://api.github.com/gists/"+gist_id)
        return r.json()
    def get(self, key,  gist_id):
        r = requests.get("https://api.github.com/gists/"+gist_id,
                         auth=(key,'x-oauth-basic'))
        return r.json()
