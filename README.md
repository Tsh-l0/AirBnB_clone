AirBnB clone - The console
=============================

This is a project to manipulate a powerful storage system built as a CLI (Command Line Interpreter). 

In order to run this program use the command "./console.py"
In the interactive mode the program looks like this:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

In the non-interactive mode the program looks like this:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

USAGE
========================================================
Inside the console, you can perform the following actions:

    Create new objects (e.g., User, Place, Amenity).
    Show information about objects.
    Update existing objects.
    Delete objects.

Run echo "help" | ./console.py to see list of available command
Run echo "help <command>" | ./console.py to see what a command does.

Unittests
====================
Interactive Mode:
python3 -m unittest discover tests

Non-interactive mode:
$ echo "python3 -m unittest discover tests" | bash
