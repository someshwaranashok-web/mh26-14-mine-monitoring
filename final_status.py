import pandas as pd

data = pd.read_csv("sensor_results.csv")

total = len(data)
normal = (data["result"] == 1).sum()
anomalies = (data["result"] == -1).sum()

print("=" * 35)
print("MH26-14 SENSOR MONITOR")
print("=" * 35)

print("Total readings:", total)
print("Normal readings:", normal)
print("Anomalous readings:", anomalies)

if anomalies > 0:
    print("\nWARNING: Unusual sensor patterns detected!")
else:
    print("\nNORMAL: No unusual patterns detected.")

print("\nNote: This is simulated sensor data.")
print("An anomaly is not proof of mine subsidence.")
