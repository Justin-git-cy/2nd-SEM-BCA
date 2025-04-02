import seaborn as sns

# Load sample dataset
penguins = sns.load_dataset("penguins")

# Create pair plot
sns.pairplot(penguins, hue="species", diag_kind="kde")
plt.show()
