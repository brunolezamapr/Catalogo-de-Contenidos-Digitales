
if __name__ == "__main__":

    from contenido_digital import ContenidoDigital
    from playlist_digital import PlaylistDigital

    print("\n" + "=" * 60)
    print("PRUEBA EJERCICIO 2: PLAYLIST Y CONTENIDO DIGITAL")
    print("=" * 60)

    c1 = ContenidoDigital("Podcast Python", 300)
    c2 = ContenidoDigital("Tutorial POO", 600)

    print(f"Formato estático (300s): {ContenidoDigital.formatear_tiempo(300)}") # 05:00

pl1 = PlaylistDigital("Tech")
pl1.agregar(c1)

pl2 = PlaylistDigital("Dev")
pl2.agregar(c2)

pl_combinada = pl1 + pl2
print(f"Total contenidos en playlist combinada: {len(pl_combinada)}") # 2
print(f"Primer contenido: {pl_combinada[0].titulo}") # Podcast Python