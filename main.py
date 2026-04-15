import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data.csv')

# -------- LINE CHART --------
plt.figure(figsize=(8,5))
plt.plot(data['StudyHours'], data['Marks'], marker='o')

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.grid(True)
plt.savefig("line_chart.png")
plt.show()


# -------- BAR CHART --------
plt.figure(figsize=(8,5))
plt.bar(data['Name'], data['Marks'])

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks of Students")
plt.savefig("line_chart.png")
plt.show()

# -------- HISTOGRAM --------
plt.figure(figsize=(8,5))

plt.hist(data['Marks'], bins=5)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")
plt.savefig("line_chart.png")
plt.show()