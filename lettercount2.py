msg=input("Enter any message ")
query=input("Letter you are looking for? ")
instances=0
i=0

while i<len(msg):
    if msg[i] == query:
        instances += 1
    i += 1
print("There are", instances, query)