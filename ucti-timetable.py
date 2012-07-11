#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Copyright (C) 2012 Maverick JS <mavjs01@gmail.com>
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.

import urllib2
import os
import sys
import webbrowser
import argparse
from BeautifulSoup import BeautifulSoup


def main(argv=None):
    " Arguments to go together with the program "
    parser = argparse.ArgumentParser(description='Download your intake \
            timetable for the week from UCTI.', version='0.5')
    parser.add_argument('-I', '--intake', dest='intake', action='store', \
            default='', help='Your UCTI Intake Code (e.g. UC1F1101IT)')
    parser.add_argument('-W', '--week', dest='week', action='store', \
            default='', help='The date of Monday of the week, should be in \
            the form of YYYY-MM-DD. (e.g. 2012-01-26)')

    " Just tring to make things easier "
    args = parser.parse_args()

    if (args.intake and args.week) == '':
        print(parser.print_help())
        return(0)
    elif args.intake == '':
        print(parser.print_help())
        return(0)
    elif args.week == '':
        print(parser.print_help())
        return(0)
    else:
        intake = args.intake
        week = args.week

    base_url = 'http://webspace.apiit.edu.my/schedule/intakeview_intake.jsp?'
    storage = 'UCTI-Timetable'
    home_path = os.path.expanduser('~')
    storage_dir = os.path.join(home_path, storage)
    storage_file = os.path.join(storage_dir, intake + '-' + week + '.html')

    print('Your intake: %s' % intake)
    print('Week: %s' % week)
    print('Folder for all your timetable files will be at: %s' % storage_dir)
    print('The file will be at: %s' % storage_file)
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)
        req = urllib2.urlopen(base_url + 'Intake1=' + intake + \
                '&Submit=Submit&Week=' + week)
        html = req.read()
        parse_html = BeautifulSoup(html)
        final_html = parse_html.find('table', {'border': '1'})
        f = file(storage_file, 'w')
        f.write(str('<!DOCTYPE html>\n<html>\n<body>\n'))
        f.write(str(final_html))
        f.write(str('\n</body>\n</html>'))
        f.close()
        try:
            browser = webbrowser.get('firefox')
        except webbrowser.Error:
            browser = webbrowser
        print('Opening the browser...')
        browser.open(storage_file)

    elif os.path.exists(storage_dir):
        if os.path.isfile(storage_file):
                try:
                    browser = webbrowser.get('firefox')
                except webbrowser.Error:
                    browser = webbrowser
                print('Opening the browser...')
                browser.open(storage_file)
        elif not os.path.isfile(storage_file):
            req = urllib2.urlopen(base_url + 'Intake1=' + intake + \
                    '&Submit=Submit&Week=' + week)
            html = req.read()
            parse_html = BeautifulSoup(html)
            final_html = parse_html.find('table', {'border': '1'})
            f = file(storage_file, 'w')
            f.write(str('<!DOCTYPE html>\n<html>\n<body>\n'))
            f.write(str(final_html))
            f.write(str('\n</body>\n</html>'))
            f.close()
            try:
                browser = webbrowser.get('firefox')
            except webbrowser.Error:
                browser = webbrowser
            print('Opening the browser...')
            browser.open(storage_file)
    return(0)

if __name__ == '__main__':
    sys.exit(main())
