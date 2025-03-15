from google_play_scraper import reviews,Sort
import pandas as pd

# Nama package aplikasi di Play Store
APP_ID = "com.mobilechess.gp"


# Mengambil 30000 ulasan pertama
all_reviews, _ = reviews(
    app_id=APP_ID,
    lang='id',  # Bahasa Indonesia
    country='id',  # Negara Indonesia
    sort=Sort.NEWEST,  # Mengambil ulasan terbaru terlebih dahulu
    count=30000
)

# Memisahkan menjadi 15000 ulasan pertama dan 15000 ulasan terakhir
reviews_first = all_reviews[:15000]
reviews_last = all_reviews[-15000:]


# Menggabungkan kedua dataset
final_reviews = reviews_first + reviews_last


data = pd.DataFrame(final_reviews)

# Menampilkan nama kolom untuk pengecekan
print("Kolom yang tersedia:", data.columns)

# Memastikan hanya kolom yang tersedia yang disimpan ke CSV
available_columns = [col for col in ['userName', 'score', 'content'] if col in data.columns]
data[available_columns].to_csv("magic_chess_reviews.csv", index=False)

print("Scraping selesai. Data disimpan dalam magic_chess_reviews.csv")