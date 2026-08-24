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