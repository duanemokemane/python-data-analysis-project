import pandas as pd

# Load datasets
dataset1 = pd.read_csv('exam1_dataset.csv')
dataset2 = pd.read_csv('exam2_dataset.csv')

# Combine datasets
#pandas will ignore the index in the orignal datasets, and create a new one
ds = pd.concat([dataset1, dataset2], ignore_index=True)

#empty dictionaries for frequency tables
hours_frequency = {}
age_frequency = {}
mark_frequency = {}

# Generate frequency tables
for _, row in ds.iterrows():
    # Average hours spent on campus
    hours_key = f"{row['StudyHours']} - {row['StudyHours'] + 1}"
    hours_frequency[hours_key] = hours_frequency.get(hours_key, 0) + 1

    # Student age
    age_key = row['AgeGroup']
    age_frequency[age_key] = age_frequency.get(age_key, 0) + 1

    # Student mark
    mark_key = row['Mark']
    mark_frequency[mark_key] = mark_frequency.get(mark_key, 0) + 1

#import matplotlib for plotting
import matplotlib.pyplot as plt

# converted the dictionary to a DataFrame because it is more efficient for matplotlib
age_df = pd.DataFrame(list(age_frequency.items()), columns=['AgeGroup', 'Frequency'])

# Create a bar chart
plt.bar(age_df['AgeGroup'], age_df['Frequency'], color='green')
plt.xlabel('Age Groups')
plt.ylabel('Number of Students')
plt.title('Number of Students in Each Age')
plt.xticks(rotation=45, ha='right')  #i rotated the x axis values so that they don't overlap each other
plt.tight_layout()
# Show the plot
plt.show()

# Aggregate data by taking the average mark for each 'ExamTime'
average_marks = ds.groupby('ExamTime')['Mark'].mean().reset_index()
# Line graph
plt.plot(average_marks['ExamTime'], average_marks['Mark'], linestyle='-', marker='', color='blue')

plt.xlabel('Time Spent on Campus')
plt.ylabel('Average Student Mark')
plt.title('Correlation Between Time Spent on Campus and Average Student Mark')
plt.show()

#scatterplot for time spent in exam vs the student marks
#added alpha so that i can fine-tune some of the plots
plt.scatter(ds['ExamTime'], ds['Mark'], alpha=0.5)

plt.xlabel('Time Spent on Examination (minutes)')
plt.ylabel('Student Mark')
plt.title('Time Spent vs. Student Mark')
plt.show()

# Scatter plot for time spent on campus vs the Student Age
plt.scatter(ds['StudyHours'], ds['AgeGroup'], alpha=0.5)

plt.xlabel('Average Hours Spent on Campus')
plt.ylabel('Student Age')
plt.title('Time Spent on Campus vs. Student Age')
plt.show()


