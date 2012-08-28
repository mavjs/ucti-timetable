About
=====
* This is a python script to download timetable for UCTI students.
* It is very minimal and make use of standard python libraries.
* It has only been tested on Fedora 16/17, but it should nonetheless work on GNU/Linux and nix systems that has GTK+ 3.
* [NOTE] It can only be used with GTK+ 3 therefore doesn't work with Microsoft Windows.

License
=======
* This script is licensed as GPLv3 - "GNU GENERAL PUBLIC LICENSE" version 3.
* The copy of the license is included with the source code.

Requirements
============
* Need BeautifulSoup_. [This is the only external library I've ever needed though.]

.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup

* If you have `pip <http://www.pip-installer.org/>`_ - a tool for installing and managing Python packages installed. You can install BeautifulSoup with pip, like this::

    ~# pip install -r requirements.txt
* [NOTE] The 'requirements.txt' file is included in the repository.

Usage
=====
Either execute the script as,
::
    ~# python ucti-timetable.py

or make it executable and use,
::
    ~# chmod +x ucti-timetable.py

Bugs / Features
===============
* If you find bugs, please do submit it at this repos's issues_. page, and label it with #bug.
* If you would like new features, submit it at issues, but label it with #features.

* Got a new feature implemented? Make a pull request, so that we can all benefit from it. :)


.. _issues: https://github.com/mavjs/ucti-timetable/issues
