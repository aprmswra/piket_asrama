from datetime import datetime
import ast 
import json 

class Base_Structure:
    def __init__(self, name, status = "Active"):
        self.name = name
        self.comserv_type = {
            "kamar mandi": [0] * 52,
            "dapur": [0] * 52,
            "gita": [0] * 52,
            "banten": [0] * 52
        }
        self.status = status

    #fungsi base status
    def activate(self):
        self.status = "Active"

    #fungsi base status
    def deactivate(self):
        self.status = "Inactive"

    #getter & setter
    def get_comserv_type(self):
        print(self.comserv_type.keys())
    
    def get_name(self):
        print(self.name)
    
    def set_name(self, new_name):
        self.name = new_name

    #lihat status secara keseluruhan
    def get_status(self):
        return f"name: {self.name}, status: {self.status}, comserv_type: {self.comserv_type}"

    #lakukan absen-(method base)
    def comserv_absence_base(self, comserv_type, minggu_ke, status):
        if status == 1 or status == 0:
            if comserv_type in self.comserv_type:
                self.comserv_type[comserv_type][minggu_ke - 1] = status
                print(f"Absensi {self.name} berhasil di-update")
            else:
                print("piket tidak ditemukan")
        else:
            print("status harus dalam bentuk binary")
    
    #menghitung kapan terakhir seseorang piket (berdasarkan jenis piket)-(fungsi base)
    def last_piket_week(person, comserv_type):
    # Mengambil daftar piket untuk tipe comserv tertentu dari orang tersebut
        piket_list = person.comserv_type[comserv_type]
        
        # Menemukan minggu terakhir orang tersebut melakukan piket (menggunakan enumerate untuk mendapatkan indeks len pada list, yang mewakili minggu)
        last_week = None
        for week, status in reversed(list(enumerate(piket_list))):
            if status == 1:
                last_week = week
                break
        return last_week

class Structure_Manager():
    def __init__(self):
        self.comserv_type_dict = {}  

    #tambahkan orang
    def add_person(self, name):
        person = Base_Structure(name)
        self.comserv_type_dict[name] = person  

    #hapus orang
    def delete_person(self, name):
        if name in self.comserv_type_dict:
            del self.comserv_type_dict[name] 

    #tambahkan jenis piket (jika diperlukan)
    def add_comserv_type(self, new_comserv):
        for name, person in self.comserv_type_dict.items():
            if new_comserv not in person.comserv_type:
                person.comserv_type[new_comserv] = [0] * 52
    
    #hapus jenis piket (jika diperlukan)
    def delete_comserv_type(self, delete_comserv):
        for name, person in self.comserv_type_dict.items():
            if delete_comserv in person.comserv_type:
                del person.comserv_type[delete_comserv]

    #melihat status, jika mau satu atau seluruhnya
    def get_status(self, name=None):
        if name:
            if name in self.comserv_type_dict:
                person = self.comserv_type_dict[name]
                print(f"name: {person.name}, status: {person.status}, comserv_type: {person.comserv_type}")
            elif name not in self.comserv_type_dict:
                print(f"Nama tidak ditemukan")
        else:
            for name, person in self.comserv_type_dict.items():
                print(f"name: {person.name}, status: {person.status}, comserv_type: {person.comserv_type}")

    #lakukan absensi, manager sangat berhubungan comserv_absence_base
    def comserv_absence_manager(self, name, comserv_type, minggu_ke, status):
        if name in self.comserv_type_dict:
            person = self.comserv_type_dict[name]
            print(f"Memperbarui absensi untuk {person.name}:")
            person.comserv_absence_base(comserv_type, minggu_ke+1, status)
        else:
            print(f"Tidak ada orang dengan nama {name}")

    #save data ke .json
    def save(self, filename):
        with open(filename, 'w') as f:
            for name, person in self.comserv_type_dict.items():
                serialized_person = {"name": person.name, "status": person.status, "comserv_type": person.comserv_type}
                f.write(json.dumps(serialized_person) + '\n')

    #load data dari .json
    def load(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                serialized_person = json.loads(line.strip())
                name = serialized_person['name']
                person = Base_Structure(name)
                person.comserv_type = serialized_person['comserv_type']
                person.status = serialized_person['status']
                self.comserv_type_dict[name] = person

    #lakukan aktivasi dari class manajemen
    def activate_person(self, name):
        if name in self.comserv_type_dict:
            person = self.comserv_type_dict[name]
            person.activate()
            print(f"{name} telah diaktifkan.")
        else:
            print(f"Tidak ada orang dengan nama {name}")

    #lakukan deaktivasi dari class manajemen
    def deactivate_person(self, name):
        if name in self.comserv_type_dict:
            person = self.comserv_type_dict[name]
            person.deactivate()
            print(f"{name} telah dinonaktifkan.")
        else:
            print(f"Tidak ada orang dengan nama {name}")  

