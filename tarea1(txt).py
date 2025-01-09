# Leer archivo y mandarlo a consola
with open(
    "quota.txt", "r", encoding="utf-8"
) as file:
    data = file.read()
    print(data)

# Preguntar nombre del autor
autor = input("Ingrese nombre del autor:\n")

# Añadir el nombre del autor al grupo
with open(
    "quota.txt", "a", encoding="utf-8"
) as name:
    write = name.write(f"\n({autor})")

# Volver a leer archivo con el nombre del autor ya escrito y mandarlo a consola
with open(
    "quota.txt", "r", encoding="utf-8"
) as Newfile:
    data2 = Newfile.read()
    print(data2)
