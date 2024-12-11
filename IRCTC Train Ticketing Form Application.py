# from tkinter import *
# import tkinter as tk
# from tkcalendar import DateEntry
# from tkinter import ttk
# import mysql.connector 
# from tkinter import messagebox




# # Function to submit form data to the database
# def submit():
#     try:
#         TRAIN_NO = entry_train_no.get()
#         TICKET_NO = entry_ticket_no.get()
#         JOURNEY_DATE = entry_journey_date.get_date().strftime("%Y-%m-%d")
#         CLASS = cb_class.get()
#         FROM_STATION = cb_from_station.get()
#         TO_STATION = cb_to_station.get()
#         BOARDING_STATION = cb_boarding_station.get()
#         QUOTA = cb_quota.get()
#         CUST_NAME = entry_cust_name.get()
#         AGE = entry_age.get()
#         CONTACT_NO = entry_contact_no.get()
#         GENDER = cb_gender.get()
#         ADDRESS = entry_address.get()
#         STATE = entry_state.get()
#         ARRIVING_TIME = entry_arriving_time.get()
#         BERTH = cb_berth.get()
#         CANCELLATION_POLICY = entry_cancellation_policy.get()
#         IRCTC_ACCIDENT_INSURANCE = "Yes" if var_accident_insurance.get() == 0 else "No"
#         IRCTC_USER_ID = "Yes" if var_user_id.get() == 0 else "No"
#         PAY_AMOUNT = entry_pay_amount.get()

#         # Check if any field is empty
#         if not all([TRAIN_NO, TICKET_NO, JOURNEY_DATE, CLASS, FROM_STATION, TO_STATION, BOARDING_STATION, QUOTA, CUST_NAME, AGE, CONTACT_NO, GENDER, ADDRESS, STATE, ARRIVING_TIME, BERTH, CANCELLATION_POLICY, PAY_AMOUNT]):
#             messagebox.showerror('Error', "All fields are mandatory")
#             return
#          # Display data in textarea
#         textarea.insert(END, f"TRAIN NO: \t\t\t\t{TRAIN_NO}\n")
#         textarea.insert(END, f"TICKET NO: \t\t\t\t{TICKET_NO}\n")
#         textarea.insert(END, f"JOURNEY DATE: \t\t\t\t {JOURNEY_DATE}\n")
#         textarea.insert(END, f"CLASS: \t\t\t\t{CLASS}\n")
#         textarea.insert(END, f"FROM STATION: \t\t\t\t{FROM_STATION}\n")
#         textarea.insert(END, f"TO STATION: \t\t\t\t{TO_STATION}\n")
#         textarea.insert(END, f"BOARDING STATION: \t\t\t\t{BOARDING_STATION}\n")
#         textarea.insert(END, f"QUOTA: \t\t\t\t{QUOTA}\n")
#         textarea.insert(END, f"CUST NAME: \t\t\t\t{CUST_NAME}\n")
#         textarea.insert(END, f"AGE: \t\t\t\t{AGE}\n")
#         textarea.insert(END, f"CONTACT NO: \t\t\t\t{CONTACT_NO}\n")
#         textarea.insert(END, f"GENDER: \t\t\t\t{GENDER}\n")
#         textarea.insert(END, f"ADDRESS: \t\t\t\t{ADDRESS}\n")
#         textarea.insert(END, f"STATE: \t\t\t\t{STATE}\n")
#         textarea.insert(END, f"ARRIVING TIME: \t\t\t\t{ARRIVING_TIME}\n")
#         textarea.insert(END, f"BERTH: \t\t\t\t{BERTH}\n")
#         textarea.insert(END, f"CANCELLATION POLICY: \t\t\t\t{CANCELLATION_POLICY}\n")
#         textarea.insert(END, f"IRCTC ACCIDENT INSURANCE: \t\t\t\t{IRCTC_ACCIDENT_INSURANCE}\n")
#         textarea.insert(END, f"IRCTC USER ID: \t\t\t\t{IRCTC_USER_ID}\n")
#         textarea.insert(END, f"PAY AMOUNT: \t\t\t\t{PAY_AMOUNT}\n")
#         textarea.insert(END, "-"*50 + "\n")
#         # Insert data into the database
#         add_data(TRAIN_NO, TICKET_NO, JOURNEY_DATE, CLASS, FROM_STATION, TO_STATION, BOARDING_STATION, QUOTA, CUST_NAME, AGE, CONTACT_NO, GENDER, ADDRESS, STATE, ARRIVING_TIME, BERTH, CANCELLATION_POLICY, IRCTC_ACCIDENT_INSURANCE, IRCTC_USER_ID, PAY_AMOUNT)
        
