import tkinter as tk

def show_about_window(root):
    about_win = tk.Toplevel(root)
    about_win.title("Tentang Aplikasi")
    about_win.geometry("400x400")
    about_win.configure(bg="#e3f2fd")

    tk.Label(
        about_win,
        text="🧹 Remove Background App",
        font=("Segoe UI", 14, "bold"),
        bg="#e3f2fd",
        fg="#0d47a1"
    ).pack(pady=10)

    info_text = (
        "Aplikasi ini membantu kamu menghapus atau mengganti\n"
        "background gambar dengan cepat dan mudah.\n\n"
        "Fitur utama:\n"
        "• Hapus background otomatis\n"
        "• Ganti warna background\n"
        "• Ganti background dengan gambar lain\n"            
        "• Preview hasil sebelum disimpan"
        "• Membuka gambar (PNG, JPG, JPEG)\n"

        "Dibuat oleh:\n"
        "1. CAESAR GALANG RESTU RAMADHAN\n"
        "2. FATKURRAHMAN RAFIE WIBOWO\n"
        "3. ROIHAN ARRAFLI\n"
        "4. TIYAS STYANINGRUM\n"
        "5. TRI AGUSTINA DIVA SARI\n\n"
    )

    tk.Label(
        about_win,
        text=info_text,
        justify="left",
        font=("Segoe UI", 10),
        bg="#e3f2fd",
        fg="#000000"
    ).pack(padx=20, pady=10)

    tk.Button(
        about_win,
        text="Tutup",
        command=about_win.destroy,
        bg="#42a5f5",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        width=10
    ).pack(pady=10)


















