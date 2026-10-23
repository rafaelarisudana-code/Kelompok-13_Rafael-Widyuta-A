
def sapa_petugas(nama, asal_daerah): 

    print(f"Selamat datang {nama} dari {asal_daerah} di sistem pemantauan Sungai Desa Patakbanteng.") 

 
def cek_status_air(tinggi_air): 

    print(f"Ketinggian air yang tercatat: {tinggi_air} cm") 

    if tinggi_air < 100: 

        return "Status: Aman, debit air normal." 

    elif tinggi_air < 200: 

        return "Status: Waspada, debit air meningkat." 

    else: 

        return "Status: Bahaya, potensi banjir!" 

def catat_pos_pantau(*pos_lokasi): 

    print("Pos pemantauan yang sedang aktif:") 

    for lokasi in pos_lokasi: 

        print(f"- {lokasi}") 

hitung_kenaikan = lambda x, y: x - y 

 
sapa_petugas("Rafael Widyuta A", "Jakarta") 

print("-" * 30) 

hasil_air = cek_status_air(150) 

print(hasil_air) 

print("-" * 30) 

catat_pos_pantau("Jembatan Utama", "Bendungan Kecil", "Hulu Sungai") 

print("-" * 30) 

print("Kenaikan air hari ini dibanding kemarin:", 

      hitung_kenaikan(150, 120), "cm") 