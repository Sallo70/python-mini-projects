# class Student:
#     def __init__(self,name,marks):
#         self.name= name
#         self.marks= marks
        
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi",self.name, "your averg score is:",sum/3) 
    
        
# s1 = Student("sallo",[90,45,55])
# # print(s1.name,s1.marks)
# s1.get_avg()



class Acount:
    def __init__(self, bal, acc):
        self.balance= bal
        self.account = acc
# debit method
    def debit(self, amonth):
        self.balance -= amonth
        print("Rs",amonth, "was debit")
        if self.get_baln() > 0:
             print("total balnce:", self.get_baln()) 
        else:
            print("No balance:",self.get_baln())   
        
# credit method
    def credit(self, amonth):
        self.balance =+ amonth
        print("Rs",amonth,"was credit")
        print('Total balance:',self.get_baln()) 
        
    def get_baln(self):
        return self.balance
acc1 = Acount(10000, 540)
acc1.credit(1000)
acc1.debit(1000)