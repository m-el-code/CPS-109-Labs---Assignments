#LAB 8
#Manar Elbeshbishy


#question 1
def add(a,b):
    if b == 1:
        return a + 1
    else:
        return 1 + add(a,b-1)

print("QUESTION 1")
print(add(5,9), "\n")

#question 2
def log2(x):
    if x <= 1:
        return 0
    else:
        return 1 + log2(x//2)

print("QUESTION 2")
print(log2(8), "\n")

#question 3
def reverse(sentence):
    if sentence == "":
        return sentence
    else:
        return reverse(sentence[1:]) + sentence[0]

print("QUESTION 3")
print(reverse('Who let the dogs out?'), "\n")

#question 4
def power(x,n):
    if n == 0:
        return 1 
    else:
        return x * power(x, n-1)

print("QUESTION 4")    
print(power(2,10), "\n")

#question 5
def power(x,n): 
    global countcalls
    countcalls +=1
    if n == 0:
        return 1 
    else:
        return (x * power(x, n-1))
    
print("QUESTION 5")
countcalls = 0
print(power(2,10), "- Coutner: ", countcalls)
countcalls = 0
print(power(5,10), "- Counter: ", countcalls)
countcalls = 0
print(power(5,0), "- Counter: ", countcalls, "\n")

#question 6
def powerHalf(x,n):
    global countcalls
    countcalls += 1
    if n == 0:
        return 1
    if n % 2 == 0:
        return powerHalf(x,n/2)**2
    else:
        return x * powerHalf(x,n-1)
print("QUESTION 6")
countcalls = 0 
print(powerHalf(2, 10), "- Counter: ", countcalls)
countcalls = 0 
print(powerHalf(5,10), "- Counter: ", countcalls)
countcalls = 0
print(powerHalf(5,0), "- Counter: ", countcalls, "\n")

#question 7
print("QUESTION 7")
f = open('kdpF.txt') #opens file for reading
line = f.readline() #reads a single line
print(line)
seq = ''
for line in f: #reads the rest of the lines
    seq = seq + line
seq = seq.replace('\n', '') #removes the newline characters
seq = seq.upper()
print(seq)

def gcContent(sequence):
    count = 0
    for x in sequence:
        if x == 'G' or x == 'C':
            count += 1
    percent = (count/(len(sequence)))* 100
    return percent

print("\ngc Content Percentage: ", gcContent(seq), "%")
