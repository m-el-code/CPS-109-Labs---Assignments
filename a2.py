#Manar Elbeshbishy
#Assignment 2

def only_odd_digits(n):
    num = str(n)
    for x in range(len(num)):
        if (int(num[x])) % 2 != 0:
            odd = True
        else:
            odd = False
            break
    return odd

def riffle(items, out=True):
    mid = len(items)//2
    half1 = items[:mid]
    half2 = items[mid: ]
    newList = []
    for i in range(mid):
        x = half1[i]
        y = half2[i]
        if out == True:
            newList.append(x)
            newList.append(y)
        if out == False:
            newList.append(y)
            newList.append(x)
    return newList

def is_cyclops(n):
    num = str(n)
    size = len(num)
    mid = size//2
    if size %2 != 0 and num.count('0') == 1 :
        if (int(num[mid])) == 0:
            return True
        else:
            return False
    else:
        return False
    
def colour_trio(colours):
    while len(colours) > 1:
        newColours = ''
        first = 0
        second = 1
        for x in range(len(colours)-1):
            if colours[first] == 'r':
                    
                if colours[second] == 'r':
                    newColours = newColours + 'r'
                    
                elif colours[second] == 'y':
                    newColours = newColours + 'b'
                        
                elif colours[second] == 'b':
                    newColours = newColours + 'y'
                
            elif colours[first] == 'y':
                
                if colours[second] == 'r':
                    newColours = newColours + 'b'
                    
                elif colours[second] == 'y':
                    newColours = newColours + 'y'
                    
                elif colours[second] == 'b':
                    newColours = newColours + 'r'
                
            elif colours[first] == 'b':
                    
                if colours[second] == 'r':
                    newColours = newColours + 'y'
                    
                elif colours[second] == 'y':
                    newColours = newColours + 'r'
                    
                elif colours[second] == 'b':
                    newColours = newColours + 'b'
                
            first += 1
            second += 1
        
        colours = newColours

    return colours

def extract_increasing(digits):
    current = 0
    previous = -1
    newList = []
    for d in digits:
        current = 10*current + int(d)
        if current > previous:
            newList.append(current)
            previous = current
            current = 0
        if current < previous:s
            continue

    return newList

def expand_intervals(intervals):
    intervalsList = intervals.split(",")
    newList = []
    if intervals=='':
        return newList
    else:
        for x in intervalsList:
            numRange = x.split("-")
            if len(numRange) == 2:
                newList += range(int(numRange[0]), int(numRange[1])+1)
            elif len(numRange) == 1:
                newList.append(int(numRange[0]))
        return newList

def is_ascending(items):
    for x in range(len(items)-1):
        if items[x] >= items[x+1]:
            return False
    else:
        return True
    
def count_and_say(digits):
    newList = ''
    if digits == '':
        return newList
    if digits != '':
        prev = digits[0]
        count = 1
        for x in digits[1:]:
            if prev == x:
                count += 1
                prev = x
            if prev != x:
                newList =newList + str(count) + prev
                prev = x
                count = 1
        newList = newList + str(count) + prev
        return newList

def reverse_vowels(text):
    vowels = 'aeiouAEIOU'
    subList = []
    newText = ''
    for x in text[::-1]:
        if x in vowels:
            subList.append(x)
    for x in text:
        if x in vowels:
            if x.isupper():
                newText = newText + subList[0].upper()
                subList.remove(subList[0])
            else:
                newText = newText + subList[0].lower()
                subList.remove(subList[0])
        else:
            newText = newText + x

    return newText

def safe_squares_rooks(n, rooks):
    row = set()
    col = set()
    
    for x in rooks:
        row.add(x[0])
        col.add(x[1])
        
    lengthRows = len(row)
    lengthCols = len(col)
    
    safeRows = n - lengthRows
    safeCol = n - lengthCols
    safeSquares = safeRows * safeCol
    
    return safeSquares