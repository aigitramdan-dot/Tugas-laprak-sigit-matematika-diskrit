username_benar = True
password_benar = True

# LOGIKA
if username_benar and password_benar:
    login = True
else:
    login = False

# OUTPUT
if login:
    print("Login berhasil")
else:
    print("Login gagal")