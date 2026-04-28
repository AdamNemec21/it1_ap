mylist = ["pomeranc", "jablko", "citron", "cisco", "vlk"]
print(mylist)
print(len(mylist))
print(mylist[-1])

duplist = mylist[2:5] # vcetne prvniho cisla a bez druheho 
print(duplist)

if "jablko" in mylist:
    print("jablko tam je")

    mylist[2] = "bazen"
    print(mylist)
    mylist.append("mango")
    print(mylist)
    mylist.insert(1, "banan")
    print(mylist)

    zelenalist = ["paprika","mrkev","okurka"]
    mylist.extend(zelenalist) #prida 
 
    print(mylist)

    mylist.remove("cisco") #odstrani zadanou polozku z listu
    print(mylist)

    mylist.pop(2) #odstrani polozku podle indexu, pokud se index vynecha odstrani posledni
print(mylist)

print(zelenalist)
zelenalist.clear() #vyprazdni list
print(zelenalist)

del zelenalist #defininitvne odstrani list

for i in mylist:
    print(i)

for i in range(len(mylist)):
    print(mylist[i])

abeceda = ["a","f","c","d"]
abeceda.sort(reverse=True) # sort seradli podle abecedy reverse obracene
print(abeceda)

mylist.sort(key=str.lower) #seradi podle malych pismenek
print (mylist)

nums = [100,50,65,82,23]
nums.sort()
print(nums)
nums.reverse()
print(nums)

print(mylist)
mylist[0] = "pomeranc"
print(mylist)

copylist = mylist.copy()
copylist[0] = "orech"
print(mylist)
print(copylist)