students=dict()
gradesOfStudents=[]
myDict={}
instructors={'nesli':'nesli123','berat':'berat123','gökhan':'gökhan123','enver':'enver123','yalın':'yalın123'}
username=input('enter an username: ')
password=input('enter a password: ')

if username in instructors.keys() and password==instructors[username]:
  instructors_list=list(instructors.keys())
  chosenLectures=instructors_list.index(username)+1
  lectures={1:"CENG-113",2:"CENG-111",3:"MATH-141",4:"PHYS-121",5:"ENG-101",6:"CENG-115"}
  chosenStudents=0

  numberOfStudents=int(input("How many students do you want to add to the students dict ?\n "))

  for i in range(1,numberOfStudents+1):
      nameOfStudents=input("Enter the students name : ")
      students[i]=nameOfStudents

  decision='yes'
  while decision=='yes':

      print("Students :\n ",students)
      chosenStudents=input("Choose student number")
      print(chosenStudents)
      mid1=int(input("To "+students[int(chosenStudents)].upper()+" Enter the scores of midterm 1 of "+lectures[int(chosenLectures)]+": "))

      mid2=int(input("To "+students[int(chosenStudents)].upper()+" Enter the scores of midterm 2 of "+lectures[int(chosenLectures)]+": "))

      final=int(input("To "+students[int(chosenStudents)].upper()+" Enter the scores of final of "+lectures[int(chosenLectures)]+": "))
      
      avg=mid1*(1-0.7)+mid2*(1-0.7)+final*(1-0.6) 
      gradesOfStudents=[students[int(chosenStudents)],lectures[int(chosenLectures)],str(mid1),str(mid2),str(final),str(avg)]
      myDict[chosenStudents]=gradesOfStudents
      print(myDict)
      decision=input("Do you want to add score of other students or change something Yes/No ")