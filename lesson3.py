got = int(input( " please write a year "))
if got % 4 == 0 and got % 100==0  and got % 400==0 :
    print(" its Right")
else:
    print("its not True")