students = []


def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f): # lub (2) "for student in f" lub (3) "for student in f.readlines()"
            students.append(student)
        f.close()
    except Exception:
        print("Could not read a file.")


def read_students(f):
    for line in f:
        yield line