class patient:
    def __init__(self,patient_id,name,age,gender,disease_name,blood_group,contact) -> None:
        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__disease_name = disease_name
        self.__contact = contact
        self.__blood_group = blood_group
        self.__assigned_doctor = None

    def assign_doctor(self,doctor):
        self.__assigned_doctor = doctor 
    
    def get_patient_details(self):
        self.__Patient_details =  {
'Patient ID' : self.__patient_id,
'Name'  : self.__name,
'Age' : self.__age,
'Gender' : self.__gender,
'Disease': self.__disease_name,
'Blood Group' :self.__blood_group,
'Contact' :self.__contact}
        print("             Patient Details            ")
        for name ,details in self.__Patient_details.items():
                print(str(name).rjust(18),' : ' ,str(details).ljust(18))
        print()
       

class doctor:
    def __init__(self,doctor_id,name,specialization,experience):
        self.__name = name
        self.__doctor_id = doctor_id
        self.__specialization = specialization
        self.__experience = experience
        print( "            Doctor Details              ")
    def get_doctor_details(self):
        self.__doctor_details = {'Doctor_Id' : self.__doctor_id,'Name' : self.__name, 
                                 'Specialization' : self.__specialization,
                                 'Experience' :  self.__experience }
        for name ,details in self.__doctor_details.items():
            print(str(name).rjust(18),' : ' ,str(details).ljust(18))
        print()
       

    #maincode

p1 = patient(245565657,'Ayaan',18,'Male','Stomach infection','O+',91+8268753287)
(p1.get_patient_details())

d1 = doctor(254658789,'Manish Bhardwaj','Gastroenterologists','10 Years')
(d1.get_doctor_details())  