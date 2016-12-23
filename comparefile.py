import os
import itertools

#compare target file to base
#prints:
#   number and percentage of lines found in target that match base
#   longest consecutive run of matched lines
#   if verbose, prints all matched lines
def compare(base, target, verbose):
    bf = open(base, 'r')
    tf = open(target)

    #print "Base:"
    
    baseLines = []
    for line in bf:
        line = simplifyLine(line)
        #skip empty lines
        if line:
            baseLines.append(line)
            #print line

    lineNum = 0 #current line number
    lineCount = 0 #does not include empty lines
    linesMatched = 0
    maxConsecutive = 0
    maxConsecutiveStartsAt = 0
    curConsecutive = 0
    curConsecutiveStartsAt = 0
    matches = []
    
    #print "Target:"
    for line in tf:
        lineNum += 1
        simpleLine = simplifyLine(line)
        #skip empty lines
        if simpleLine:
            #print simpleLine
            lineCount += 1
            matched = False
            for baseLine in baseLines:
                if baseLine == simpleLine:
                    matched = True
                    linesMatched += 1
                    curConsecutive += 1
                    if curConsecutiveStartsAt == 0:
                        curConsecutiveStartsAt = lineNum
                    if curConsecutive > maxConsecutive:
                        maxConsecutive = curConsecutive
                        maxConsecutiveStartsAt = curConsecutiveStartsAt
                    #remove from baseLines, shouldn't match it again!
                    baseLines.remove(baseLine)
                    if verbose:
                        matches.append(str(lineNum) + '\t' + line.rstrip())
                    break
            if not matched:
                curConsecutive = 0
                curConsecutiveStartsAt = 0

    percentage = round(100.0 * linesMatched / lineCount, 2)
    print str(linesMatched) + " of " + str(lineCount) + " lines matched (" + str(percentage) + "%)"
    
    if linesMatched > 0:
        if maxConsecutive > 1:
            #this is wrong, doesn't account for skipped lines
            #lastConsecutive = maxConsecutiveStartsAt + maxConsecutive - 1
            consecutivePercentage = round(100.0 * maxConsecutive / lineCount, 2)
            #print str(maxConsecutive) + " consecutive lines (" + str(maxConsecutiveStartsAt) + "-" + str(lastConsecutive) + ", " + str(consecutivePercentage) + "%)"
            print str(maxConsecutive) + " consecutive lines (" + str(consecutivePercentage) + "%)"
        if verbose:
            print
            for line in matches:
                print line
            

#strips whitespace and converts to lowercase
def simplifyLine(str):
    str = str.strip()
    str = str.lower()
    #should we also strip spaces within lines?
    #would catch lines like "a=1"-"a = 1"
    str = str.replace(' ','')
    return str

#
