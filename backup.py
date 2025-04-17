import os

# Fungsi untuk mengecek apakah file HTML memiliki tag meta charset="UTF-8"
def filter_html_by_utf8(directory):
    # Menyaring semua file HTML dalam direktori
    for filename in os.listdir(directory):
        if filename.endswith(".html"):  # Pastikan file dengan ekstensi .html
            filepath = os.path.join(directory, filename)
            
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Cek apakah ada tag <meta charset="UTF-8">
                if '<meta charset="UTF-8">' in content:
                    print(f"File {filename} memiliki charset UTF-8.")
                else:
                    print(f"File {filename} tidak memiliki charset UTF-8.")

# Ganti dengan direktori tempat file HTML kamu berada
directory_path = "/home/videos/htm"
filter_html_by_utf8(directory_path)
