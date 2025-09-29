fo=open("plik.txt")
print(fo.read())
fo.close()#trzeba zamknac
fo=open("plik.txt","a")
fo.write("\n nowa tresc")
fo.close()
fo=open("plik.txt")
print(fo.read())
fo.close()