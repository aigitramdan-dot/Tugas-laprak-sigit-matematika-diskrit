bayar_cash = True
bayar_transfer = False

# LOGIKA
if bayar_cash ^ bayar_transfer:
    pembayaran = True
else:
    pembayaran = False

# OUTPUT
if pembayaran:
    print("Pembayaran berhasil")
else:
    print("Pilih salah satu metode pembayaran")