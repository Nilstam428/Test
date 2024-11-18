def divisible(number):
  newlist = []
  for i in range(1,number+1):
    if number % i == 0:
      newlist.append(i)
  return newlist  

entered_no = int(input("Enter a number:"))
print(divisible(entered_no))