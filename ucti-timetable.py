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
from gi.repository import Gtk, WebKit
from BeautifulSoup import BeautifulSoup
from datetime import datetime, date, timedelta

class MyWindow(Gtk.Window):

    def __init__(self):
        """ to get current date time to parse later on. """
        self.now = datetime.now()
        self.year = datetime.date(self.now).isocalendar()[0]
        self.week = datetime.date(self.now).isocalendar()[1]

        """ initializing the GTK Window """
        Gtk.Window.__init__(self, title="UCTI Timetable Downloader")
        self.resize(400, 600)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)

        self.hbox = Gtk.Box(spacing=6)
        self.vbox.pack_start(self.hbox, False, True, 0)

        self.intake_label = Gtk.Label("Your intake: ")
        self.hbox.pack_start(self.intake_label, False, True, 10)

        self.intake = Gtk.Entry()
        self.hbox.pack_start(self.intake, True, True, 10)
        
        self.date_label = Gtk.Label("Date of the current week: ")
        self.hbox.pack_start(self.date_label, False, True, 10)

        self.date = self.monday_of_week()
        self.date_combox = Gtk.ComboBoxText()
        self.date_combox.append_text(self.date)

        self.hbox.pack_start(self.date_combox, False, True, 10)
        
        self.go = Gtk.Button(stock=Gtk.STOCK_APPLY)
        self.go.connect("clicked", self.on_button_clicked)
        self.hbox.pack_start(self.go, False, True, 10)

        self.scroller = Gtk.ScrolledWindow()
        self.browser = WebKit.WebView()
        self.browser.connect("title-changed", self.title_changed)
        self.scroller.add(self.browser)
        self.vbox.pack_end(self.scroller, True, True, 0)

    def monday_of_week(self):
        """ date of monday of the week parsing first. """
        d = date(self.year, 1, 1)    
        delta_days = d.isoweekday() - 1
        delta_weeks = self.week
        if self.year == d.isocalendar()[0]:
            delta_weeks -= 1
        # delta for the beginning of the week
        delta = timedelta(days=-delta_days, weeks=delta_weeks)
        weekbegin = d + delta
        return str(weekbegin)

    def on_button_clicked(self, widget):
        if not (self.intake.get_text() is None and self.date_combox.get_active_text() is None):
            print self.intake.get_text().upper()
            print self.date_combox.get_active_text()
            html_to_load = self.strip_crappy_stuff()
            self.browser.load_string(str(html_to_load), "text/html", "UTF-8", "")

    def title_changed(self, webview, frame, title):
        self.set_title(title)

    def strip_crappy_stuff(self):
        request = urllib2.Request('http://webspace.apiit.edu.my/schedule/intakeview_intake.jsp?Intake1=' + self.intake.get_text().upper() + '&Submit=Submit&Week=' + self.date_combox.get_active_text())
        request.add_header('User-Agent', \
                'ucti-timetable.py/1.0 (+https://github.com/mavjs/ucti-timetable)')
        opener = urllib2.build_opener()
        html = opener.open(request).read()
        parse_html = BeautifulSoup(html)
        final_html = parse_html.find('table', {'border': '1'}).prettify()
        return final_html

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
