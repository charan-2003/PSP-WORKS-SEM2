import turtle
name = []
marks = []

students = [
{"name":"charan","marks":[213]},
{"name":"mitra","marks":[321]},
{"name":"rahul","marks":[123]},
{"name":"nithin","marks":[202]},
{"name":"shreeya","marks":[316]},
{"name":"sai","marks":[167]},
{"name":"adithya","marks":[234]},
{"name":"kaushik","marks":[300]}
]

def drawbar(student, marks):
    student.begin_fill()
    student.left(90)               
    student.forward(marks)
    student.write(" " + str(marks))
    student.right(90)
    student.forward(40)            
    student.right(90)
    student.forward(marks)        
    student.left(90)
    student.end_fill()

def names(stu,name):
    stu.forward(10)
    stu.write(name,font=('Times New Roman',15))
    stu.forward(30)


#f=open("student_grades.txt","r")
#if f.mode=="r":
  #  contents = f.read()
    
maxmarks = max(marks)
num_stu = len(name)    
border = 10


wn = turtle.Screen()
wn.setworldcoordinates(0-border, 0-border, 40*num_stu+border, maxmarks+border)
wn.bgcolor("black")

student = turtle.Turtle()
student.color("white")
student.fillcolor("navy")
student.pensize(3)
student.speed(0)

stu = turtle.Turtle()
stu.color("white")

for i in marks:
    drawbar(student, i)
    
stu.goto(0,0)
for j in name:
    names(stu,j)

wn.exitonclick()
