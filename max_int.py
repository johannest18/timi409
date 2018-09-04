#taka við heiltölum í input
num_int = int(input("Input a number: "))    # Do not change this line
#Láta forritið muna eftir tölunni
max_int = num_int
#Ef að ekki er skráð inn jákvæð heiltala (0 meðtalinn) þá er hún hæsta talan og skal því prenta hana út.
#Aftur skal biðja um heiltölu í input.
# Ef hún er hærri en hæsta talan sem forritið man eftir skal forritið gleyma þeirri tölu og muna þessa í staðinn.
#Ef talan er neikvæð heiltala skal forritið prenta út hæstu tölu sem slegin hefur verið inn.
# EF talan er jákvæð skal endurtaka

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int=num_int
    

print("The maximum is", max_int)    # Do not change this line