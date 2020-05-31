import os

def getFeatList(fileName):

    fid = open(fileName, 'r')
    Lines = fid.readlines()

    featList = []
    for line in Lines:
        split = line.strip().split()
        if len(split) > 1:
            featList.append(split[0].lower())

    return featList

def AlexComputer():
    if os.getcwd() == r'C:\Users\Alex\PycharmProjects\DeepEarnings':
        return True
    else:
        return False