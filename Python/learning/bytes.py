# Беззнаковые целые в мире байтов: они скрываются от вас!
unsigned_int = 1024
bytes_unsigned = unsigned_int.to_bytes((unsigned_int.bit_length() + 7), 'big')

# Знаковые целые попадают в бинарные ловушки!
signed_int = -1024
bytes_signed = signed_int.to_bytes(((signed_int).bit_length() + 7) // 8, 'big', signed=True)
print(bytes_unsigned)
print(bytes_signed)

signed_int = int.from_bytes(bytes_signed, 'big', signed=True)
unsigned_int = int.from_bytes(bytes_unsigned, "big")
print(unsigned_int, signed_int, sep="\n")



var = "www"
byt_var = bytes(var, "utf-8")
print(byt_var)