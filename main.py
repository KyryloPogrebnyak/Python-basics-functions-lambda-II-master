### Task 1

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key=lambda x: x[1])
print(subject_marks)

### Task 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter = filter(lambda x: x if x % 2 == 0 else False, numbers)

print('###########################################################################')
print(list(filter))



