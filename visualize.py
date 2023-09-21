import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
data = pd.read_csv("suicide_reates.csv")

# Create a new DataFrame (data2) without the "INDICATOR" and "UNIT" columns
data2 = data.drop(columns=["INDICATOR", "UNIT", "FLAG"])

# Count the occurrences of each unique value in the "STUB_LABEL" column
stub_label_counts = data2["STUB_LABEL"].value_counts()

# Extract the "INDICATOR" value to use as the title
indicator_label = data['INDICATOR'].iloc[0]

# Create a 2x2 grid of plots
plt.figure(figsize=(12, 10))

# Plot 1: Scatter plot (AGE_NUM vs. ESTIMATE)
plt.subplot(2, 2, 1)
plt.scatter(data2["AGE_NUM"], data2["ESTIMATE"], marker='o', color='green', alpha=0.5)
plt.title("Scatter Plot: AGE_NUM vs. ESTIMATE")
plt.xlabel("AGE_NUM")
plt.ylabel("ESTIMATE")

# Plot 2: Histogram (AGE_NUM distribution)
plt.subplot(2, 2, 2)
plt.hist(data2["AGE_NUM"], bins=10, color='blue', alpha=0.7)
plt.title("Histogram: AGE_NUM Distribution")
plt.xlabel("AGE_NUM")
plt.ylabel("Frequency")

# Plot 3: Bar graph for "STUB_NAME" vs. "STUB_NAME_NUM"
plt.subplot(2, 2, 3)
stub_name_data = data2['STUB_NAME']
stub_name_num_data = data2['STUB_NAME_NUM']
plt.bar(stub_name_data, stub_name_num_data, color='purple', alpha=0.7)
plt.title("Bar Graph: STUB_NAME vs. STUB_NAME_NUM")
plt.xlabel("STUB_NAME")
plt.ylabel("STUB_NAME_NUM")
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

# Plot 4: Line graph (STUB_NAME_NUM vs. YEAR)
plt.subplot(2, 2, 4)
plt.plot(data2["YEAR"],data2["STUB_NAME_NUM"], marker='o', linestyle='-')
plt.title("Line Graph: STUB_NAME_NUM vs. YEAR")
plt.ylabel("STUB_NAME_NUM")
plt.xlabel("YEAR")

# Add a title for the entire set of plots
plt.suptitle(f"Data Visualization for: {indicator_label}", fontsize=16)

# Adjust layout and show the plots
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
