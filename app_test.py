import numpy as np
import pandas as pd

raw_data = {
    "rider_name": ["Raju", "Shyam", "Raju", "Raju", "Shyam"],
    "distance_km": [5.2, 3.8, 7.1, 4.5, 6.0],
    "time_taken_mins": [15, 10, 20, 12, 18]
}

df = pd.DataFrame(raw_data)

print("--- Database se aaya raw data --- ")
print(f"{df}\n")

avg_performance = df.groupby("rider_name")['time_taken_mins'].mean()
print("--- Average Performance ---")
print(avg_performance)
