def normalisasi_nama(nama):
    return " ".join(nama.strip().title().split())


def buat_inisial(nama):
    kata = normalisasi_nama(nama).split()
    return "".join(k[0] for k in kata).upper()


def normalisasi_kode(kode):
    return kode.strip().upper().replace(" ", "")


nama = input("Nama: ")
kode = input("Kode kelas: ")

nama_bersih = normalisasi_nama(nama)
inisial = buat_inisial(nama)
kode_bersih = normalisasi_kode(kode)

print(f"Nama normalisasi = {nama_bersih}")
print(f"Inisial = {inisial}")
print(f"Kode kelas = {kode_bersih}")