# 1️⃣5️⃣ Mini Login System

# Create:

# users = {
#     "admin": "1234",
#     "user1": "abcd"
# }


# Ask for username and password.
# Print:

# "Login Successful"

# "Invalid Username"

# "Wrong Password"

user = {
  "admin" : "1234",
  "user1" : "abcd",
  "bishal" : "bishal@123"
}

userName = input("Enter your username: ")

if userName not in user:
  print("Incorrect username!!!")
else:
  password = input("Enter your password: ")

  if user[userName] == password:
    print(f"Login Successful. Welcome {userName}")
  else:
    print("Incorrect Password!!!")
  