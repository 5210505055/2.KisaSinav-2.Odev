import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import OPTICS
from sklearn.preprocessing import StandardScaler

# Step 1: Praproses Data
data = pd.read_excel(r'C:/python/belajar/Mall_Customers.xlsx')
#data = data[['Age', 'Spending Score (1-100)', 'Gender']]  # Menghilangkan fitur yang tidak relevan

# Mengubah data kategorikal menjadi numerik (jika diperlukan)
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# Melakukan standarisasi data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Step 2: Menerapkan Algoritma OPTICS
optics = OPTICS(min_samples=5, xi=0.05, min_cluster_size=0.1)  # Menginisialisasi model OPTICS
optics.fit(data_scaled)  # Melakukan klasterisasi

# Step 3: Memvisualisasikan Hasil Klasterisasi
data['Cluster'] = optics.labels_  # Menambahkan kolom "Cluster" ke DataFrame data

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Spending Score (1-100)', hue='Cluster', data=data, palette='rainbow')
plt.show()
