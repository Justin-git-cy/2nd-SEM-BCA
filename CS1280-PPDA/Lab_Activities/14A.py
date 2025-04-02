import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
penguins = sns.load_dataset("penguins")

# Plot histogram and KDE for flipper_length_mm
plt.figure(figsize=(8, 5))
sns.histplot(penguins["flipper_length_mm"], bins=20, kde=True, color="blue")
plt.title("Distribution of Flipper Length in Penguins")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Frequency")
plt.show()
