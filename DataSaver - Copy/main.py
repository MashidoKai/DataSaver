from src.upload.dataBaseUploader import uploadData
from src.update.changePassword import changePassword
from src.update.changeUsername import changeUsername
from src.update.changeEmail import changeEmail

print("Welcome to MySQL DataSaver")
print("1 - Upload new user")
print("2 - Change Password")
print("3 - Change Username")
print("4 - Change Email")
print("")
userInput = input("Select data behavor: ")

if userInput == "2":
    userInput = input("Enter your Username: ")
    passwordChange = input("Enter new Password: ")

    changePassword(userInput, passwordChange)

elif userInput == "3":
    emailInput = input("Enter your Email: ")
    usernameChange = input("Enter new Username: ")

    changeUsername(emailInput, usernameChange)
elif userInput == "4":
    usernameInput = input("Enter your Username: ")
    emailChange = input("Enter new Email: ")

    changeEmail(usernameInput, emailChange)
else:
    usernameInput = input("Enter your Username: ")
    emailInput = input("Input your Email: ")
    passwordInput = input("Input your Password: ")

    uploadData(usernameInput, emailInput, passwordInput)