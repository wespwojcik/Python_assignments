


class User:
    name = "mark"
    email = "mark@mark.com"
    password = "hellohellohello"

    def getinfo(self):
        msg = "\nName: {}\nEmail: {} \nPassword:".format(self.name, self.email , self.password)
        return msg


    
class Employee(User):
    base_pay = 11.00
    department = 'general'
    pin_number = '3980'



    def getinfo(self):
        msg = "\n{} is making {} an hour\n his department is {}\nand his employee pin is {}\nYou may contact him by emailing him at {}".format(self.name,self.base_pay,self.department,self.pin_number,self.email)

        return msg
class Vacation(User):
    place = "new zealand"
    favoritemeal = "Breakfast"

    def getinfo(self):
        msg = "\n{} love to go to {},and he enjoys {} in {} while he is there!".format(self.name,self.place,self.favoritemeal ,self.place)
        return msg
    




if __name__ == "__main__":
    user = User()
    print("Marks Information")
    print(user.getinfo())
    
    print("His Employee Info")
    emp = Employee()
    print(emp.getinfo())

    print("His favorite Vaction spot!")
    vac = Vacation()
    print(vac.getinfo())



 
        


    
           

