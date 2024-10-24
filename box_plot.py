import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('latency_results.csv')

df['Test Case'] = df.groupby('Text').ngroup()

# Create a boxplot for each test case
plt.figure(figsize=(12, 8))
df.boxplot(column='Latency (s)', by='Test Case')
plt.title('Latency Performance by Test Case')
plt.suptitle('')
plt.xlabel('Test Case')
plt.ylabel('Latency (seconds)')

# Calculate and annotate the average performance for each test case
avg_latency = df.groupby('Test Case')['Latency (s)'].mean()

for test_case, avg in avg_latency.items():
    plt.text(test_case + 1, avg, f'Avg: {avg:.4f}s', horizontalalignment='center', color='blue')

# Save the plot to a file
plt.savefig('latency_performance_boxplot.png')
