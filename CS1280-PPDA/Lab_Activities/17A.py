import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset("penguins")

# Create bar plot
plt.figure(figsize=(8, 5))
sns.barplot(data=penguins, x="species", y="body_mass_g", estimator=sum, ci=None, palette="viridis")

# Add title and labels
plt.title("Total Body Mass by Penguin Species")
plt.xlabel("Species")
plt.ylabel("Total Body Mass (g)")

# Show plot
plt.show()
