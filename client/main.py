"""
Main entry point for the program.
"""

import sys
import os

# setup to properly import later on.

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

if __name__ == '__main__':
    from client.app.app import main
    main()