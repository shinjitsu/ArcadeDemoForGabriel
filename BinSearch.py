

def binary_search(list_to_search, target):
    if list_to_search == []:
        return {}
    middle = len(list_to_search)//2
    middle_item = list_to_search[middle]
    if middle_item.get("name") == target:
        return middle_item
    if middle_item.get("name") <= target:
        return binary_search(list_to_search[middle+1:], target)
    else:
        return binary_search(list_to_search[:middle], target)


def main():
    all_students = get_students()
    all_students.sort(key=get_key)
    student_to_find = input("which student do you want to find?")
    student_record = binary_search(all_students, student_to_find)
    print(student_record)

def get_key(student):
    return student["name"]




def get_students()->list:
    all_students = []
    with open('students.txt', 'r') as students_file:
        all_lines = students_file.readlines()
        for line in all_lines:
            data = line.split(',')
            student = {}
            student['name'] = data[0]
            student['studentNumber'] = int(data[1])
            student['gpa'] = float(data[2])
            student['credits'] = int(data[3])
            all_students.append(student)
    return all_students

if __name__ == '__main__':
    main()