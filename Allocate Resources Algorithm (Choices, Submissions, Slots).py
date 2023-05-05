# Import the required libraries
from collections import defaultdict
import pandas as pd
import random

# Load the Excel file containing choices using Pandas
choices_df = pd.read_excel('path/to/your/choices/file.xlsx')

# Extract the list of choices from the loaded Excel data
choices = choices_df["Choice"].tolist()

# Load the Excel file containing submissions using Pandas
submissions_df = pd.read_excel('path/to/your/submissions/file.xlsx')

# Convert the loaded submissions data into a list of dictionaries
submissions = submissions_df.to_dict(orient='records')

# Set the number of slots available for each choice
slots = 2

# Define the function for allocating resources
def allocate_resources(choices, submissions, slots):
    # Initialize a dictionary to store allocations
    allocations = defaultdict(list)

    # Create a dictionary to store the persons who rank each choice similarly
    similarly_ranked = defaultdict(list)

    # Iterate through the submissions in random order
    random.shuffle(submissions)
    for submission in submissions:
        # Extract ranked choices from submission
        ranked_choices = submission["Rank"].split(",")  # Assumes the "Rank" column contains comma-separated ranked choices
        for choice in ranked_choices:
            if len(allocations[choice]) < slots:
                allocations[choice].append(submission["Person"])
                break  # Break out of the loop after allocating to the first available choice
            else:
                similarly_ranked[choice].append(submission["Person"])

    # Allocate persons who rank a choice similarly randomly
    for choice, persons in similarly_ranked.items():
        while len(allocations[choice]) < slots and len(persons) > 0:
            person = random.choice(persons)
            allocations[choice].append(person)
            persons.remove(person)

    return allocations

# Call the allocate_resources function
allocations = allocate_resources(choices, submissions, slots)

# Convert the allocations dictionary to a Pandas DataFrame
allocations_df = pd.DataFrame(list(allocations.items()), columns=['Choice', 'Allocations'])

# Save the allocations to an Excel file
allocations_df.to_excel('path/to/your/output/file.xlsx', index=False)
