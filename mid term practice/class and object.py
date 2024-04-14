class Student:
    print("This Data is Entered in Database!!!")
    def __init__(self,name,age,course,college,marks):
        self.name = name
        self.age = age
        self.course = course
        self.college = college
        self.marks = marks
    @staticmethod              #it is nothing but decorater and it is used to convert our method in normal form or we can say when we don't want o use self parameter .
    def hello():
        print("Hello")  
    def info(self):
        print(f"Name : {self.name},Age : {self.age},Course : {self.course},College : {self.college}")
    def get_ave(self):
        sum = 0
        for i in self.marks:
            sum+=i
        print(f'Hello {self.name} Yours Ave Marks is : {sum/4}')

s1 = Student('Manish Bhardwaj',18,'B-Tech-CS-AIML AND IOT','GLA University',[20,30,40,50])
s2 = Student('Mohammad Ayaan Hussain',18,'B-Tech-CS-AIML AND IOT','GLA University',[30,40,50,66])
s3 = Student('Alok Bhadauria',18,'B-Tech-CS-AIML AND IOT','GLA University',[20,40,60,10])
s4 = Student('Priyanshu Sharma',18,'B-Tech-CS-AIML AND IOT','GLA University',[30,20,10,50])
print("------------------------------------")
s1.info()
s2.info()
s3.info()
s4.info()
print("------------------------------------")
s1.get_ave()
s2.get_ave()
s3.get_ave()
s4.get_ave()
print("------------------------------------")
s1.hello()
s2.hello()
s3.hello()
s4.hello()
print("------------------------------------")