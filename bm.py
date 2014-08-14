#!/usr/bin/env python

import sqlite3
import cgi

n = sqlite3.connect('Bookmarks.db')
c = n.cursor()


print """<!DOCTYPE NETSCAPE-Bookmark-file-1>
    <!--This is an automatically generated file.
    It will be read and overwritten.
    Do Not Edit! -->
    <Title>Bookmarks</Title>
    <H1>Bookmarks</H1>
"""
print "<DL>"
for row in c.execute('select url, title from bookmarks'):
	if row[0] == None or row[1] == None:
		continue
	print "<DT><A HREF=\"%s\" ADD_DATE=\"1\" LAST_VISIT=\"1\" LAST_MODIFIED=\"1\">%s</A>\n" % (
		cgi.escape(row[0].encode('utf-8')), cgi.escape(row[1].encode('utf-8')))

print "</DL>"
