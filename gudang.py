import streamlit as st

class Barang:
    def __init__(self, kode, nama, jumlah):
        self.kode = kode
        self.nama = nama
        self.jumlah = jumlah

    def __str__(self):
        return f"Kode: {self.kode} | Nama: {self.nama} \t| Jumlah: {self.jumlah}"

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
        print(f"--> Barang '{barang.nama}' berhasil masuk ke gudang.")

    def sisip_setelah(self, kode_target, barang_baru):
        pointer = self.head
        while pointer:
            if pointer.data.kode == kode_target:
                node_baru = Node(barang_baru)
                node_baru.next = pointer.next
                pointer.next = node_baru
                print(f"--> Barang '{barang_baru.nama}' ditambahkan setelah '{kode_target}'.")
                return
            pointer = pointer.next
        print(f"---> ERROR: Kode '{kode_target}' tidak ditemukan.")

    def hapus_barang(self, kode):
        if self.head is None:
            print("Gudang kosong.")
            return

        if self.head.data.kode == kode:
            self.head = self.head.next
            print(f"--> Barang dengan kode '{kode}' berhasil dihapus.")
            return

        pointer = self.head
        while pointer.next:
            if pointer.next.data.kode == kode:
                pointer.next = pointer.next.next
                print(f"--> Barang dengan kode '{kode}' berhasil dihapus.")
                return
            pointer = pointer.next
        print(f"---> ERROR: Barang dengan kode '{kode}' tidak ditemukan.")

    def cari_barang(self, kode):
        pointer = self.head
        while pointer:
            if pointer.data.kode == kode:
                print("--> Ditemukan:", pointer.data)
                return
            pointer = pointer.next
        print(f"---> Barang dengan kode '{kode}' tidak ada di gudang.")

    def tampilkan_daftar(self):
        if self.head is None:
            print("Daftar Gudang: (Kosong)")
            return
        
        print("\n================== DAFTAR BARANG DI GUDANG ===================")
        pointer = self.head
        no = 1
        while pointer:
            print(f"{no}. {pointer.data}")
            pointer = pointer.next
            no += 1
        print("==============================================================\n")

if __name__ == "__main__":
    gudang_ku = GudangLinkedList()

    b1 = Barang("1134", "Cover Safety          ", 300)
    b2 = Barang("1235", "Tool Box Penutup Bawah", 1150)
    b3 = Barang("1334", "Knob Wide             ", 750)
    b4 = Barang("1335", "Knob Shutter          ", 800)

    gudang_ku.tambah_di_awal(b1)   
    gudang_ku.tambah_di_awal(b2)  
    gudang_ku.tambah_di_awal(b3)
    gudang_ku.tambah_di_awal(b4)   

    gudang_ku.tampilkan_daftar()

    print("----- Menyimpan barang setelah Tool Box Penutup Bawah -----")
    b_mid = Barang("1236", "Tool Box Penutup Atas", 950)
    gudang_ku.sisip_setelah("1235", b_mid)
    gudang_ku.tampilkan_daftar()

    print("----- Mencari barang -----")
    gudang_ku.cari_barang("1134")

    print("\n----- Mengeluarkan barang -----")
    gudang_ku.hapus_barang("1134")
    gudang_ku.tampilkan_daftar()