print ("Change Calculator")
print ("--------------------")
fiftynote =50
twentynote =20
tennote =10
fivenote =5
twopound =2
onepound =1

price =int(input("Enter price of item(s)£:"))
cash =int(input("Enter amount paid£:"))
change =(cash-price)

fiftychange = int(change/fiftynote)
fiftypnewbalance=change-fiftychange*fiftynote

twentychange=int(fiftypnewbalance/twentynote)
twentypnewbalance=fiftypnewbalance-twentychange*twentynote

tenchange=int(twentypnewbalance/tennote)
tenpnewbalance=twentypnewbalance-tenchange*tennote

fivechange=int(tenpnewbalance/fivenote)
fivepnewbalance=tenpnewbalance-fivechange*fivenote

twochange=int(fivepnewbalance/twopound)
twopnewbalance=fivepnewbalance-twochange*twopound

onechange=int(twopnewbalance/onepound)
onepnewbalance=twopnewbalance-onechange*onepound

if fiftychange>0:
    print("£50 x",fiftychange)
if twentychange>0:
    print("£20 x", twentychange)
if tenchange>0:
    print("£10 x",tenchange)
if fivechange>0:
    print("£5 x", fivechange)
if twochange>0:
    print("£2 x", twochange)
if onechange>0:
    print("£1 x", onechange)


    



