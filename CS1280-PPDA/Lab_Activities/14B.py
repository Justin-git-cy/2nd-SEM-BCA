# Sample DataFrame
df = sns.load_dataset("iris")  

sns.pairplot(df, hue="species")  
plt.show()
