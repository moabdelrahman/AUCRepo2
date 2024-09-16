f = open("words.txt",'r')
vowles = 'aeiou'
maxlength = 0
maxword = ""
c = 0
letterCount = 0
for line in f:
    line = line.strip()
    L = len(line)
    letterCount = letterCount + L
    if L > maxlength:
        maxlength = L
        maxword = line
    if line[-1] == 's':
        print(line)
        c = c+1
    elif line[0] in vowles:
        print('an', line)
    else:
        print('a', line)
print("the longest word is :",maxword)
print('no of plural words = ',c)
print('file has ', letterCount, 'letters')
