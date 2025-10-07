f = open("../demo.txt")
print(f.read())

frt = open("../demo.txt", "rt")
print(frt.read())
frb = open("../demo.txt", "rb")
print(frb.read())
frb.close()
frt.close()
f.close()


with open("../demo.txt") as f:
    print(f.read(3))

with open("../demo.txt") as f:
    for x in f:
        print(x)

with open("../demo.txt", "a") as f:
    f.write("\nNow the file has more contents")

with open("../demo.txt") as f:
    print(f.read())

with open("../demo.txt", "w") as f:
    f.write("Ohh i lost my file contents")
with open("../demo.txt") as f:
    print(f.read())

try:
    f = open("../demo.txt", "x")
except FileExistsError as e:
    print(e)
finally:
    f.close()

# f = open('../document.txt','x')

with open("../document.txt", "a") as f:
    f.write("\nNow the file has more contents")
    f.write("\nNo needs to be active")

with open("../document.txt") as f:
    print(f.read())

from os import path, remove

f = open("../document2.txt", "x")
f.close()
if path.exists("../document2.txt"):
    remove("../document2.txt")
    print("Document removed")
else:
    print("The file does not exist")
