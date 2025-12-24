print("Hey pizza! Good Pizza ")
size = (input("what is the size that you want? S,M or L ? ")).upper()
pepperoni = (input("Do you want pepperoni on your za? Y or N: ")).upper()
extra_cheese = (input("Do you want extra cheese on your za? Y or N: ")).upper()
bill = 0
# for s = 15, m=20, l=25
# for p_s = 2, p_m_OR_l = 3, extra_cheese=1
if size=="S": 
    bill = 15
    
elif size=="M":
    bill = 20

elif size=="L":
    bill = 25

else:
    print("Invalid input!")
    
if pepperoni=="Y":
    if size=="S":
        bill+=2
    
    else:
        bill+=3
        
if extra_cheese=="Y":
    bill+=1

print(f"Your total bill is ${bill}")
print("Please come again!")
