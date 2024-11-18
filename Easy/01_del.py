my_str = "Radha"
print("Radha")
val = input(print("Enter the character you want to delete:"))

my_list = list(my_str)
for i in my_list:
  if i == val:
    my_list.remove(i)
  else:
    print("Character not found")
    
my_str = str(my_list)
print(my_str)