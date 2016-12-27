# Usage: python labcompare.py compare base target
from __future__ import print_function
import comparefile
import sys

def compare(base, target, verbose):
    r = comparefile.compare(base, target, verbose)
    p = "{0:.2f}".format(100.0 * r["percentage"])
    print(r["linesMatched"], " of ", r["lineCount"], " lines matched (", p, "%)", sep="")
    if r["linesMatched"] > 0:
        cp = "{0:.2f}".format(100.0 * r["consecutivePercentage"])
        print(r["maxConsecutive"], " consecutive lines at ", r["maxConsecutiveStartsAt"], " (", cp, "%)", sep="")
        if verbose:
            print()
            for line in r["matches"]:
                print(line)

    
def printUsage():
    print("Usage:")
    print("labcompare.py compare base target [verbose]")


if __name__ == "__main__":
    if sys.argv[1].lower() == "compare":
        if len(sys.argv) == 4:
            compare(sys.argv[2], sys.argv[3], True)
        elif len(sys.argv) > 4:
            verbose = True
            v = sys.argv[4]
            if (v=="f") or (v=="false") or (v=="n") or (v=="no"):
                verbose = False
            compare(sys.argv[2], sys.argv[3], verbose)
        else:
            printUsage()
    else:
        printUsage()