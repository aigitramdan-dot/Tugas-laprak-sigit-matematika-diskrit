password_benar = False
sidik_jari_cocok = True

# LOGIKA
if password_benar or sidik_jari_cocok:
    akses = True
else:
    akses = False

# OUTPUT
if akses:
    print("Akses diterima")
else:
    print("Akses ditolak")