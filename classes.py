class Student:
    stdcnt=0
    def __init__(self,name,prn,dob):
        self.Name=name
        self.PRN=prn
        self.DOB = dob
        Student.stdcnt=Student.stdcnt + 1
        print("Constructor running")
    def getDetails(self):
        print('Name: ',self.Name)
        print('Prn: ',self.PRN)
        print('Dob: ',self.DOB)
    def geti(self):
        print("Student k andar hai")

S1=Student('bala',23,3453223)
print(S1.Name)
print(S1.PRN)
S1.getDetails()
print(Student.stdcnt)
#s2=Student()
#print(s2)
