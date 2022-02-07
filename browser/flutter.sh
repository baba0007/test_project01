#!/bin/sh

#kill $(ps aux | grep "Safari")
kill ps aux | grep "Chrome"
python3 /Users/babadialo/Documents/python/wing/browser/browser-script.py /Users/babadialo/Documents/python/wing/browser/websites.txt chrome
exit 0

