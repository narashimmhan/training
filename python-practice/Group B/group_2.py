class Department:
    def __init__(self):
        try:
            f=open("group_b_demo.txt","r")
            s=f.read().splitlines()
            self.subj=s[0].split(",")
            self.topics=s[1].split(':')
            self.teachers=s[2].split(':')
            #print(self.topics)
            #print(self.teachers)
            self.sub_details={}
            self.dep_details={}
            f.close()
        except Exception as e:
            print (e)
    def get_subject(self):
        print("SUBJECTS :", self.subj)
        self.sub_details=dict(zip(self.subj,self.topics))
        self.dep_details=dict(zip(self.subj,self.teachers))
    def get_subj_details(self,sub):
        self.sub=sub
        #print ('Subject-topics:', self.sub_details)
        print ('Subject topics available:')
        print (sub,':',self.sub_details.get(sub))
        self.topic = input('Enter the topic you are choosing:')
        print ('Teachers who are available for the subject:')
        print (self.dep_details.get(sub))
        self.teacher = input('Enter the teacher you are choosing:')

class Student(Department):
    def s_details(self):
        self.id=int(input('Enter your id:'))
        self.name=input('Enter your name:')
        self.email=input('Enter your frequently used email:')
        self.phn=input('Enter your mobile number:')
    def choose(self):
        self.get_subject()
        sub=input("Select the subject of your choice :")
        self.get_subj_details(sub)


    def write_stud_details(self):
        f=open("student_details.txt",'a')
        f.write(str(self.id)+','+str(self.name)+','+str(self.email)+','+str(self.sub)+','+str(self.topic)+','+str(self.teacher))
        f.write('\n')
        f.close()

while True:
    ch=int(input("Do you want to enter details.If yes give 1 else 0"))
    if ch==1:
        s1=Student()
        s1.s_details()
        s1.choose()
        s1.write_stud_details()
        print("Thank you! Your details have been updated")
    else:
        break
