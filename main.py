import tkinter as tk
from datetime import datetime
import pyodbc

con = pyodbc.connect(Trusted_Connection='no',
                     driver='{SQL Server}',
                     server='192.168.15.32',
                     database='Operations',
                     UID='pladis_dba',
                     PWD='BigFlats')
cursor = con.cursor()


standard_font = ('Times New Roman', 13)
standard_main_loop_pady = 10
standard_main_loop_padx = 15
shift_options = ['1', '2', '3', '4']
specific_location_dictionary = {'Alpha Enrobing': ['Drum', 'Tempering Unit KGM', 'NBD', 'Belt Washer',
                                                   'Cooling Tunnel 1', 'Wire Belt Section', 'Enrober 1',
                                                   'Cooling Tunnel 2', 'Depositor', 'Enrober 2', 'Decorator Station',
                                                   'Cooling Tunnel 3', 'Tempering Unit 1', 'Tempering Unit 2',
                                                   'Sieve 1', 'Sieve 2', 'Mini tempering Unit', 'Day Tank', 'Tank 8/9',
                                                   'Kason Sieve'],
                                'Alpha Dry End': ['Evolution Date Coder', 'Metal Detector', 'Markem Printer',
                                                  'Shanklin', 'Conveyors', 'DDU1', 'DU1', 'South Handpack',
                                                  'North Handpack', 'Taper', 'Buffer'],
                                'North Hand Pack': [''],
                                'South Hand Pack': [''],
                                'Sig 1 Packaging': ['Buffer Discharge Belts', 'Profile Station', 'Metal Detector',
                                                    'Accumulator', 'Lug Chain', 'Card Feed', 'Film', 'Former', 'Knives',
                                                    'Markem Printer', 'Check Weigher', 'Vacuum',
                                                    'Exit Conveyor to TTM'],
                                'Sig 2 Packaging': ['Buffer Discharge Belts', 'Profile Station', 'Metal Detector',
                                                    'Accumulator', 'Lug Chain', 'Card Feed', 'Film', 'Former', 'Knives',
                                                    'Markem Printer', 'Check Weigher', 'Vacuum',
                                                    'Exit Conveyor to TTM'],
                                'TTM': ['Infeed', 'Product Grouping', 'Robot Pick', 'Carriages', 'Cardboard Feed',
                                        'Cardboard Robot', 'Box Former', 'Glue Station', 'Discharge',
                                        'Outfeed Conveyor', 'Taper', 'Evolution Date Coder', 'Markem Printer',
                                        'TTM Machine/Tool'],
                                'Bravo Enrobing': ['Pretzel Feeder', 'Drum', 'Tempering Unit KGM', 'NBD', 'Belt Washer',
                                                   'Cooling Tunnel 1', 'Wire Belt Section', 'Enrober 1',
                                                   'Cooling Tunnel 2', 'Depositor', 'Enrober 2', 'Decorator Station',
                                                   'Cooling Tunnel 3', 'Tempering Unit 1', 'Tempering Unit 2',
                                                   'Sieve 1', 'Sieve 2', 'Mini Tempering Unit', 'Day Tank', 'Tank 8/9'],
                                'Bravo Dry End': ['Evolution Date Coder', 'Metal Detector', 'Markem Printer',
                                                  'Shanklin', 'Conveyors', 'DDU1', 'Handpack', 'Buffer', 'Taper'],
                                'Bravo Hand Pack': [''],
                                'Bravo Sig/Sig 0': ['Profile Station', 'Metal Detector', 'Accumulator', 'Lug Chain',
                                                    'Card Feed', 'Film', 'Former', 'Knives', 'Markem Printer',
                                                    'Check Weigher', 'Vacuum'],
                                'Charlie Enrobing': ['Panners', 'Nut Infeed System', 'Nut return System', 'Depositor',
                                                     'Jet Tunnel', 'Conveyor', 'Enrober', 'Tempering unit', 'Day tank',
                                                     'Nut Return Incline', 'Wire Belt Section', 'Cooling Tunnel',
                                                     'Sieve'],
                                'Charlie Packaging': ['Conveyor', 'Metal Detector', 'Jar Feeder', 'Jar Sealer',
                                                      'Labeler', 'Markem Printer', 'Evolution Date Coder',
                                                      'Big Joe Lift'],
                                'Delta Enrobing': ['Pretzel Feeder', 'Gapping Belts', 'Enrober', 'Tempering Unit',
                                                   'Sieve', 'Day Tank', 'Stringer', 'Cooling Tunnel'],
                                'Delta Packaging': ['Conveyor', 'Metal Detector'],
                                'Echo Enrobing': ['Pretzel Feeder', 'Jet Tunnel', 'Depositor', 'Wire Belt Section',
                                                  'Enrober', 'Tempering Unit', 'Sieve', 'Day Tank', 'Cold Table',
                                                  'Cooling Tunnel'],
                                'Echo Packaging': ['Conveyor', 'Metal Detector'],
                                'SN Packaging': ['Fastback', 'Incline Elevator', 'Ishida Scale', 'Clamps/Duck Bills',
                                                 'Metal Detector', 'Film', 'Zipper', 'Hot Seal', 'Cold Seal',
                                                 'Hole Punch', 'Knives', 'Grippers', 'Conveyor', 'Markem Printer'],
                                'East Combi': ['Conveyors', 'Box Erector', 'Fill Station', 'Taper',
                                               'Evolution Date Coder'],
                                'West Combi': ['Conveyors', 'Box Erector', 'Fill Station', 'Taper',
                                               'Evolution Date Coder'],
                                'Thurling Packaging': ['Fastback', 'Incline Elevator', 'Ishida Scale',
                                                       'Thurlings Machine', 'Conveyor', 'Markem Printer', 'Taper',
                                                       'Evolution Date Coder', 'Check Weigher', 'Metal Detector'],
                                'Hayssen Packaging': ['Fastback', 'Incline Elevator', 'Ishida Scale', 'Hayssen Machine',
                                                      'Conveyor', 'Markem Printer', 'Taper', 'Evolution Date Coder',
                                                      'Metal Detector'],
                                'Kitchen': ['Scales', 'Milk Preparation', 'Contherm', 'Melt Tanks', 'Sucrofilm',
                                            'Day Tank', 'Autograv', 'Dynamic Mixer', 'Reclaim', 'Caraflex',
                                            'Heat/Steam Skid', 'Buffer Tank'],
                                'Facilities': ['RTU', 'Chillers', 'Cooling Tower', 'Boilers', 'Compressors',
                                               'Electrical/Light Bulbs', 'Generators', 'Public Water', 'Rest Rooms',
                                               'Offices', 'Break Room', 'COP Room', 'CIP Room', 'Hand Wash Room',
                                               'Air Handler', 'Plant Warehouse', 'Plant Doors', 'Fork Lifts',
                                               'Man Lifts', 'Miscellaneous Maintenance', 'Special Project Work',
                                               'Programming/Controls', 'Outdoor Maintenance', 'Compactors', 'Cooler',
                                               'R&D Lab', 'Old Kitchen', 'Cargo Elevator', 'Contractor',
                                               'Warehouse Storage', 'Truck Bay']
                                }
