import time
import csv
import requests

# Define test cases
test_cases = [
    {'text': 'Drinking Age at Disney World May be Lowered to 18'}, # Fake
    {'text': 'Justin Trudeau pressured to resign by MPs within own party'}, # Real
    {'text': 'Fred Rogers served as a sniper during the Vietnam War'}, # Fake
    {'text': 'Trump nearly assassinated at rally'} # Real
]

url = 'http://pra5.eba-ujxy8kkb.us-east-2.elasticbeanstalk.com/predict'

# Record timestamps and responses
results = []

for test_case in test_cases:
    for _ in range(25):  # Run each test case 25 times
        start_time = time.time()
        response = requests.post(url, json=test_case)
        end_time = time.time()

        latency = end_time - start_time
        result = response.json()

        results.append([latency, result['prediction'], test_case['text']])

# Write results to a CSV file
with open('latency_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Latency (s)', 'Prediction', 'Text'])
    writer.writerows(results)

print("Latency test complete. Results saved in latency_results.csv.")