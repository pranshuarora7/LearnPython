dic = {1: "asda", 2: "sdfssda", 3: "zsdassda"}
print(dic[3])
print(dic)

for i in dic.keys():
    print(f"the value is {i} : {dic[i]}")

dic2 = {4: " sdas", 5: " dadadf"}
dic.update(dic2)
print(dic)
