# Program that reads or writes Employees from or to json format
# takes argument "read" or "write" followed by a file path in the command line
# Read finds a json list of employees from the file argument and prints descriptions
# Write puts a list of random specified number of employees in the file argument
# by Mitul Saha

import os
import sys
import argparse

from Lib.empRead import read
from Lib.empWrite import write
from Lib import LogHelper


def main():
    print("Starting employee read or write")

    parser = argparse.ArgumentParser(description='Parse employee input')
    parser.add_argument('-r', '--read', action='store_true',
                        help="if set, read from the specified filepath")
    parser.add_argument('-w', '--write', action='store_true',
                        help="if set, write to the specified filepath")
    parser.add_argument('-f-', "--filepath", action="store", dest="filepath",
                        help='takes filepath to be read from or written to')
    parser.add_argument('-n', '--numwrite', type=int,
                        help='number of random employees to write')
    args = parser.parse_args()

    if args.read == args.write:
        print("Must choose either --read or --write but not both")
        sys.exit(99)
    if not args.filepath.endswith(".json") and not args.filepath.endswith(".txt"):
        print("filepath must be of a json or txt file")
        sys.exit(99)
    try:
        f = open(args.filepath, "r")
        f.close()
    except Exception as e:
        print("%s is an invalid filepath; check the second argument" % args.filepath)
        print("Error message: " + str(e))
        sys.exit(99)

    path = os.path.dirname(os.path.realpath(__file__))
    logDir = path + "/UsageLog"
    logger = LogHelper.LogHelper(logDir, "Tester")
    logger.Info("Initial arg checks passed..")

    if args.read:
        try:
            read(args.filepath)
        except Exception as e:
            logger.Error("Error when reading: " + str(e))
            sys.exit(99)

        logger.Info("Read completed successfully")
    else:
        if args.numwrite is None or args.numwrite < 1:
            print("A positive integer arg (numwrite) is needed in write mode")
            sys.exit(99)

        try:
            write(args.filepath, args.numwrite)
        except Exception as e:
            logger.Error("Error when writing: " + str(e))

        logger.Info("Write completed successfully")


if __name__ == "__main__":
    main()
