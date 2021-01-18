import random

lst=["r","p","s"]
lst1=["p","s","r"]
dic={"p":"paper","r":"rock","s":"scisers"}

while True:
    r= random.choice(lst)
    ip=input("r,p or s ---->")

    if r==ip:
        print(dic[r]+" <  VS  >  "+dic[ip])
        print(" ---------its tie----------- ")
    elif lst.index(r)==lst1.index(ip):
        print(dic[r]+" <  VS  >  "+dic[ip])
        print("u win")
        break
    else:
        print(dic[r]+" <  VS  >  "+dic[ip])
        print("u lose")
        break

        