standard_bg = '#ffffff'


def specific_location_callback(*args):
    key_lookup = workstation_entry_var.get()
    if key_lookup == '':
        pass
    else:
        specific_area_entry = tk.OptionMenu(root, specific_area_entry_var, *specific_location_dictionary[key_lookup])
        specific_area_entry.config(font=standard_font)
        specific_area_entry.grid(row=4, column=1, padx=standard_main_loop_pady, pady=standard_main_loop_pady, sticky='E')


def retrieve_entries():
    user_date = date_entry_var.get()
    user_shift = shift_entry_var.get()
    user_workstation = workstation_entry_var.get()
    user_specific_area = specific_area_entry_var.get()
    user_minutes_spent = minutes_spent_var.get()
    user_comments = comments_message_entry.get("1.0", 'end-1c')
    instance_tuple = (user_date, user_shift, user_workstation, user_specific_area, user_minutes_spent, user_comments)
    cursor.execute('INSERT INTO [dbo].[Maintenance_EOS] VALUES ' + str(instance_tuple))
    con.commit()
    workstation_entry_var.set('')
    specific_area_entry_var.set('')
    minutes_spent_var.set(0)
    comments_message_entry.delete(1.0, "end")


root = tk.Tk()
root.title('Maintenance EOS')
root.configure(background=standard_bg)
img = tk.PhotoImage(file='Maintenance Background Image.png')
tk.Label(root, image=img).grid(row=0, column=0, columnspan=3, rowspan=8, padx=5, pady=5)
root.geometry('425x525')


