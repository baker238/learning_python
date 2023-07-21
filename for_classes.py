classes = [
    {'name': '3А', 'scores': [3,4,4,5,2]},
    {'name': '3Б', 'scores': [5,5,3,2,2]},
    {'name': '3В', 'scores': [4,5,3,5,4]},
]
			
def class_avg_score(student_scores):
    class_avg =0
    for one_class in student_scores:
        class_avg += one_class
    return class_avg / len(student_scores)

school_avg = 0

for cl in classes:
    class_score_avg = class_avg_score(cl["scores"])
    print(f'Средняя оценка {cl["name"]} класса: {class_score_avg}')
    school_avg += class_score_avg 

school_avg = round(school_avg / len(classes),1)

print(f'Средняя оценка по школе {school_avg}')