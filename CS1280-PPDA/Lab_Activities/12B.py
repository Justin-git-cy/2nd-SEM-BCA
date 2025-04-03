Q1 = df["Values"].quantile(0.25)  
Q3 = df["Values"].quantile(0.75)  
IQR = Q3 - Q1 

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["Values"] < lower_bound) | (df["Values"] > upper_bound)]
print("\nOutliers detected:\n", outliers)
