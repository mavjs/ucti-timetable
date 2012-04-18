About
=====
* This is a python script to download timetable for UCTI students.
* It is very minimal and make use of standard python libraries.
* It has only been tested on Fedora 16, but it should nonetheless work on GNU/Linux and nix systems.
* [NOTE] it has never been tested on a Microsoft Windows.


License
=======
* This script is licensed as GPLv3 - "GNU GENERAL PUBLIC LICENSE" version 3.
* The copy of the license is included with the source code.

Requirements
============
* Need BeautifulSoup_. [This is the only external library I've ever needed though.]

.. _BeautifulSoup: http://www.crummy.com/software/BeautifulSoup

Usage
=====
Either execute the script as,
::
    ~# python ucti-timetable.py

or make it executable and use,
::
    ~# chmod +x ucti-timetable.py

Executing the script with the "-h" or "--help" option should show you this help;
::
    Usage: ucti-timetable.py [options]

    Options:
    -h, --help                  show this help message and exit
    -I INTAKE, --intake=INTAKE  Your UCTI Intake Code (e.g. UC1F1101IT)
    -W WEEK, --week=WEEK        The date of Monday of the week, should be in the form of YYYY-MM-DD. (e.g. 2012-01-26)

Bugs / Features
===============
* If you find bugs, please do submit it at this repos's issues_. page, and label it with #bug.
* If you would like new features, submit it at issues, but label it with #features.

* Got a new feature implemented? Make a pull request, so that we can all benefit from it. :)


.. _issues: https://github.com/mavjs/ucti-timetable/issues
