import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
penguins = sns.load_dataset("penguins").dropna()

# Sort data by body mass for trend visualization
penguins = penguins.sort_values(by="body_mass_g")

# Plot line chart
plt.figure(figsize=(8, 5))
sns.lineplot(x=range(len(penguins)), y=penguins["body_mass_g"], marker="o", color="blue")
plt.title("Trend of Body Mass in Penguins")
plt.xlabel("Sample Index")
plt.ylabel("Body Mass (g)")
plt.show()
