#!/usr/bin/env python

# RDriveDiary, a driving diary CGI thingy

# Copyright Eetu "Razbit" Pesonen, 2015
#
# This file is part of RDriveDiary.
# 
# RDriveDiary is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# RDriveDiary is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with RDriveDiary.  If not, see <http://www.gnu.org/licenses/>.

import cgi

def print_head():
    print("<head>")
    print("<title>CGI</title>")

    print("</head>")

def print_body():
    print("<body>")
    print("<h1>HALLO</h1>")

    print("</body>")


# -- ENTRY -- #

print("Content-Type: text/html")
print("")

print('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" \
"http://www.w3.org/TR/html4/strict.dtd">')
print("<html>")

print_head()
print_body()


print("</html>")
