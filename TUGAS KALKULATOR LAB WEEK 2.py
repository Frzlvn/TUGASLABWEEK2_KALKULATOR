import math

def KALKULATOR():
    print("KALKULATOR")
    print("INPUT NUMBER : ")
    print("1. +")
    print("2. -")
    print("3. X")
    print("4. /")
    print("5. ^")
    print("6. √")
    print("0. EXIT")

    while True:
        Pilihan = input("Input your choice : ")

        if Pilihan == "0":
            print("Thank you !!")
            break

        elif Pilihan in ["1", "2", "3", "4", "5"]:
            a = int(input("First Number : "))
            b = int(input("Second Number: "))

            if Pilihan == "1":
                hasil = a + b
                print("Result: ", hasil)

            elif Pilihan == "2":
                hasil = a - b
                print("Result: ", hasil)

            elif Pilihan == "3":
                hasil = a * b
                print("Result: ", hasil)

            elif Pilihan == "4":
                if b != 0:
                    hasil = a / b
                    print("Result: ", hasil)
                else:
                    print("Wrong input number")

            elif Pilihan == "5":
                hasil = a**b
                print("Result: ", hasil)

        elif Pilihan == "6":
            desimal = float(input("Enter the number: "))

            if desimal >= 0:
                hasil = math.sqrt(desimal)
                print("Result: ", hasil)
            else:
                print("Wrong Input Number")

        else:
            print("Wrong input number,Please try again.")

        print()  

KALKULATOR()
