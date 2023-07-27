import logging


def fibo(n):
    a = 0
    b = 1
    while a < n:
        logging.info(a)
        a, b = b, b+a


# fibo(7)

# num1 = int(input("Enter a number: "))
# # num2 = int(input("Enter a number: "))
total = 0
for num in range(1, 9):
    if (num % 2 == 1):
        logging.info(num)
    total = total+num
logging.info(total)
# maximum = int(input(" Please Enter the Maximum Value : "))
# total = 0


# # # for number in range(1, maximum+1):
# # #     if(number % 2 == 0):
# # #         logging.info("{0}".format(number))
# # #         total = total + number

# # # logging.info("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))

# a = "vavava"
# logging.info(a[:3]+a[2:].replace("a", "$"))
# st = "hi how are you"
# logging.info(st.count("h"))
# s = st.split(" ")
# logging.info(s)
# t = s[::-1]
# logging.info(t)
# # k = " ".join(t)
# # logging.info(k)
# # logging.info(len(a))
# # logging.info(a)
