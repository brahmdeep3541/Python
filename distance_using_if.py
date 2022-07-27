dkm = int(input("please enter the distance in kilometers : "))
unit=input("please enter unit (mi=miles, m=meters): ")
mi= 0.621371

unit1 = "mi"
unit2= "m"

if unit == unit1 :
    print("The distance is ",dkm*mi, "miles")

elif unit == unit2:
    print("The distance is ",dkm*1000, "meters")
