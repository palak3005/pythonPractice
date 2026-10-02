#list->[square brackets]
list1 = [10,20,30,40]
#tuple->(round brackets)
tup =(10,20,30,40)
print(tup[3])
#tup[2] = 40 can not change once defined
print(tup.count(10))

#set-> curly brackets
sets = {10,20,10,35,30, 100,40}
#sets[2] indexing is not allowed unorderd sequence h
print(sets)
#get value not in same sequence u added
#{40, 10, 20, 30}{35, 20, 40, 10, 30}
#no repetation in elements

#operations

sets.add(120)
sets.discard(20)
print(sets.issuperset({10,120,40}))
print(sets)
