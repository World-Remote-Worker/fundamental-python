print('Tipe data skalar => tipe data sederhana')
anak1 = 'Arjuna'
anak2 = 'Bhima'
anak3 = 'Yudistira'
anak4 = 'Birawa'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\nTipe data daftar/list/array')
anak = ['Arjuna', 'Bhima', 'Yudistira', 'Birawa']
print(anak)
anak.append('Kurawa')
print(anak)

print('\nSapa anak ke-3')
print(f'Hello {anak[2]}!')

print('\nSapa semua anak!')
for a in anak:
    print(f'Hello {a}!')

print('\nSapa semua anak!: cara rumit')
for a in range(0, len(anak)):
    print(f'{a+1}. Hello {anak[a]}')
