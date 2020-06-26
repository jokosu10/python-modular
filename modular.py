"""
Program untuk menghitung luas segitiga
"""

print('\n Menghitung luas segitiga without functiob')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas {luas_segitiga}')

print('\n Menghitung luas segitiga with function')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = (alas * tinggi) / 2
    return luas_segitiga

print(f'Menghitung luas segitiga dengan fungsi {hitung_luas_segitiga(20,2)}')
print(f'Menghitung luas segitiga dengan fungsi {hitung_luas_segitiga(10,2)}')
