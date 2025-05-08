students_scores = [150, 142, 68, 61, 105, 87, 189, 180, 107, 99, 171, 186, 122, 87]

total_exam_score = sum(students_scores)
print(total_exam_score)

sum = 0
for score in students_scores:
    sum += score

print(sum)

max_score = 0
for score in students_scores:
    if score > max_score:
        max_score = score

print(max_score)