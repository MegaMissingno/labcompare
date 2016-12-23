# Usage: python labcompare.py base target
import comparefile
import sys

if __name__ == "__main__":
    comparefile.compare(sys.argv[1],sys.argv[2], True)

