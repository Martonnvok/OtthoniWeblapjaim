def gyak():
   n = 5
   m = int(input("Adj meg egy értéket: "))
   while n > m:
    n -= 1
    print("n= ", n)
def gyak2():
    for i in range(5):
        print(i)
    print("_____________________________________________")
    for i in range(6,9):
        print(i)
    print("_____________________________________________")
    for i in range(6, 19, 3):
        print(i)
    print("_____________________________________________")
    for i in range(76, 58, -3):
        print(i)
    print("_____________________________________________")
    for i in range(13):
        print(i, end=" ")

def feladat1():
    for i in range(100):
        print(i, end=" ")
def feladat2():
    b=0;
    while b < 150:
        b += 2
        print(b)
def feladat3():
    b=0;
    while b > 150:
        b ** 2
        print(b)