'''
4.1
'''
import csv

# a. Read the csv file as a list of lists.
with open(r'C:\Users\EDUV4835142\Downloads\percent-bachelors-degrees-women-usa.csv', 'r') as file:
    reader = csv.reader(file)
#b. Assign to BDW
    BDW = list(reader)

# c. first five rows of BDW on different lines.
print("First row:")
print(BDW[0])
print("\nSecond row:")
print(BDW[1])
print("\nThird row:")
print(BDW[2])
print("\nFourth row:")
print(BDW[3])
print("\nFifth row:")
print(BDW[4])

# d. Header removed and rest added to BDW1
BDW1 = BDW[1:]

# e. Using slicing, display the first, second and third row of BDW1
print("\nFirst row of BDW1:")
print(BDW1[0])
print("\n2nd row of BDW1:")
print(BDW1[1])
print("\n3rd row of BDW1:")
print(BDW1[2])

'''
4.2
'''

# a. Creating a dictionary "Indexcount_year" with years as keys and frequencies as values
Indexcount_year = {}
for row in BDW1:
    year = int(row[1])  # Assuming the year is in the second column
    if year in Indexcount_year:
        Indexcount_year[year] += 1
    else:
        Indexcount_year[year] = 1

# b. Creating a dictionary "Indexpercent_year" with years as keys and indices as values
Indexpercent_year = {}
for index, row in enumerate(BDW1):
    year = int(row[1])  # Assuming the year is in the second column
    Indexpercent_year[year] = index
'''
4.3
'''
#Create empty lists for my variables
Maths_Stats = []
Physic_Sci = []
Engine = []
Comp_Sci = []
Year = []

# Loop through BDW1
for row in BDW1:
    year = int(row[1])      
    # Append the percentages to the empty lists i created
    #Counted where each column was in BDW
    Maths_Stats.append(float(row[14]))  
    Physic_Sci.append(float(row[15]))   
    Engine.append(float(row[10]))
    Comp_Sci.append(float(row[7]))      
    # Append the year to the Year list
    Year.append(year)
    
'''
4.4
'''
#importing numpy for the question
import numpy as np

# converted all the lists to a float separately
Maths_Statsfloat = [float(percentage) for percentage in Maths_Stats]
Physic_Scifloat = [float(percentage) for percentage in Physic_Sci]
Enginefloat = [float(percentage) for percentage in Engine]
Comp_Scifloat = [float(percentage) for percentage in Comp_Sci]

# combine all the separate lists into a single NumPy array
Selected4Majors = np.array(Maths_Statsfloat + Physic_Scifloat + Enginefloat + Comp_Scifloat)

#Creating a dictionary called majors
#range(len()) first returns the length of the list and then creates a sequence starting from zero.
Majors = {
    'Math and Statistics': range(len(Maths_Stats)),
    'Physical Sciences': range(len(Maths_Stats), len(Maths_Stats) + len(Physic_Sci)),
    'Engineering': range(len(Maths_Stats) + len(Physic_Sci), len(Maths_Stats) + len(Physic_Sci) + len(Engine)),
    'Computer Science': range(len(Maths_Stats) + len(Physic_Sci) + len(Engine), len(Selected4Majors))
}

'''
4.5
'''
import matplotlib.pyplot as plt

#python function that accepts two arguments
def plot_selected_majors(data, majorlist):
    """
    Plot the data in the variable Year against Selected4Majors for the specified majors.
    """
    # figure and axis
    fig, ax = plt.subplots()

    # Plot each major using a for loop
    for major, indices in majorlist.items():
        selected_data = [Selected4Majors[index] for index in indices]
        ax.plot(data, selected_data, label=major)

    # Display the legend in the upper left corner
    ax.legend(loc='upper left')

    # Set the title and labels
    ax.set_title("Percentage of Selected4Degrees Awarded per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Selected4Degrees")

    # Show the plot
    plt.show()

# Call the function to plot the data
plot_selected_majors(Year, Majors)

'''
4.6 in the word document
'''





