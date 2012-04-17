#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 Maverick JS <mavjs01@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version. 
# 
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details. 
# 
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import urllib2
import os
import sys
import webbrowser
from optparse import OptionParser
from BeautifulSoup import BeautifulSoup

def main(argv=None):
   
    parser = OptionParser()
    parser.add_option("-I", "--intake", dest="intake", default="", help="Your UCTI Intake Code (e.g. UC1F1101IT)")
    parser.add_option("-W", "--week", dest="week", default="", help="The date of Monday of the week, should be in the form of YYYY-MM-DD. (e.g. 2012-01-26)")
    
    (options, args) = parser.parse_args()
    intake = options.intake
    week = options.week

    if len(intake) == 0 and len(week) == 0:
        print("\nYou have not supplied any information regarding your \"Intake\" and or \"Week\".\n")
        print(parser.print_help())
        return(1)
    if len(intake) == 0:
        print("\nYou have not supplied any information about your intake.\n")
        print(parser.print_help())
        return(1)
    if len(week) == 0:
        print("\nYou have not supplied any information about the week.\n")
        print(parser.print_help())
        return(1)
    
    base_url = 'http://webspace.apiit.edu.my/schedule/intakeview_intake.jsp?'
    storage = 'UCTI-Timetable'
    home_path = os.path.expanduser('~')
    storage_dir = os.path.join(home_path, storage)
    storage_file = os.path.join(storage_dir, intake+"-"+week+".html")

    print("Your intake: %s" % intake)
    print("Week: %s" % week)
    print("Folder for all your timetable files will be at: %s" % storage_dir)
    print("The file will be at: %s" % storage_file)
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)
        req = urllib2.urlopen(base_url+"Intake1="+intake+"&Submit=Submit&Week="+week)
        html = req.read()
        parse_html = BeautifulSoup(html)
        final_html = parse_html.find("table", {"border": "1"})
        f = file(storage_file, 'w')
        f.write(str('<!DOCTYPE html>'))
        f.write(str('<html>'))
        f.write(str('<body>'))
        f.write(str('<table border=1 width=100% cellpadding=5 cellspacing=0>'))
        for line in final_html:
            f.write(str(line))
        f.write(str('</table>'))
        f.write(str('</body>'))
        f.write(str('</html>'))
        f.close()
        try:
            browser = webbrowser.get("firefox")
        except webbrowser.Error:
            browser = webbrowser
        print("Opening the browser...")
        browser.open(storage_file)

    elif os.path.exists(storage_dir):
        if os.path.isfile(storage_file):
                try:
                    browser = webbrowser.get("firefox")
                except webbrowser.Error:
                    browser = webbrowser
                print("Opening the browser...")
                browser.open(storage_file)
        elif not os.path.isfile(storage_file):
            req = urllib2.urlopen(base_url+"Intake1="+intake+"&Submit=Submit&Week="+week)
            html = req.read()
            parse_html = BeautifulSoup(html)
            final_html = parse_html.find("table", {"border": "1"})
            f = file(storage_file, 'w')
            f.write(str('<!DOCTYPE html>'))
            f.write(str('<html>'))
            f.write(str('<body>'))
            f.write(str('<table border=1 width=100% cellpadding=5 cellspacing=0>'))
            for line in final_html:
                f.write(str(line))
            f.write(str('</table>'))
            f.write(str('</body>'))
            f.write(str('</html>'))
            f.close()
            try:
                browser = webbrowser.get("firefox")
            except webbrowser.Error:
                browser = webbrowser
            print("Opening the browser...")
            browser.open(storage_file)
    return(0)

if __name__ == "__main__":
    sys.exit(main())
