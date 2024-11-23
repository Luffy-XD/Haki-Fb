
2. **Buat Skrip Python**: Buat file Python baru, misalnya `google_scholar_trends.py`, dan masukkan kode berikut:

```python
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Inisialisasi koneksi ke Google Trends
pytrends = TrendReq(hl='en-US', tz=360)

# Membangun payload untuk kata kunci "Google Scholar"
kw_list = ["Google Scholar"]
pytrends.build_payload(kw_list, timeframe='today 5-y')  # Mengambil data selama 5 tahun terakhir

# Mengambil data minat seiring waktu
data = pytrends.interest_over_time()

# Mengolah data untuk mendapatkan jumlah pencarian per tahun
data['year'] = data.index.year
yearly_data = data.groupby('year').sum()

# Menyimpan data ke dalam file CSV
yearly_data.to_csv('google_scholar_trends.csv')

# Visualisasi data
plt.figure(figsize=(10, 5))
plt.plot(yearly_data.index, yearly_data['Google Scholar'], marker='o')
plt.title('Jumlah Pengguna Google Scholar per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Pencarian')
plt.grid()
plt.savefig('google_scholar_trends.png')  # Menyimpan grafik sebagai file gambar
plt.show()
