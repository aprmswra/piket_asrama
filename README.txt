File ini digunakan untuk memberikan tata cara penggunaan method pada aplikasi sederhana piket asrama

# see calender and it's week
print_calendar_with_week_numbers(2023, specific_month=9)

# load data
## Membuat instance dari ManajemenPiket
manajemen = Structure_Manager()
manajemen.load("data_piket.json")

# menambahkan orang
manajemen = Structure_Manager()
manajemen.add_person(name)

# deactive active status seseorang
manajemen = Structure_Manager()
manajemen.deactivate_person("Arbi")
manajemen.activate_person("Arbi")

# melihat status
## melihat status satu orang
manajemen = Structure_Manager()
manajemen.get_status(name = "Arbi")

## melihat status semua
manajemen = Structure_Manager()
manajemen.get_status()

# generate piket
manajemen = Structure_Manager()
manajemen.load("data_piket.json")
scheduler = PiketScheduler(manajemen)
schedule = scheduler.generate()
print(schedule)

# melakukan absen
manajemen = Structure_Manager()
manajemen.load("data_piket.json")
manajemen.comserv_absence_manager("Arbi", "dapur", 35,1)

# save data
manajemen = Structure_Manager()
manajemen.save("data_piket.json")

# menambahkan jenis piket
manajemen = Structure_Manager()
manajemen.add_comserv_type("Ngasi makan boy")
manajemen.save("data_piket.json")

# menghapus jenis piket
manajemen = Structure_Manager()
manajemen.delete_comserv_type("Ngasi makan boy")
manajemen.save("data_piket.json")



