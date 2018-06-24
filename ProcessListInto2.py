
#partition the incoming list into 2 based on condition
def partition(pred, iterable):
    trues = []
    falses = []
    for item in iterable:
        if pred(item):
            trues.append(item)
        else:
            falses.append(item)
    return trues, falses

# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

#print list elements with newline
def printList(lst):
    for lElement in lst:
        print(lElement+'\n')


#read the file line by line and store in list
fname = "myurl.txt"
with open(fname) as f:
    content = f.readlines()

#remove whitespace
content = [x.strip() for x in content]

# remove none from list
content = list(filter(None, content))

#remove duplicates from list
content = Remove(content)

#split the list
community, nonCommunity = partition(lambda x: 'community' in x, content)

printList(community)
printList(nonCommunity)