welcome_title = tk.Label(text='Maintenance EOS', font=('Times New Roman', 25), justify='center', bg=standard_bg)
welcome_title.grid(column=0, row=0, columnspan=2, sticky='NSEW')
date_label = tk.Label(text='Date:', font=standard_font, justify='center', bg=standard_bg)
date_label.grid(column=0, row=1, sticky='W', padx=3, pady=standard_main_loop_pady)
shift_label = tk.Label(text='Shift:', font=standard_font, justify='center', bg=standard_bg)
shift_label.grid(column=0, row=2, sticky='W', padx=3, pady=standard_main_loop_pady)
workstation_label = tk.Label(text='Workstation', font=standard_font, justify='center', bg=standard_bg)
workstation_label.grid(column=0, row=3, sticky='W', padx=3, pady=standard_main_loop_pady)
specific_area_label = tk.Label(text='Specific Area', font=standard_font, justify='center', bg=standard_bg)
specific_area_label.grid(column=0, row=4, sticky='W', padx=3, pady=standard_main_loop_pady)
minutes_spent_label = tk.Label(text='Minutes Spent:', font=standard_font, justify='center', bg=standard_bg)
minutes_spent_label.grid(column=0, row=5, sticky='W', padx=3, pady=standard_main_loop_pady)
comments_label = tk.Label(text='Comments:', font=standard_font, justify='center', bg=standard_bg)
comments_label.grid(column=0, row=6, sticky='NW', padx=3, pady=standard_main_loop_pady)

date_entry_var = tk.StringVar()
date_entry_var.set(datetime.now().strftime('%m/%d/%Y %H:%M'))
date_entry = tk.Entry(root, textvariable=date_entry_var, font=standard_font, state='readonly', bd=2, justify='right')
date_entry.grid(row=1, column=1, padx=standard_main_loop_pady, pady=standard_main_loop_pady, sticky='E')
shift_entry_var = tk.StringVar()
shift_entry = tk.OptionMenu(root, shift_entry_var, *shift_options)
shift_entry.config(font=standard_font)
shift_entry.grid(row=2, column=1, padx=standard_main_loop_pady, pady=standard_main_loop_pady, sticky='E')
workstation_entry_var = tk.StringVar()
workstation_entry = tk.OptionMenu(root, workstation_entry_var, *specific_location_dictionary.keys())
workstation_entry.config(font=standard_font)
workstation_entry.grid(row=3, column=1, padx=standard_main_loop_pady, pady=standard_main_loop_pady, sticky='E')
workstation_entry_var.trace('w', specific_location_callback)
specific_area_entry_var = tk.StringVar()
specific_area_entry = tk.OptionMenu(root, specific_area_entry_var, *specific_location_dictionary['Facilities'])
specific_area_entry.config(font=standard_font)
specific_area_entry.grid(row=4, column=1, padx=standard_main_loop_pady, pady=standard_main_loop_pady, sticky='E')
minutes_spent_var = tk.IntVar()
minutes_spent_entry = tk.Entry(root, textvariable=minutes_spent_var, font=standard_font, bd=2, justify='right', width=5)
minutes_spent_entry.grid(row=5, column=1, padx=standard_main_loop_pady, pady=standard_main_loop_pady, sticky='E')
comments_message_entry = tk.Text(root, height=11, width=20, font=('Times New Roman', 11), bd=2, wrap='word')
comments_message_entry.grid(row=6, column=1, rowspan=3, padx=standard_main_loop_pady, pady=standard_main_loop_pady,
                            sticky='SE')

submit_button = tk.Button(root, text='Submit', command=retrieve_entries, pady=standard_main_loop_pady,
                          font=('Times New Roman', 15))
submit_button.grid(row=7, column=0)

root.mainloop()
