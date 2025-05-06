from collections import defaultdict

def map_students(line):
    name, mark = line.strip().split(',')
    return [(name,int(mark))]

def group(mapped_data):
    students = defaultdict(list)
    for name,mark in mapped_data:
        students[name].append(mark)
    return dict(students)    

def reduce_student_marks(grouped_data):
    result = {}
    for name, marks in grouped_data.items():
        result[name] = sum(marks)
    return result    

# Grading Function
def assign_grade(total):
    if total >= 180:
        return 'A'
    elif total >= 150:
        return 'B'
    elif total >= 120:
        return 'C'
    elif total >= 100:
        return 'D'
    else:
        return 'F'

def process_grade(filename):
    mapped=[]
    with open(filename, 'r') as file:
        for line in file:
            mapped.extend(map_students(line))
    print("mapped : ",mapped)

    grouped = group(mapped)

    print("grouped : ",grouped)

    reduced = reduce_student_marks(grouped)

    print("reduced : ",reduced)
    
    # return reduced

    grades = {}
    for name,total in reduced.items():
        grades[name]=(total,assign_grade(total))
    return grades  
  

result = process_grade("4_grades/sample.txt")  
print(result)      