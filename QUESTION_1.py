import csv
import random

# Function to generate student age based on specified age groups
def generate_age():
    age_ranges = {'18-25': (18, 25), '25-35': (25, 35), '35-45': (35, 45), 'over 45': (46, 99)}

    # Choose a random age group
    age_group = random.choice(list(age_ranges.keys()))

    # Generate a random age within the selected age group
    age_range = age_ranges[age_group]
    random_age = random.randint(age_range[0], age_range[1])

    return random_age

# Function to generate average hours spent studying on campus
def generate_study_hours():
    study_hours_categories = [(1, 2), (2, 3), (4, 5)]
    return random.randint(*random.choice(study_hours_categories))

# Function to generate student mark and corresponding percentage
def generate_student_mark():
    mark_choices = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]  # 12 possible choices
    mark = random.choice(mark_choices)
    percentage = (mark / 130) * 100
    return mark, percentage

# Function to generate time taken on examination
def generate_exam_time():
    return random.randint(1, 180)

# Creating datasets using pandas
columns = ['StudentNumber', 'AgeGroup', 'StudyHours', 'Mark', 'Percentage', 'ExamTime']

dataset1_list = []
dataset2_list = []

for student_number in range(1, 151):
    age_group = generate_age()
    study_hours = generate_study_hours()
    mark, percentage = generate_student_mark()
    exam_time = generate_exam_time()

    # Appending data to lists
    dataset1_list.append([student_number, age_group, study_hours, mark, percentage, exam_time])
    dataset2_list.append([student_number, age_group, study_hours, mark, percentage, exam_time])

# Writing datasets to CSV files
with open('exam1_dataset.csv', 'w', newline='') as file1:
    writer = csv.writer(file1)
    writer.writerow(columns)
    writer.writerows(dataset1_list)

with open('exam2_dataset.csv', 'w', newline='') as file2:
    writer = csv.writer(file2)
    writer.writerow(columns)
    writer.writerows(dataset2_list)
