import matplotlib.pyplot as plt

students_name = ["Sanjay","Rahul","Karan","Rohit","Virat","Ajay","ramesh","Sartaj","Priya"]
students_marks = [30,24,56,7,66,45,20,65,55]

marks_perc = []
for x in students_marks:
    res = (x/70)*100
    marks_perc.append(res)

print(marks_perc)

#line chart
def marks_line_chart():
    plt.plot(students_name,students_marks)
    plt.title("Students Marks graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()

marks_line_chart()

#bar chart

def percentage_bar_chart():
    plt.bar(students_name,marks_perc)
    plt.title("Students ' Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Student Percentage")
    plt.show()

percentage_bar_chart()
