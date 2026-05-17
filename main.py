import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("students.csv")

# Calculate Total
df["Total"] = df["Math"] + df["Physics"] + df["Python"]

# Calculate Percentage
df["Percentage"] = df["Total"] / 3

# Pass/Fail
df["Result"] = df["Percentage"].apply(
    lambda x: "Pass" if x >= 35 else "Fail"
)

# Rank Students
df["Rank"] = df["Percentage"].rank(
    ascending=False
)

# Display Data
print("\nSTUDENT RESULT ANALYSIS\n")
print(df)

# Find Topper
topper = df.loc[df["Percentage"].idxmax()]

print("\nTOPPER OF CLASS")
print(topper["Name"])

# Class Average
average = df["Percentage"].mean()

print("\nCLASS AVERAGE")
print(round(average, 2))

# Create Bar Graph
plt.bar(df["Name"], df["Percentage"])

plt.title("Student Percentage Analysis")
plt.xlabel("Students")
plt.ylabel("Percentage")

plt.show() 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

df["Total"] = df["Math"] + df["Physics"] + df["Python"]

df["Percentage"] = df["Total"] / 3

print(df)

plt.bar(df["Name"], df["Percentage"])

plt.show()
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

df["Total"] = df["Math"] + df["Physics"] + df["Python"]

df["Percentage"] = df["Total"] / 3

print(df)

plt.bar(df["Name"], df["Percentage"])

plt.show()
def grade(p):
    if p >= 90:
        return "A"
    elif p >= 75:
        return "B"
    elif p >= 50:
        return "C"
    else:
        return "D"

df["Grade"] = df["Percentage"].apply(grade)
df.to_csv("final_results.csv", index=False)
def grade(p):
    if p >= 90:
        return "A"
    elif p >= 75:
        return "B"
    elif p >= 50:
        return "C"
    else:
        return "D"

df["Grade"] = df["Percentage"].apply(grade)
df.to_csv("final_results.csv", index=False)
name = input("Enter student name: ")

student = df[df["Name"] == name]

print(student)
math_topper = df.loc[df["Math"].idxmax()]

print("\nMATH TOPPER")
print(math_topper["Name"])

df["Rank"] = df["Percentage"].rank(
    ascending=False
).astype(int)