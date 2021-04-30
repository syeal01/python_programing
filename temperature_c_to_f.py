# Aliabbas Syed
# Convert from temperature in C to F
# F = C 9/5 + 32

import os
import datetime

def C_to_F(temp_in_C):
    temp_in_F = float(temp_in_C * 9 / 5 + 32)
    return(temp_in_F)

temp_in_C = float(input("Enter Temperature in ºC: "))
if( temp_in_C <= -273.15):
    print("Sorry lowest possible temperature that physical matter can reach is -273.15C")
else:
    print("{}ºC is {}ºF".format(temp_in_C, C_to_F(temp_in_C)))


# TEST USE CASES
# temperatures = [10,-20,-289,100]
# for t in temperatures:
#     print( C_to_F(t) )

# FILE = r".\Output.txt"
# with open(FILE, "w") as file:
#     for t in temperatures:
#         file.write("{} = {}\n".format(datetime.datetime.now(), str(C_to_F(t))))
# print("Check {}".format(FILE))
# os.system("notepad {}".format(FILE))