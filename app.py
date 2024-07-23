import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib


df = pd.read_csv("data/cases_cumulative_daily.csv", encoding="utf-8")

df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(8, 3))

plt.plot(df["Date"], df["Iwate"], label="Iwate", color="y")
plt.plot(df["Date"], df["Tokyo"], label="Tokyo", color="b")

plt.title("岩手・東京-コロナ感染者数")
plt.xlabel("日付")
plt.ylabel("感染者数")

plt.grid(True)
plt.xticks(rotation=45)

plt.legend()
plt.show()
