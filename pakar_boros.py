def diagnosa_boros(jawaban):
   
    if len(jawaban) < 8:
        return {"error": "Jawaban tidak lengkap"}

    j = jawaban[:8]

    s_impulsif  = j[0] + j[7]
    s_tabungan  = j[1] + j[5]
    s_konsumtif = j[2] + j[3]
    s_utang     = j[4] + j[6]
    total       = sum(j)
    pct         = total / (8 * 3)

    booster = 0
    if len(jawaban) >= 10:
        booster = jawaban[8] + jawaban[9]

    if s_impulsif >= 4 and s_konsumtif >= 3:
        return {
            "diagnosis": "Impulsive Buyer",
            "deskripsi": "Kamu cenderung membeli berdasarkan emosi sesaat, bukan kebutuhan. Pola ini menguras keuangan tanpa disadari.",
            "tipe": "Impulsif",
            "risiko": "Sangat Tinggi" if booster >= 4 else "Tinggi",
            "fokus": "Kontrol Belanja",
            "target": "30 Hari",
            "saran": [
                {"judul": "Terapkan aturan 24 jam", "isi": "Tunggu 24 jam sebelum beli barang tidak direncanakan. Jika masih ingin, baru beli."},
                {"judul": "Hapus aplikasi belanja online", "isi": "Matikan notifikasi promo untuk mengurangi godaan belanja impulsif."},
                {"judul": "Buat wishlist bulanan", "isi": "Daftar barang yang ingin dibeli beserta anggarannya. Beli hanya yang ada di list."},
                {"judul": "Hindari belanja saat stres", "isi": "Cari aktivitas pengganti seperti olahraga atau jalan-jalan gratis saat ingin belanja impulsif."}
            ]
        }

    elif s_tabungan >= 4 and s_utang >= 4:
        return {
            "diagnosis": "Financial Risk Zone",
            "deskripsi": "Tidak ada tabungan, tidak ada dana darurat, dan terbebani utang. Kondisi ini sangat rentan terhadap krisis keuangan mendadak.",
            "tipe": "Tidak Terstruktur",
            "risiko": "Sangat Tinggi",
            "fokus": "Stabilisasi Keuangan",
            "target": "3 Bulan",
            "saran": [
                {"judul": "Buat dana darurat mini dulu", "isi": "Targetkan Rp500rb-1jt sebagai buffer darurat sebelum fokus ke hal lain."},
                {"judul": "Hentikan utang baru", "isi": "Fokus lunasi utang dengan bunga tertinggi terlebih dahulu (metode avalanche)."},
                {"judul": "Cari penghasilan tambahan", "isi": "Dengan kondisi ini, mengurangi pengeluaran saja tidak cukup. Perlu tambah pemasukan."},
                {"judul": "Konsultasi ke perencana keuangan", "isi": "Kondisimu membutuhkan strategi yang lebih terstruktur. Pertimbangkan konsultasi profesional."}
            ]
        }

    elif s_konsumtif >= 4 and s_tabungan >= 2:
        return {
            "diagnosis": "Konsumtif Tanpa Kontrol",
            "deskripsi": "Pengeluaran harian terlalu tinggi dan tidak terkontrol. Perlu ada batas yang jelas.",
            "tipe": "Konsumtif",
            "risiko": "Sedang–Tinggi",
            "fokus": "Budgeting Harian",
            "target": "2 Minggu",
            "saran": [
                {"judul": "Catat pengeluaran harian 2 minggu", "isi": "Gunakan aplikasi atau notes HP. Kesadaran adalah langkah pertama perubahan."},
                {"judul": "Terapkan budgeting 50/30/20", "isi": "50% kebutuhan, 30% keinginan, 20% tabungan. Mulai dari bulan depan."},
                {"judul": "Masak sendiri 3-4x seminggu", "isi": "Bisa hemat 40-60% dari biaya makan bulanan. Mulai dari sarapan."},
                {"judul": "Tetapkan batas harian", "isi": "Tentukan batas pengeluaran harian maksimal dan patuhi dengan ketat."}
            ]
        }

    elif j[3] >= 2 and j[6] >= 2:
        return {
            "diagnosis": "Tidak Berencana",
            "deskripsi": "Tidak ada budget dan tidak ada dana darurat. Rentan terhadap kejutan keuangan kapan saja.",
            "tipe": "Tidak Terencana",
            "risiko": "Sedang",
            "fokus": "Perencanaan",
            "target": "1 Bulan",
            "saran": [
                {"judul": "Buat anggaran bulan ini", "isi": "Tulis pemasukan lalu alokasikan ke kebutuhan, tabungan, dan gaya hidup."},
                {"judul": "Otomatisasi tabungan", "isi": "Set auto-transfer ke rekening tabungan di tanggal gajian sebelum sempat dipakai."},
                {"judul": "Target dana darurat 3 bulan", "isi": "Sisihkan sedikit tapi konsisten setiap bulan selama 1 tahun."},
                {"judul": "Gunakan aplikasi keuangan", "isi": "Pakai aplikasi seperti Money Manager atau Wallet untuk tracking otomatis."}
            ]
        }

    elif pct <= 0.3 and booster <= 2:
        return {
            "diagnosis": "Finansial Cukup Sehat",
            "deskripsi": "Kebiasaan finansialmu sudah cukup baik! Tidak impulsif, punya tabungan, dan relatif terkontrol. Saatnya naik level.",
            "tipe": "Terencana",
            "risiko": "Rendah",
            "fokus": "Optimasi & Investasi",
            "target": "Jangka Panjang",
            "saran": [
                {"judul": "Mulai investasi reksadana atau saham", "isi": "Dana yang sudah aman di tabungan bisa dikembangkan melalui instrumen investasi."},
                {"judul": "Tingkatkan persentase tabungan", "isi": "Jika sudah menabung 10%, coba tingkatkan ke 15-20% dari pemasukan."},
                {"judul": "Buat target keuangan 1-5 tahun", "isi": "Tulis target (rumah, menikah, pensiun dini) dan hitung berapa yang perlu disiapkan."},
                {"judul": "Diversifikasi investasi", "isi": "Jangan taruh semua di satu instrumen. Kombinasikan saham, obligasi, dan emas."}
            ]
        }

    else:
        return {
            "diagnosis": "Perlu Perhatian Lebih",
            "deskripsi": "Ada beberapa kebiasaan keuangan yang perlu diperbaiki. Belum darurat, tapi perlu segera ditangani.",
            "tipe": "Kurang Konsisten",
            "risiko": "Sedang",
            "fokus": "Konsistensi",
            "target": "2 Bulan",
            "saran": [
                {"judul": "Identifikasi kebocoran terbesar", "isi": "Cari tahu pengeluaran apa yang paling besar dan tidak perlu, lalu kurangi."},
                {"judul": "Bayar diri sendiri dulu", "isi": "Sisihkan tabungan di awal bulan, bukan dari sisa akhir bulan."},
                {"judul": "Evaluasi keuangan tiap akhir bulan", "isi": "Luangkan 15 menit untuk review pengeluaran dan progres tabungan."},
                {"judul": "Tetapkan 1 kebiasaan baru per bulan", "isi": "Jangan ubah semua sekaligus. Fokus pada 1 perubahan kecil yang konsisten."}
            ]
        }