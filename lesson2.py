# gradus = int(input( "gradus"))
# typt_temp=input("F or C").lower()
# if typt_temp == "F":
#     temp=(gradus - 32) * (5/9)
#     print(f"{gradus}  foreigeht {temp } celsii")
# elif typt_temp == "C" :
#     temp = gradus  * (9/5) + 32
#     print(f" gradus {gradus} celsii ravno {temp } fo

# for i in lists:
#     print(i)
# for i in "dearmy":
#     print(i)
# k = [3, 8, 7, 2334, 667, 88]
# for i in k:
#     if i % 2==0 and i % 3==0:
#         num.append(i)
# print(num)

# Ii = list(range(1,1000))
# print(Ii)
# for i in  Ii:
#  if i % 2==0:
#      print(i)
# print("*****\n*****\n*****\n*****\n*****")
# for  o in range(1,10):
#     for i in range(1, o + 1):
#         print('{} * {} = {}'.format(i, o, i * o), end="")
#
#
# print()

# num = int(input("write a num : "))
# for i in range(5):
#     print(f"*" * 5 )



# def get_result(genre: str, time: int, cost: int):
#     result = (
#         genre in ['comedy', 'horror', 'detective']
#         and(
#             (time<=21 and cost<500) or
#             (time<21 and cost<300)
#             )
#         )
#     return result

# for i in range(20):
#     print(i)
# num = int(input("write "))
# counter = 0
#for i in range(1,num +1):
#     counter+=i
# else:
#     print("result" , counter)

# for i in range(1,100):
#     if i % 3 != 0 :
#       continue
#     print(i)
# else:
#     ("end")
# lists=[]
# for i in range(1,100):
#     if i % 3 != 0 :
#         continue
#     lists.append(i)
# #     print(lists)
# i = 0
# while i<=100:
#     i+=1
#     if i ==50:
#        break
#     i +=1
#     print(i)

user_parol = ["ailin","adil"]
a =3
while True:

    if a<=0 :
        user_parol.clear()
        print("max try ")
        break
    get_user_name = input("Write a you'r user name ")
    ger_user_parol = input("Write a you'r user parol ")

    if get_user_name == user_parol[0] and ger_user_parol == user_parol[1]:
        print("YOU WIN CONG")
        break
    elif a>0:
        print("TRY AGAIN")
        a-=1








