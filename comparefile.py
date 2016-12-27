from __future__ import division
import os

#compare target file to base
#returns dict of the following:
#   linesMatched: number of identical lines
#   lineCount: number of lines counted (empty lines are skipped)
#   percentage: linesMatched/lineCount
#   maxConsecutive: longest run of consecutive lines matched.
#   maxConsecutiveStartsAt: line number of the above, first instance if there is a tie, omitted if no matches at all
#   matches: list of all matched lines, prefixed with line numbers, only if verbose is true and matches were found
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
    
    r = {}
    r["percentage"] = linesMatched / lineCount
    r["linesMatched"] = linesMatched
    r["lineCount"] = lineCount
    r["maxConsecutive"] = maxConsecutive

    if linesMatched > 0:
        #this is wrong, doesn't account for skipped lines
        #lastConsecutive = maxConsecutiveStartsAt + maxConsecutive - 1
        r["consecutivePercentage"] = maxConsecutive / lineCount
        r["maxConsecutiveStartsAt"] = maxConsecutiveStartsAt
        #print str(maxConsecutive) + " consecutive lines (" + str(maxConsecutiveStartsAt) + "-" + str(lastConsecutive) + ", " + str(consecutivePercentage) + "%)"
        if verbose:
            #print
            r["matches"] = matches
            #for line in matches:
                #print line
    
    return r


#strips whitespace and converts to lowercase
def simplifyLine(str):
    str = str.strip()
    str = str.lower()
    #should we also strip spaces within lines?
    #would catch lines like "a=1"-"a = 1"
    str = str.replace(' ','')
    return str