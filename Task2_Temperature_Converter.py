temp=float(input("Enter the temperature: "))
option=input("Enter option(C for Celsius,F for Fahrenheit):")
if option=="C" or option=="c":
  fahrenheit=(temp*9/5)+32
  print("Temperature in fahrenheit:",fahrenheit)
elif option=="F" or option=="f":
  celsius=(temp-32)*5/9
  print("Temperature in celsius:",celsius)
else:
  print("Invalid option")