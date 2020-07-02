"""
Tipe data dictionary menghubungkan antara KEY dan VALUE
KVP = KEY VALUE PAIR
dictionary = kamus
"""

kamus_ind_eng = {'Tenaga': 'Power', 'Kuda': 'Horse', 'Cepat': 'Fast', 'Tak tertandingi': 'Unbeaten'}

print(kamus_ind_eng)
print(kamus_ind_eng['Tenaga'])
print(kamus_ind_eng['Kuda'])

print('Data ini dikirimkan oleh server Grab untuk memberikan informasi driver di sekitar pemakai aplikasi')
data_server_Grab = {
    'tanggal': '2020-07-02',
    'daftar_driver': [
        {'nama': 'Arjuna', 'jarak': 10},
        {'nama': 'Bhima', 'jarak': 500},
        {'nama': 'Yudistira', 'jarak': 700},
        {'nama': 'Birawa', 'jarak': 1200}
    ]
}
print(data_server_Grab)
print(f"\nDriver sekitar sini {data_server_Grab['daftar_driver']}")
print(f"Driver 1. {data_server_Grab['daftar_driver'][0]}")
print(f"Driver 3. {data_server_Grab['daftar_driver'][2]}")
print(f"\ndriver terdekat berjarak {data_server_Grab['daftar_driver'][3]['jarak']} meter")
