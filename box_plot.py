import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('latency_results.csv')

# Create a boxplot for latency
plt.figure(figsize=(10, 6))
df.boxplot(column='Latency (s)', by='Prediction')
plt.title('Latency Performance by Prediction')
plt.suptitle('')  # Suppress the automatic title to clean up the plot
plt.xlabel('Prediction (Fake/Real)')
plt.ylabel('Latency (seconds)')

# Save the plot to a file
plt.savefig('latency_performance_boxplot.png')  # This saves it to the same folder as your script
