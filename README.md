ios-bookmark-export
===================

iOS bookmark exporter. Turns iOS bookmarks into a standard bookmark HTML file that can be imported into other browsers.

To export bookmarks from an iOS device:

1. Back up the iOS device to a Mac.
2. Use iPhone Backup Extractor ( http://www.iphonebackupextractor.com/ ) to extract the bookmark database (bookmarks.db) from /Library/Safari
3. Run bm.py > bookmarks.html in the directory that the bookmarks.db is in.
4. Import those bookmarks into another browser.
