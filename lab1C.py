import hashlib

class User(object):
    # 
    #Attributes:
    #  name: String that contains the name of the current user
    #  Saltvalue: String that is crucial in figuring out users Password
    #  HashedPw : Used to check users password.
    #  Password : Will hold the Password of the user once found 
    def __init__(self, name, saltV, HashedPW):
        
        self.name = name
        self.saltV = saltV
        self.HashedPW = HashedPW
        self.Password = None

# method that will be used to check if generated string match the Hashed Password .
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig



def generate_Passwords(current_num, minlength, maxlength, user_List):
    if (maxlength <minlength) or (maxlength < 0) or (minlength <0):
        print("Invalid parameters")
    elif current_num > (10**maxlength)-1:
        print("All possible passwords from length ", minlength, " to ", maxlength," generated and tested ")
        print(current_num-1," was the last number tested" )
        return user_List
    else:
        for i in range(500):
            test_Passwords(str(current_num), minlength, maxlength, user_List)
            current_num +=1 
        return generate_Passwords(current_num, minlength, maxlength,user_List)

def getUsers(filename):
    user_List = []
    with open(filename)as file:
        for line in file:
            values = line.split(",")
            user_List.append(User(values[0],values[1],values[2]))
    return user_List

# Test Passwords take a string and checks to see if it the password of any of the users.
def test_Passwords(string, minlength, maxlength,user_List ):
  if len(string)< minlength:
      string = "0" + string
      test_Passwords(str(string), minlength, maxlength, user_List)
  else:
        for i in range(100):
            if hash_with_sha256(string + user_List[i].saltV) == user_List[i].HashedPW :
                user_List[i].Password = string
                print(user_List[i].name, " password: ", user_List[i].Password )  
        if len(string) < maxlength:
            string = "0" + string
            test_Passwords(str(string), minlength, maxlength, user_List)
        return user_List


minlength = int(input("Please enter the minimum length of the passwords to be checked: "))
maxlength = int(input("Please enter the maximum length of the passwords to be checked: "))
file_name = str(input("Enter the name of the file which contains the list of Users: "))
user_List = getUsers(file_name)
user_List =  generate_Passwords(0, minlength, maxlength, user_List)
#for i in range(len(user_List)):
#   print (user_List[i].name, user_List[i].saltV ,user_List[i].HashedPW, user_List[i].Password)
