import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
df = pd.read_csv("suicide_reates.csv")

# Menu for user's choice
print("Select a graph to display:")
print("1. Bar Graph")
print("2. Histogram")
print("3. Scatter Plot")
print("4. Line Graph")  # Add Line Graph option

choice = input("Enter your choice (1/2/3/4): ")

# Convert the choice to an integer
choice = int(choice)

# Check the user's choice and create the corresponding plot
if choice == 1:
    # Bar Graph
    plt.figure(figsize=(10, 6))
    plt.bar(df["YEAR"], df["ESTIMATE"])
    plt.title("Bar Graph: Suicide Death Rates Over Time")
    plt.xlabel("Year")
    plt.ylabel("Death Rate (per 100,000 population)")
    plt.grid(axis="y")
    plt.show()
elif choice == 2:
    # Histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df["ESTIMATE"], bins=5, edgecolor="k")
    plt.title("Histogram: Suicide Death Rates")
    plt.xlabel("Death Rate (per 100,000 population)")
    plt.ylabel("Frequency")
    plt.grid(axis="y")
    plt.show()
elif choice == 3:
    # Scatter Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["YEAR"], df["ESTIMATE"], s=50, alpha=0.7)
    plt.title("Scatter Plot: Suicide Death Rates Over Time")
    plt.xlabel("Year")
    plt.ylabel("Death Rate (per 100,000 population)")
    plt.grid(True)
    plt.show()
elif choice == 4:
    # Line Graph
    plt.figure(figsize=(10, 6))
    plt.plot(df["YEAR"], df["ESTIMATE"], marker='o', linestyle='-')
    plt.title("Line Graph: Suicide Death Rates Over Time")
    plt.xlabel("Year")
    plt.ylabel("Death Rate (per 100,000 population)")
    plt.grid(True)
    plt.show()
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
