import streamlit as st

# ==========================================
# 1. KELAS BARANG (Model Data)
# ==========================================
class Barang:
    def __init__(self, kode, nama, jumlah):
        self.kode = kode
        self.nama = nama
        self.jumlah = jumlah

    def __str__(self):
        return f"Kode: {self.kode} | Nama: {self.nama} | Jumlah: {self.jumlah}"

# ==========================================
# 2. KELAS NODE & LINKED LIST
# ==========================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class GudangLinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_awal(self, barang):
        node_baru = Node(barang)
        node_baru.next = self.head
        self.head = node_baru
        return f"Barang '{barang.nama}' berhasil masuk ke gudang."

    def sisip_setelah(self, kode_target, barang_baru):
        pointer = self.head
        while pointer:
            if pointer.data.kode == kode_target:
                node_baru = Node(barang_baru)
                node_baru.next = pointer.next
                pointer.next = node_baru
                return f"Barang '{barang_baru.nama}' ditambahkan setelah '{kode_target}'."
            pointer = pointer.next
        return f"ERROR: Kode '{kode_target}' tidak ditemukan."

    def hapus_barang(self, kode):
        if self.head is None:
            return "Gudang kosong."

        if self.head.data.kode == kode:
            self.head = self.head.next
            return f"Barang dengan kode '{kode}' berhasil dihapus."

        pointer = self.head
        while pointer.next:
            if pointer.next.data.kode == kode:
                pointer.next = pointer.next.next
                return f"Barang dengan kode '{kode}' berhasil dihapus."
            pointer = pointer.next
        return f"ERROR: Barang dengan kode '{kode}' tidak ditemukan."

    def cari_barang(self, kode):
        pointer = self.head
        while pointer:
            if pointer.data.kode == kode:
                return f"Ditemukan: {pointer.data}"
            pointer = pointer.next
        return f"Barang dengan kode '{kode}' tidak ada di gudang."

    def tampilkan_daftar_list(self):
        # Mengembalikan list of string untuk ditampilkan di UI
        data_list = []
        pointer = self.head
        while pointer:
            data_list.append(str(pointer.data))
            pointer = pointer.next
        return data_list

# ==========================================
# 3. INISIALISASI STATE (Wajib di Streamlit)
# ==========================================
if 'gudang' not in st.session_state:
    st.session_state.gudang = GudangLinkedList()

    # Menambahkan data contoh awal
    b1 = Barang("1134", "Cover Safety          ", 300)
    b2 = Barang("1235", "Tool Box Penutup Bawah", 1150)
    b3 = Barang("1334", "Knob Wide             ", 750)
    b4 = Barang("1335", "Knob Shutter          ", 800)
    
    st.session_state.gudang.tambah_di_awal(b1)
    st.session_state.gudang.tambah_di_awal(b2)
    st.session_state.gudang.tambah_di_awal(b3)
    st.session_state.gudang.tambah_di_awal(b4)

# ==========================================
# 4. TAMPILAN UI STREAMLIT
# ==========================================
st.title("🏭 Aplikasi Gudang (Linked List)")

# --- SIDEBAR: MENU OPERASI ---
with st.sidebar:
    st.header("📂 Menu Operasi")
    menu = st.radio(
        "Pilih Operasi:",
        ("Tampilkan Daftar", "Tambah di Awal", "Sisip Setelah", "Cari Barang", "Hapus Barang")
    )

# --- LOGIKA PER MENU ---
gudang = st.session_state.gudang

if menu == "Tampilkan Daftar":
    st.subheader("📋 Daftar Barang di Gudang")
    data_nya = gudang.tampilkan_daftar_list()
    
    if not data_nya:
        st.info("Gudang masih kosong.")
    else:
        for item in data_nya:
            st.write(f"• {item}")

elif menu == "Tambah di Awal":
    st.subheader("📥 Tambah Barang di Awal")
    with st.form("form_tambah_awal"):
        kode = st.text_input("Kode Barang")
        nama = st.text_input("Nama Barang")
        jumlah = st.number_input("Jumlah", min_value=0, step=1)
        submit_awal = st.form_submit_button("Simpan")
        
        if submit_awal:
            if kode and nama:
                b_baru = Barang(kode, nama, int(jumlah))
                msg = gudang.tambah_di_awal(b_baru)
                st.success(msg)
            else:
                st.error("Kode dan Nama wajib diisi!")

elif menu == "Sisip Setelah":
    st.subheader("➕ Sisip Barang Setelah Kode Tertentu")
    with st.form("form_sisip"):
        kode_target = st.text_input("Kode Target (Acuan)")
        kode_baru = st.text_input("Kode Barang Baru")
        nama_baru = st.text_input("Nama Barang Baru")
        jumlah_baru = st.number_input("Jumlah", min_value=0, step=1)
        submit_sisip = st.form_submit_button("Sisipkan")
        
        if submit_sisip:
            if kode_target and kode_baru and nama_baru:
                b_baru = Barang(kode_baru, nama_baru, int(jumlah_baru))
                msg = gudang.sisip_setelah(kode_target, b_baru)
                if "ERROR" in msg:
                    st.error(msg)
                else:
                    st.success(msg)
            else:
                st.error("Semua field wajib diisi!")

elif menu == "Cari Barang":
    st.subheader("🔍 Cari Barang")
    with st.form("form_cari"):
        kode_cari = st.text_input("Masukkan Kode Barang")
        submit_cari = st.form_submit_button("Cari")
        
        if submit_cari:
            if kode_cari:
                msg = gudang.cari_barang(kode_cari)
                if "ERROR" in msg or "tidak ada" in msg:
                    st.warning(msg)
                else:
                    st.success(msg)
            else:
                st.error("Masukkan kode terlebih dahulu!")

elif menu == "Hapus Barang":
    st.subheader("🗑️ Hapus Barang")
    with st.form("form_hapus"):
        kode_hapus = st.text_input("Masukkan Kode Barang yang ingin dihapus")
        submit_hapus = st.form_submit_button("Hapus")
        
        if submit_hapus:
            if kode_hapus:
                msg = gudang.hapus_barang(kode_hapus)
                if "ERROR" in msg or "tidak ditemukan" in msg:
                    st.error(msg)
                else:
                    st.success(msg)
            else:
                st.error("Masukkan kode terlebih dahulu!")

# --- RESET DATA ---
if st.button("🔄 Reset Data Gudang"):
    st.session_state.gudang = GudangLinkedList()
    st.rerun()
