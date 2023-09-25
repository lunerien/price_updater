# Określ nazwę pliku txt
nazwa_pliku = "./unformatted.txt"

found_words = []

coins = open('coins.txt', 'w', encoding='utf-8')
coins.write("(")


# Otwórz plik do odczytu
try:
    with open(nazwa_pliku, "r") as plik:
        # Iteruj przez każdą linijkę pliku
        for numer_linii, linia in enumerate(plik, 1):
            if linia.startswith(('a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z')):
                if not linia.isupper():
                    if not (linia in found_words):
                        coin = linia.lower()
                        coin = coin.replace(" ", "-")
                        coin = coin.replace("\n", "")
                        print("zapisuje: ", coin)
                        found_words.append(linia)
                        coin = f"'{coin}',"
                        print(coin)
                        coins.write(coin)
    coins.write(")")

except FileNotFoundError:
    print(f"Plik '{nazwa_pliku}' nie został znaleziony.")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
