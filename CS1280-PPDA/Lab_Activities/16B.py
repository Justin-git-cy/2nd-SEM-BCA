import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(8, 5))
sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="species", style="species", s=100)
plt.title("Relationship Between Flipper Length and Body Mass")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()
