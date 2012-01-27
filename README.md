About
====
* This is a python script to download timetable for UCTI students.
* It is very minimal and make use of standard python libraries.
* It has only been tested on Fedora 16, but it should nonetheless work on GNU/Linux
and *nix systems.
* [NOTE] it has never been tested on a Microsoft Windows.


License
=======
* This script is licensed as GPLv3 - "GNU GENERAL PUBLIC LICENSE" version 3.
* The copy of the license is included with the source code.


Usage
====
Either execute the script as,

<code>~# python ucti-timetable.py</code>

or make it executable and use,

<code>~# chmod +x ucti-timetable.py</code>


Executing the script with the "-h" or "--help" option should show you this help;

<pre>
Usage: ucti-timetable.py [options]

Options:
  -h, --help            show this help message and exit
  -I INTAKE, --intake=INTAKE
                        Your UCTI Intake Code (e.g. UC1F1101IT)
  -W WEEK, --week=WEEK  The date of Monday of the week, should be in the form
                        of YYYY-MM-DD. (e.g. 2012-01-26)
</pre>
