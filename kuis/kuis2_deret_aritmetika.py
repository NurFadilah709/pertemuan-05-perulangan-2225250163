
print("Program Deret Aritmetika")

a = float(input("Suku pertama (a): "))
d = float(input("Beda (d): "))
n = int(input("Banyak suku (n): "))

while n <= 0:
    print("Banyak suku harus positif!")
    n = int(input("Banyak suku (n): "))

total = 0
suku = a

for i in range(1, n + 1):
    print(f"Suku ke-{i}: {suku}")
    total += suku
    suku += d

print(f"Jumlah deret = {total:.2f}")