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

        print(Array)

# Commit #3 done here ----