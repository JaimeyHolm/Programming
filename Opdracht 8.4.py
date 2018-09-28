studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    studentlijst = []
    for cijfers in range(len(studentencijfers)):
        studentlijst.append(round(sum(studentencijfers[cijfers])/3,2))
    return studentlijst

def gemiddelde_van_alle_studenten(studentencijfers):
    studentlijst = []
    for i in range(len(studentencijfers)):
        studentlijst.append(sum(studentencijfers[i]))
    return round(sum(studentlijst)/12,2)

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))