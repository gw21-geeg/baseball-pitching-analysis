import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("active-spin.csv")
print(df.head())
print(df.columns)
print(df.shape)
print(df[["entity_name", "pitch_hand", "active_spin_fourseam"]].sort_values("active_spin_fourseam", ascending=False).head(10))
average_spin = df["active_spin_fourseam"].mean()
print("Average Four-Seam Active Spin:")
print(round(average_spin, 2))
handedness_avg = df.groupby("pitch_hand")["active_spin_fourseam"].mean()

print("\nAverage Active Spin by Pitcher Hand:")
print(handedness_avg)
handedness_avg = df.groupby("pitch_hand")["active_spin_fourseam"].mean()
handedness_avg.plot(kind="bar")
plt.title("Average Four-Seam Active Spin by Pitcher Hand")
plt.xlabel("Pitcher Hand")
plt.ylabel("Active Spin %")
plt.show()
df["active_spin_fourseam"].plot(kind="hist")
plt.show()
below_85 = df[df["active_spin_fourseam"] < 85]
print(below_85[["entity_name", "pitch_hand", "active_spin_fourseam"]])
print(df["active_spin_fourseam"].count())
below_85 = df[df["active_spin_fourseam"] < 85]

print("\nPitchers below 85% active spin:")
print(len(below_85))
