from structure import Structure_Manager, Base_Structure
from generator import PiketScheduler
from calendar_view import print_calendar_with_week_numbers

# list_name = ["Andre", "Agus", "Arya", "Arbi", "Bayu", "Bobo", "Dwi", "Enricho", 
#              "Lingga", "Mira", "Nanda", "Odit", "Pini", "Tri", "Zenna", "Wirgun"]

# list_piket = ["kamar mandi", "dapur", "gita", "banten"]


## lihat tanggal 
# print_calendar_with_week_numbers(2023 , 9)

#load data
manajemen = Structure_Manager()
manajemen.load("data_piket.json")

# Aktivasi dan deaktivasi
manajemen.deactivate_person("Wirgun")

# absen
manajemen.comserv_absence_manager("Zenna", "dapur", 36,1)
manajemen.comserv_absence_manager("Odit", "dapur", 36,1)
manajemen.comserv_absence_manager("Andre", "kamar mandi", 36,1)
manajemen.comserv_absence_manager("Nanda", "dapur", 36,1)
manajemen.comserv_absence_manager("Agus", "gita", 36,1)
manajemen.comserv_absence_manager("Agus", "banten", 36,1)
manajemen.comserv_absence_manager("Tri", "banten", 36,1)
manajemen.save("data_piket.json")

# manajemen = Structure_Manager()
# manajemen.load("data_piket.json")
# manajemen.activate_person("Arbi")
# manajemen.comserv_absence_manager("Arbi", "dapur", 34,0)
# manajemen.save("data_piket.json")
# manajemen.get_status(name = "Arbi")

# # manajemen.get_status("Wirgun")