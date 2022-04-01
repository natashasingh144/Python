#initializing the list
test_list = [1,2,3,4,5,6]
print("Checking if 4 exists in list ( using loop ) : ")
for i in test_list:
    if(i==4):
      print("Element exists")
print("Checking if 4 exists in list (using in) : ")
if(4 in test_list):
    print("Element exists")
else:
    print("Element does not exist")


