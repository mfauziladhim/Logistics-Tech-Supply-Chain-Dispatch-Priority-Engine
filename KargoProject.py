import numpy as np
import pandas as pd

zona = np.random.choice([1, 2, 3, 4, 5], size=20)
berat_paket = np.random.choice(range(10, 20), size=20)
nilai = np.random.choice(range(10000000, 50000000), size=20)
deadline =np.random.choice(range(1, 5), size=20)
jenis_kargo = np.random.choice(range(1,  3), size=20)

data = pd.DataFrame({
'id' : np.arange(1, 21, 1),
'zona' : zona,
'berat_paket' : berat_paket,
'nilai' : nilai,
'jenis_kargo' : jenis_kargo,
'deadline' : deadline,
}) 

data = data.set_index('id')

data['nilai_juta'] = data['nilai'] / 1000000

data['nilai_gabungan_deadline'] = 1 / data['deadline']

data['kepadatan'] = data['nilai_juta'] / berat_paket

data['variabel_penentu'] = 40 * data['nilai_gabungan_deadline'] + 30 * data['kepadatan'] + 30

pengangkutan_barang = data.nlargest(5, 'variabel_penentu')

print(pengangkutan_barang)





#import numpy as np
#import pandas as pd

# 1. Dataset Awal
#zona = np.random.choice([1, 2, 3, 4, 5], size=20)
#berat_paket = np.random.choice(range(10, 20), size=20)
#nilai = np.random.choice(range(10000000, 50000000), size=20)
#deadline = np.random.choice(range(1, 5), size=20)
#jenis_kargo = np.random.choice(range(1, 3), size=20) # 1: Standard, 2: Express/Perishable

#data = pd.DataFrame({
#    'id' : np.arange(1, 21, 1),
#    'zona' : zona,
#    'berat_paket' : berat_paket,
#    'nilai' : nilai,
#    'jenis_kargo' : jenis_kargo,
#    'deadline' : deadline,
#}).set_index('id')

# 2. Penyetaraan Skala Variabel
# Konversi nilai ke satuan Juta agar angkanya berkisar 10 - 50
#data['nilai_juta'] = data['nilai'] / 1_000_000

# Kepadatan Nilai per Kg (Skala: ~0.5 sampai 5.0)
#data['kepadatan'] = data['nilai_juta'] / data['berat_paket']

# Urgensi Deadline (Skala: 0.25 sampai 1.0)
#data['urgensi_deadline'] = 1 / data['deadline']

# 3. Rumus Variabel Penentu yang Seimbang (Total Bobot 100%)
# Urgensi Deadline (40%), Kepadatan Nilai (35%), Faktor Jenis Kargo (25%)
#data['variabel_penentu'] = (
#    (0.40 * data['urgensi_deadline']) + 
#    (0.35 * data['kepadatan']) + 
#    (0.25 * data['jenis_kargo'])
#).round(2)

# 4. Filter 5 Barang Prioritas Utama (Bukan sekadar head(5))
#pengangkutan_barang = data.nlargest(5, 'variabel_penentu')

#print("=== 5 BARANG PRIORITAS UTAMA PENGANGKUTAN ===")
#print(pengangkutan_barang[['zona', 'berat_paket', 'nilai_juta', 'deadline', 'jenis_kargo', 'variabel_penentu']])
