#!/usr/bin/env python3

import urllib.request

link = "https://www.dev.home-appliances.philips/occ/v2/versuni-b2c-dk/sitemap.xml"
f = urllib.request.urlopen(link)
myfile = f.read()
print(myfile)
