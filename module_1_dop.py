gradies = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list_sorted = sorted(list(students))

dict_students_and_gradies = {}
index = 0
for gradie  in gradies:
    average_value = sum(gradie) / len(gradie)
    student_and_gradies = {students_list_sorted[index]: average_value}
    dict_students_and_gradies.update(student_and_gradies)
    index += 1

print(dict_students_and_gradies)