#         messagebox.showinfo('Success', "Data submitted successfully!")
#     except Exception as e:
#         messagebox.showerror('Error', str(e))

# # Function to create the database
# def create_database():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="vinit1234"
#     )
#     cursor = conn.cursor()
#     cursor.execute("CREATE DATABASE IF NOT EXISTS INDIA_IRCTC")
#     conn.close()

# # Function to create the table

# def create_table():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="vinit1234",
#         database="INDIA_IRCTC"
#     )
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS BHARAT_RAILWAY (
#         TICKET_NO INT AUTO_INCREMENT PRIMARY KEY,
#         TRAIN_NO VARCHAR(50),
#         JOURNEY_DATE DATE,
#         CLASS VARCHAR(20),
#         FROM_STATION VARCHAR(60),
#         TO_STATION VARCHAR(60),
#         BOARDING_STATION VARCHAR(50),
#         QUOTA VARCHAR(50),
#         CUST_NAME VARCHAR(60),
#         AGE INT,
#         CONTACT_NO BIGINT,
#         GENDER VARCHAR(50),
#         ADDRESS VARCHAR(120),
#         STATE VARCHAR(50),
#         ARRIVING_TIME VARCHAR(50),
#         BERTH VARCHAR(50),
#         CANCELLATION_POLICY VARCHAR(50),
#         IRCTC_ACCIDENT_INSURANCE VARCHAR(50),
#         IRCTC_USER_ID VARCHAR(60),
#         PAY_AMOUNT BIGINT
#     )''')
#     conn.commit()
#     conn.close()

# # Function to add data to the table
# def add_data(TRAIN_NO, TICKET_NO, JOURNEY_DATE, CLASS, FROM_STATION, TO_STATION, BOARDING_STATION, QUOTA, CUST_NAME, AGE, CONTACT_NO, GENDER, ADDRESS, STATE, ARRIVING_TIME, BERTH, CANCELLATION_POLICY, IRCTC_ACCIDENT_INSURANCE, IRCTC_USER_ID, PAY_AMOUNT):
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="vinit1234",
#         database="INDIA_IRCTC"
#     )
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO BHARAT_RAILWAY (TRAIN_NO, TICKET_NO, JOURNEY_DATE, CLASS, FROM_STATION, TO_STATION, BOARDING_STATION, QUOTA, CUST_NAME, AGE, CONTACT_NO, GENDER, ADDRESS, STATE, ARRIVING_TIME, BERTH, CANCELLATION_POLICY, IRCTC_ACCIDENT_INSURANCE, IRCTC_USER_ID, PAY_AMOUNT) 
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
#     (TRAIN_NO, TICKET_NO, JOURNEY_DATE, CLASS, FROM_STATION, TO_STATION, BOARDING_STATION, QUOTA, CUST_NAME, AGE, CONTACT_NO, GENDER, ADDRESS, STATE, ARRIVING_TIME, BERTH, CANCELLATION_POLICY, IRCTC_ACCIDENT_INSURANCE, IRCTC_USER_ID, PAY_AMOUNT))
#     conn.commit()
#     conn.close()

# # GUI setup
# root = tk.Tk()
# root.title("IRCTC TICKET FORM")
# # root.iconbitmap("SubwayTrain_Green_icon-icons.com_54890.ico")
# root.geometry("1200x1200")

# lb = tk.LabelFrame(root, width=1520, height=50, bg="#1E3D81").place(x=10, y=5)
# l1 = tk.Label(lb, text="I      R      C      T      C", font=("arial 20 bold"), width=33, bg="#829BCB").place(x=500, y=10)

# lb1 = tk.LabelFrame(root, width=1460, height=23, bg="#006CB1").place(x=40, y=70)
# l2 = tk.Label(root, text="Journey details", font=("arial 10 bold")).place(x=42.4, y=70)

# l3 = tk.Label(root, text="Train no  :", font=("arial 10 bold")).place(x=60, y=115)
# entry_train_no = tk.Entry(root)
# entry_train_no.place(x=165, y=115)

# l4 = tk.Label(root, text="Ticket no  :", font=("arial 10 bold")).place(x=445, y=115)
# entry_ticket_no = tk.Entry(root)
# entry_ticket_no.place(x=545, y=119)

# l5 = tk.Label(root, text="Journey date :", font=("arial 10 bold")).place(x=858, y=115)
# entry_journey_date = DateEntry(root, width=17)
# entry_journey_date.place(x=966, y=117)

# l6 = tk.Label(root, text="Class  :", font=("arial 10 bold")).place(x=1282, y=115)

# cb_class = StringVar()
# cb_class = ttk.Combobox(root, width=17, text=cb_class, state="readonly")
# cb_class["values"] = ("AC FIRST TIER", "AC SECOND TIER", "3E", "SLEEPER", "GENERAL")
# cb_class.place(x=1342, y=116)
# cb_class.current(0)

# l7 = tk.Label(root, text="From station  :", font=("arial 10 bold")).place(x=60, y=200)

# cb_from_station = StringVar()
# cb_from_station = ttk.Combobox(root, width=17, text=cb_from_station, state="readonly")
# cb_from_station["values"] = ("AMBALA CANTT", "DELHI", "CHANDIGARH", "YAMUNANAGAR", "KATRA")
# cb_from_station.place(x=165, y=200)
# cb_from_station.current(3)

# l8 = tk.Label(root, text="To station  :", font=("arial 10 bold")).place(x=448, y=200)

# cb_to_station = StringVar()
# cb_to_station = ttk.Combobox(root, width=17, text=cb_to_station, state="readonly")
# cb_to_station["values"] = ("MUMBAI", "AMBALA CANTT", "NOIDA", "DELHI", "GURUGRAM", "CHANDIGARH", "YAMUNANAGAR", "KATRA")
# cb_to_station.place(x=546, y=200)
# cb_to_station.current(2)

# l9 = tk.Label(root, text="Boarding Sta :", font=("arial 10 bold")).place(x=858, y=200)
# cb_boarding_station = StringVar()
# cb_boarding_station = ttk.Combobox(root, width=17, text=cb_boarding_station, state="readonly")
# cb_boarding_station["values"] = ("MUMBAI", "AMBALA CANTT", "NOIDA", "DELHI", "GURUGRAM", "CHANDIGARH", "YAMUNANAGAR", "KATRA")
# cb_boarding_station.place(x=966, y=200)
# cb_boarding_station.current(3)

# l10 = tk.Label(root, text="Quota  :", font=("arial 10 bold")).place(x=1282, y=200)

# cb_quota = StringVar()
# cb_quota = ttk.Combobox(root, width=17, text=cb_quota, state="readonly")
# cb_quota["values"] = ("TATKAL", "GENERAL", "SENIOR CITIZEN")
# cb_quota.place(x=1342, y=200)
# cb_quota.current(1)

# lb2 = tk.LabelFrame(root, width=1460, height=23, bg="#006CB1").place(x=40, y=250)
# l11 = tk.Label(root, text="Passenger Details", font=("arial 10 bold")).place(x=42.4, y=250)

# l12 = tk.Label(root, text="Cust_Name  :", font=("arial 10 bold")).place(x=60, y=300)
# entry_cust_name = tk.Entry(root)
# entry_cust_name.place(x=165, y=300)

# l13 = tk.Label(root, text="Age  :", font=("arial 10 bold")).place(x=445, y=300)
# entry_age = tk.Entry(root)
# entry_age.place(x=545, y=300)

# l14 = tk.Label(root, text="Contact no :", font=("arial 10 bold")).place(x=858, y=300)
# entry_contact_no = tk.Entry(root)
# entry_contact_no.place(x=966, y=300)

# l15 = tk.Label(root, text="Gender :", font=("arial 10 bold")).place(x=1280, y=300)

# cb_gender = StringVar()
# cb_gender = ttk.Combobox(root, width=17, text=cb_gender, state="readonly")
# cb_gender["values"] = ("Male", "Female", "Transgender")
# cb_gender.place(x=1344, y=300)
# cb_gender.current(0)

# l16 = tk.Label(root, text="Address  :", font=("arial 10 bold")).place(x=60, y=360)
# entry_address = tk.Entry(root)
# entry_address.place(x=165, y=360)

# l17 = tk.Label(root, text="State  :", font=("arial 10 bold")).place(x=445, y=360)
# entry_state = tk.Entry(root)
# entry_state.place(x=545, y=360)

# l18 = tk.Label(root, text="Arriving Time :", font=("arial 10 bold")).place(x=858, y=360)
# entry_arriving_time = tk.Entry(root)
# entry_arriving_time.place(x=966, y=366)

# l18 = tk.Label(root, text="Berth  :", font=("arial 10 bold")).place(x=1280, y=360)

# cb_berth = StringVar()
# cb_berth = ttk.Combobox(root, width=17, text=cb_berth, state="readonly")
# cb_berth["values"] = ("UPPER BERTH", "MIDDEL BERTH", "LOWER BERTH", "WINDOW BERTH")
# cb_berth.place(x=1340, y=360)
# cb_berth.current(0)

# lb3 = tk.LabelFrame(root, width=1460, height=23, bg="#006CB1").place(x=40, y=405)
# l19 = tk.Label(root, text="  Billing   Detail  ", font=("arial 10 bold")).place(x=42.4, y=405)

# l20 = tk.Label(root, text="IRCTC user id  :", font=("arial 10 bold")).place(x=60, y=605)
# entry_cancellation_policy = tk.Entry(root)
# entry_cancellation_policy.place(x=260, y=607)

# l21 = tk.Label(root, text="IRCTC accident insurance :", font=("arial 10 bold")).place(x=60, y=530)
# l22 = tk.Label(root, text="0.45/person", font=("arial 10 bold")).place(x=60, y=552)
# var_accident_insurance = IntVar()
# RB = tk.Radiobutton(root, text="Yes", font=("arial 10 bold"), value=0, variable=var_accident_insurance)
# RB1 = tk.Radiobutton(root, text="No", font=("arial 10 bold"), value=1, variable=var_accident_insurance)
# RB.place(x=250, y=530)
# RB1.place(x=342, y=530)

# l20 = tk.Label(root, text="Cancellation POlicy  :", font=("arial 10 bold")).place(x=60, y=455)
# var_user_id = IntVar()
# RB2 = tk.Radiobutton(root, text="Yes", font=("arial 10 bold"), value=0, variable=var_user_id)
# RB3 = tk.Radiobutton(root, text="No", font=("arial 10 bold"), value=1, variable=var_user_id)
# RB2.place(x=250, y=455)
# RB3.place(x=342, y=455)

# l23 = tk.Label(root, text="Pay amount  :", font=("arial 11 bold")).place(x=60, y=690)
# entry_pay_amount = tk.Entry(root)
# entry_pay_amount.place(x=257, y=690)


# textarea_frame = Frame(root)
# textarea_frame.place(x=450, y=440)

# ticket_detail = tk.Label(root, text = "TICKET PRINT :", font="arial 10 bold", bg="#829BCB",fg="Black")
# ticket_detail.place(x=900, y=445 )


# scrollbar = Scrollbar(textarea_frame, orient="vertical")
# textarea = Text(textarea_frame, bg="#829BCB",fg="#F0F0F0", width=130, height=20, yscrollcommand=scrollbar.set)

# scrollbar.pack(side=RIGHT, fill=Y)
# textarea.pack(side=LEFT, fill=BOTH, expand=True)
# scrollbar.config(command=textarea.yview)

# l24 = tk.Button(root, text="Submit", font=("arial 11 bold"), bg="#9AA5D4", width=14, height=1, command=submit)
# l24.place(x=250, y=740)

# # Create the database and table
# create_database()
# create_table()

# root.mainloop()
