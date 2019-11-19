# Caylin Kuenn
# CSCI 102 - Section B
# Week 12 - Part A

# First commit done here---

# Function # 1
def PrintOutput(output):
    print("OUTPUT",output)

# Second Commit done here---

# Function #2
def LoadFile(file):
    with open(file,'r') as text:
        string = list(text.read())
        Total = ""
        Array = []

        for word in string:  # Place each word in one cell of array

            if word == '\n':
                word = ""
                Array.append(Total)
                Total = ""

            Total += word

        return Array

# Commit #3 done here ----

#Function #3
def UpdateString(string,char,num):
    string = list(string)
    string[num] = char
    string = "".join(string)
    print("OUTPUT",string)

# Commit #4 done here ----

# Function #4
def FindWordCount(string,word):
    string = str(string)
    count = string.count(word)
    return count

# Commit #5 done here ----

# Function #5

def ScoreFinder(players, scores, person):
    person = list(person)
    letter = person[0].upper()
    person[0] = letter
    person = "".join(person)
    if person in players:
        position = players.index(person)
        print("OUTPUT %s got a score of %f" %(person,scores[position]))
    else:
        print("OUTPUT player not found")


