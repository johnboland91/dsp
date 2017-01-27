# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count < 10:
        print("Number of Donuts: " + str(count))
    else:
        print("Number of Donuts: many")



def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[0:2] + s[-2:]

def fix_start(s):
    return s[0] + "".join(["*" if s[0] == i else i for i in s[1:]])

def mix_up(a, b):          
    return b[0:2] + a[2:] + " " + a[0:2] + b[2:]          

def verbing(s):
    r = []
    if len(s) >= 3:
        if s[-3:] == "ing":
            r = list(s)
            r.append("ly")
            return "".join(r)
        else:
            r = list(s)
            r.append("ing")
            return "".join(r)
    else:
        return s


def not_bad(s):
    def not_bad(s):
    punc = ""
    start = 0
    stop = 0
    if s[-1] == "." or s[-1] == "?" or s[-1] == "!":
        punc = s[-1]
        s = list(s)
        s.pop()
        s = "".join(s)
    r = s.split(" ")
    try:
        start += r.index("not")
        stop += r.index("bad")
        if start < stop:
            r[start] = "good"
            r[start + 1:stop+1] = ""
            return " ".join(r) + punc
        else:
            return " ".join(r) + punc
    except ValueError:
        return " ".join(r) + punc


def front_back(a, b):
    a_front = ""
    a_back = ""
    b_front = ""
    b_back = ""
    
    if len(a) % 2 == 1:
        a_front = a[0:len(a)// 2 + 1]
        a_back = a[len(a)//2 + 1:]
    else:
        a_front = a[0:len(a)//2]
        a_back = a[len(a)//2:]
    if len(b) % 2 == 1:
        b_front = b[0:len(b)// 2 + 1]
        b_back = b[len(b)//2 + 1:]
    else:
        b_front = b[0:len(b)//2]
        b_back = b[len(b)//2:]
        
    return a_front + b_front + a_back + b_back
