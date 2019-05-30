find = input("What are you looking for?: ")
replace = input ("Replace with what?: ")


file_read=open("data.txt","r")
file_write=open("data3.txt", "w")


for data in file_read:
    i=0
    while i<len(data):
        if data[i] == find[0]:
            if data[i:len(find)+1] == find:
                print(replace, end ="",file=file_write)
                i+= len(find)-1
            else:
                print(data[i],end ="",file=file_write)
        else:
            print(data[i],end = "",file=file_write)
        i+=1