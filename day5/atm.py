#ATM

balance = 10000

while True:
    print("\n---------HDFC---------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. check balance")
    print("4. Exit")

if choice == 1:
    amount = float(input("enter your amount: "))
    if amount <- 0:
        print("firse try kar or paise nahi hai to kyu aya")
        continue
    balance += amouunt
    print("amount add ho gya bro")


elif choice == 2:
    amount = floa(input("kitne paise chahiye bro enter kar"))
    if amount > balance:
        print("pehle paise kama le bhai")
        continue
    balance -= amount
    print("haa thik hai paise lele lekin depost bhi kar dena")

elif choice == 3:
   print("abhi bhi tu gareeb hi hai", balance)


elif choice == 4:
    print("chal thik hai fir milenge")
    break
