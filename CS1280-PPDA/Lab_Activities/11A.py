import seaborn as sns
import matplotlib.pyplot as plt

def visualize_outliers(df, column):
    """Displays a box plot to visualize outliers."""
    sns.boxplot(x=df[column])
    plt.show()
