import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
penguins = sns.load_dataset("penguins")

# Compute correlation matrix (dropping non-numeric columns)
corr_matrix = penguins.drop(columns=["species", "island", "sex"]).corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()
