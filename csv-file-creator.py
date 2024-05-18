import csv
from faker import Faker
import random

fake = Faker()

def generate_student_details(num_records):
    student_details = []
    for student_id in range(1, num_records + 1):
        student_details.append({
            'student_id': student_id,
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=25).strftime("%Y-%m-%d"),
            'gender': random.choice(['M', 'F'])
        })
    return student_details

def generate_student_contacts(num_records):
    student_contacts = []
    for student_id in range(1, num_records + 1):
        student_contacts.append({
            'student_id': student_id,
            'email': fake.email(),
            'phone_number': fake.phone_number()
        })
    return student_contacts

def generate_student_marks(num_records, subjects):
    student_marks = []
    for student_id in range(1, num_records + 1):
        cgpa = round(random.uniform(2.0, 4.0), 2) 
        for subject in subjects:
            marks = random.randint(50, 100)
            student_marks.append({
                'student_id': student_id,
                'subject': subject,
                'marks': marks,
                'cgpa': cgpa
            })
    return student_marks

def write_csv(filename, fieldnames, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    num_records = 7000
    subjects = ['Math', 'English', 'Science', 'History']

    student_details = generate_student_details(num_records)
    student_contacts = generate_student_contacts(num_records)
    student_marks = generate_student_marks(num_records, subjects)

    write_csv('student_details.csv', ['student_id', 'first_name', 'last_name', 'date_of_birth', 'gender'], student_details)
    write_csv('student_contacts.csv', ['student_id', 'email', 'phone_number'], student_contacts)
    write_csv('student_marks.csv', ['student_id', 'subject', 'marks', 'cgpa'], student_marks)

    print("CSV files have been created successfully.")

if __name__ == "__main__":
    main()
