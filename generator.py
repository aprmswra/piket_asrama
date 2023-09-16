from structure import Structure_Manager, Base_Structure

class PiketScheduler:
    def __init__(self, manager):
        self.manager = manager

    #lakukan generate berdasarkan value default seperti parameter dibawah
    def generate(self, week = 1, n_mandi = 2, n_dapur = 2, n_gita = 1, n_banten = 2):
        print(f"Jadwal piket dapur minggu ke-{week}")
        # Inisialisasi jadwal
        schedule = {
            "kamar mandi": [],
            "dapur": [],
            "gita": [],
            "banten": []
        }

        #Lakukan seleksi nama, jika deactive tidak masuk hitungan
        active_names = []

        #pisahkan item dan person
        for name, person in self.manager.comserv_type_dict.items():

            #ambil yang memiliki status aktif saja
            if person.status == "Active":
                active_names.append(name)
            
        available_names = active_names.copy()

        #Kamar Mandi
        for _ in range(n_mandi):
            # Menghitung minggu terakhir setiap orang melakukan piket kamar mandi
            last_weeks = {name: self.manager.comserv_type_dict[name].last_piket_week("kamar mandi") for name in available_names}

            # Mengurutkan berdasarkan minggu terakhir (None diprioritaskan)
            sorted_names = sorted(available_names, key=lambda x: (last_weeks[x] is None, last_weeks[x]), reverse=True)

            # Memilih orang yang memiliki minggu paling jauh
            person = sorted_names[0]

            #masukan ke dalam list
            schedule["kamar mandi"].append(person)

            #remove sehingga tidak ada yang double.
            available_names.remove(person) 

        #Dapur
        for _ in range(n_dapur):
            last_weeks = {name: self.manager.comserv_type_dict[name].last_piket_week("dapur") for name in available_names}
            sorted_names = sorted(available_names, key=lambda x: (last_weeks[x] is None, last_weeks[x]), reverse=True)
            person = sorted_names[0]
            schedule["dapur"].append(person)
            available_names.remove(person) 

        #Gita
        for _ in range(n_gita):
            last_weeks = {name: self.manager.comserv_type_dict[name].last_piket_week("gita") for name in available_names}
            sorted_names = sorted(available_names, key=lambda x: (last_weeks[x] is None, last_weeks[x]), reverse=True)
            person = sorted_names[0]
            schedule["gita"].append(person)
            available_names.remove(person) 

        #Banten
        for _ in range(n_banten):
            last_weeks = {name: self.manager.comserv_type_dict[name].last_piket_week("banten") for name in available_names}
            sorted_names = sorted(available_names, key=lambda x: (last_weeks[x] is None, last_weeks[x]), reverse=True)
            person = sorted_names[0]
            schedule["banten"].append(person)
            available_names.remove(person) 

        return schedule