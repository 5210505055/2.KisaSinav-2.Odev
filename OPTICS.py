import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import OPTICS
from sklearn.preprocessing import StandardScaler

# Veri Ön İşleme
data = pd.read_excel(r'C:/python/belajar/Mall_Customers.xlsx')


# Kategori veriyi numerik veriye dönüştürmek 
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# veri standartlaştırma
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# OPTICS Algoritması
optics = OPTICS(min_samples=5, xi=0.05, min_cluster_size=0.1)  # OPTICS modelini başlatmak
optics.fit(data_scaled)  # kümeleme işlemi gerçekleştirmek(clustering)

# Kümeleme Sonuçlarını Görselleştirmek
data['Cluster'] = optics.labels_  # Veri DataFrame'ine 'Cluster' sütunu eklemek

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Spending Score (1-100)', hue='Cluster', data=data, palette='rainbow')
plt.show()
