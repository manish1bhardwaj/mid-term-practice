class employee:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id
    def details(self):
        print(f"The name of the ID:{self.id} is {self.name}")
class new_employee(employee):
    def new_details(self):
        print(f"the name of the both employee are familiar")
    

#main code
E1 = employee('Manish bhardwaj',29)
E2 = new_employee('Alok Bhadauria',7)
# =================================================call function=============================================================
E1.details()
E2.details()
E2.new_details()

