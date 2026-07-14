import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Basic cleaning
df['country'] = df['country'].fillna("Unknown")
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

# Set style
sns.set(style="darkgrid")

# Create one figure
plt.figure(figsize=(14,10))

# 🔹 1. Movies vs TV Shows
plt.subplot(2,2,1)
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows")

# 🔹 2. Top 5 Countries
plt.subplot(2,2,2)
df['country'].value_counts().head(5).plot(kind='bar')
plt.title("Top 5 Countries")

# 🔹 3. Content added over years
plt.subplot(2,2,3)
df['year_added'].value_counts().sort_index().plot()
plt.title("Content Added Over Years")

# 🔹 4. Pie Chart (Distribution)
plt.subplot(2,2,4)
type_counts = df['type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Movies vs TV Shows Distribution")

# Layout fix
plt.tight_layout()

# Show all graphs together
plt.show()