import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
from PIL import Image, ImageTk

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#importing database file
import medimanager_data as db
db.initDBConnection()

    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

BG_COLOR = 'white'  # Define background color

beds = {
    "Single Bed": 15,
    "Twin Sharing": 5,
    "Dormitory": 2 * 8,  # 2 dormitories with 8 beds each
    "ICU": 3
}

bed_bookings = []  # List to store bookings


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class LoginWindow:
    def _init_(self, root):
        self.root = root
        self.root.title("Login")

        # Set a fixed size for the window
        self.root.geometry("800x500")

        # Make window non-resizable
        self.root.resizable(width=False, height=False)

        # Set window icon 
        self.root.iconbitmap(r'C:\Users\debi2\OneDrive\Desktop\hsm_new\icon.ico')

        # Load the background image
        self.bg_image = Image.open(r'C:\Users\debi2\OneDrive\Desktop\hsm_new\doctor.jpg')
        self.bg_image = self.bg_image.resize((800, 500), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        # Create a Canvas widget
        self.canvas = tk.Canvas(self.root, width=800, height=500)
        self.canvas.pack(fill='both', expand=True)

        # Set the background image on the canvas
        self.canvas.create_image(0, 0, image=self.bg_image, anchor='nw')

        # Add welcome label
        welcome_label = tk.Label(self.root, text="Welcome to the MediManager", font=("Arial", 24), bg="#CDDDF3")
        welcome_label.place(x=200, y=50)

        self.frame = tk.Frame(self.root, bg="#CDDDF3")
        self.frame.place(x=220, y=150, width=360, height=200)

        # Function to increase font size and center align labels
        label_style = {'font': ('Times New Roman', 15), 'foreground': 'black'}

        tk.Label(self.frame, text="Username:", **label_style, bg="white").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.username_entry = tk.Entry(self.frame, font=('Arial', 15))
        self.username_entry.grid(row=0, column=1, padx=15, pady=15, sticky='w')

        tk.Label(self.frame, text="Password:", **label_style, bg="white").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.password_entry = tk.Entry(self.frame, show="*", font=('Arial', 15))
        self.password_entry.grid(row=1, column=1, padx=15, pady=15, sticky='w')

        self.login_button = tk.Button(self.frame, text="Login", command=self.login, font=('Arial', 12))
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def set_full_size(self):
        pass

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Hardcoded username and password for simplicity.
        if username == "admin" and password == "password":
            self.root.destroy()  # Close the login window
            open_dashboard()  # Open the dashboard window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            
def open_dashboard():
    root = tk.Tk()
    dashboard = Dashboard(root)
    root.mainloop()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
class Dashboard:
    def _init_(self, root):
        self.root = root
        self.root.title("Dashboard")

        # Set window icon 
        self.root.iconbitmap(r'C:\Users\debi2\OneDrive\Desktop\hsm_new\icon.ico')

        # Set window to full size
        self.set_full_size()

        # Load the background image
        self.bg_image = Image.open(r'C:\Users\debi2\OneDrive\Desktop\hsm_new\hospital.jpg')
        self.bg_image = self.bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        # Create a Canvas widget
        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.pack(fill='both', expand=True)

        # Set the background image on the canvas
        self.canvas.create_image(0, 0, image=self.bg_image, anchor='nw')

        # Configure the grid columns
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)

        # Panel frame for buttons
        self.panel_frame = tk.Frame(self.canvas, bg="#C5C8CC")
        self.panel_window = self.canvas.create_window(0, 0, window=self.panel_frame, anchor='nw')

        # Dashboard button
        self.dashboard_button = tk.Button(self.panel_frame, text="Dashboard", command=self.show_dashboard, font=("Helvetica", 15), fg="black")
        self.dashboard_button.pack(fill=tk.X, padx=15, pady=(10, 5))

        # Doctor button
        self.doctor_button = tk.Button(self.panel_frame, text="Doctor", command=self.open_doctor, font=("Helvetica", 15), fg="black")
        self.doctor_button.pack(fill=tk.X, padx=15, pady=(10, 5))

        # Patient button
        self.patient_button = tk.Button(self.panel_frame, text="Patient", command=self.open_patient, font=("Helvetica", 15), fg="black")
        self.patient_button.pack(fill=tk.X, padx=15, pady=(10, 5))

        # Bed button
        self.bed_button = tk.Button(self.panel_frame, text="Bed", command=self.open_bed, font=("Helvetica", 15), fg="black")
        self.bed_button.pack(fill=tk.X, padx=15, pady=(10, 5))

        # Billing button
        self.billing_button = tk.Button(self.panel_frame, text="Billing", command=self.open_billing, font=("Helvetica", 15), fg="black")
        self.billing_button.pack(fill=tk.X, padx=15, pady=(10, 5))

        # Main frame for text area or main content
        self.main_frame = tk.Frame(self.canvas, bg="#C5C8CC")
        self.main_window = self.canvas.create_window(self.root.winfo_screenwidth()//4, 0, window=self.main_frame, anchor='nw')

        # Show dashboard initially
        self.show_dashboard()

    def set_full_size(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")

    def show_dashboard(self):
        # Clear existing widgets in main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Display dashboard label
        dashboard_label = tk.Label(self.main_frame, text="Welcome to MediManager", font=("Arial", 24), fg="#0A0657")
        dashboard_label.pack(pady=20)

        # Add space between dashboard_label and about_us content
        space_label = tk.Label(self.main_frame, text="Navigating Health, Guiding Wellness: Your Trusted System",font=("Arial", 12, "italic"))
        space_label.pack()


        # About Us content
        about_label = tk.Label(self.main_frame, text="About Us", font=("Helvetica", 20), fg="#0A0657")
        about_label.pack(pady=(40, 20))

        about_text = """
        MediManager is a comprehensive hospital management system designed 
        to streamline patient, doctor, bed, and billing management processes. 
        Our mission is to provide efficient and effective tools for healthcare 
        institutions to improve patient care and operational efficiency.

        Features:
        - Manage patient records securely
        - Schedule and manage doctor appointments
        - Allocate and manage hospital beds efficiently
        - Handle billing and insurance claims seamlessly

        We strive to innovate and integrate the latest technologies to meet 
        the evolving needs of healthcare providers, ensuring better patient outcomes 
        and operational excellence.
        """
        about_content = tk.Label(self.main_frame, text=about_text, justify=tk.LEFT, font=("Times New Roman", 18), fg="black")
        about_content.pack(padx=20, pady=(0, 20))


    def open_doctor(self):
        self.root.withdraw()  # Hide the dashboard window
        root = tk.Tk()
        doctor_management = DoctorManagement(root, self.root)
        root.mainloop()

    def open_patient(self):
        self.root.withdraw()  # Hide the dashboard window
        root = tk.Tk()
        patient_management = PatientManagement(root, self.root)
        root.mainloop()

    def open_bed(self):
        self.root.withdraw()  # Hide the dashboard window
        root = tk.Tk()
        bed_management = BedManagement(root, self.root)
        root.mainloop()

    def open_billing(self):
        self.root.withdraw()  # Hide the dashboard window
        root = tk.Tk()
        billing_management = BillingManagement(root, self.root)
        root.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class DoctorManagement:
    def _init_(self, root, parent):
        self.root = root
        self.parent = parent
        self.root.title("Doctor Management System")
        self.root.configure(background='#C3E7F3')

        # Set window icon 
        self.root.iconbitmap(r'C:\Users\debi2\OneDrive\Desktop\hsm_new\icon.ico')

        # Set window to full size
        self.set_full_size()

        welcome_label = tk.Label(self.root, text="Welcome to the MediManager", font=("Arial", 24))
        welcome_label.pack(pady=20)

        # Font configuration
        self.default_font = ("Times New Roman", 15)  # Default font family and size

        self.add_doctor_frame = tk.Frame(root, background='#C3E7F3')
        self.add_doctor_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(self.add_doctor_frame, text="Doctor Name:", font=self.default_font, background='#C3E7F3').grid(row=0, column=0, padx=5, pady=5)
        self.doctor_name_entry = tk.Entry(self.add_doctor_frame, font=self.default_font)
        self.doctor_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.add_doctor_frame, text="Specialization:", font=self.default_font, background='#C3E7F3').grid(row=1, column=0, padx=5, pady=5)
        self.specialization_entry = tk.Entry(self.add_doctor_frame, font=self.default_font)
        self.specialization_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.add_doctor_frame, text="Mobile:", font=self.default_font, background='#C3E7F3').grid(row=2, column=0, padx=5, pady=5)
        self.mobile_entry = tk.Entry(self.add_doctor_frame, font=self.default_font)
        self.mobile_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.add_doctor_frame, text="Email:", font=self.default_font, background='#C3E7F3').grid(row=3, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.add_doctor_frame, font=self.default_font)
        self.email_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_doctor_button = tk.Button(self.add_doctor_frame, text="Add Doctor", font=self.default_font, command=self.add_doctor, width=20)
        self.add_doctor_button.grid(row=4, column=0, columnspan=2, pady=10)  

        self.view_doctor_frame = tk.Frame(root, background='#C3E7F3')
        self.view_doctor_frame.pack(side=tk.TOP, fill=tk.X)

        self.view_doctor_button = tk.Button(self.view_doctor_frame, text="View Doctors", font=self.default_font, command=self.view_doctors, width=20)
        self.view_doctor_button.pack(pady=10)

        self.edit_doctor_frame = tk.Frame(root, background='#C3E7F3')
        self.edit_doctor_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(self.edit_doctor_frame, text="Doctor ID to Edit:", font=self.default_font, background='#C3E7F3').grid(row=0, column=0, padx=5, pady=5)
        self.doctor_id_entry = tk.Entry(self.edit_doctor_frame, font=self.default_font)
        self.doctor_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.edit_doctor_button = tk.Button(self.edit_doctor_frame, text="Edit Doctor Info", font=self.default_font, command=self.edit_doctor, width=20)
        self.edit_doctor_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.doctor_list_text = tk.Text(root, height=10, width=80, font=self.default_font)
        self.doctor_list_text.pack(pady=10)

        self.back_button = tk.Button(root, text="Back to Dashboard", font=self.default_font, command=self.back_to_dashboard, width=20)
        self.back_button.pack(pady=10)

        self.doctors = {}

    def set_full_size(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")

    def add_doctor(self):
        name = self.doctor_name_entry.get()
        specialization = self.specialization_entry.get()
        mobile = self.mobile_entry.get()
        email = self.email_entry.get()

        if name and specialization and mobile and email:
            DOCTOR = (name, specialization, mobile, email)  # Create a tuple of values
            result = db.add_doctor(*DOCTOR)  # Pass tuple unpacked as arguments
            if result:
                doctor_id = len(self.doctors) + 1
                self.doctors[doctor_id] = {"Name": name, "Specialization": specialization, "Mobile": mobile, "Email": email}
                messagebox.showinfo("Success", f"Doctor added with ID: {doctor_id}")
                self.clear_doctor_entries()
            else:
                messagebox.showerror("Error", "Failed to add doctor to database")
        else:
            messagebox.showerror("Error", "All fields are required")

    def view_doctors(self):
        self.doctor_list_text.delete(1.0, tk.END)
        if self.doctors:
            for doctor_id, doctor in self.doctors.items():
                self.doctor_list_text.insert(tk.END, f"Doctor ID: {doctor_id}\nName: {doctor['Name']}\nSpecialization: {doctor['Specialization']}\nMobile: {doctor['Mobile']}\nEmail: {doctor['Email']}\n\n")
        else:
            self.doctor_list_text.insert(tk.END, "No doctors found")

    def edit_doctor(self):
        doctor_id = self.doctor_id_entry.get()
        if doctor_id.isdigit() and int(doctor_id) in self.doctors:
            doctor = self.doctors[int(doctor_id)]
            messagebox.showinfo("Edit Doctor Info", f"Doctor ID: {doctor_id}\nName: {doctor['Name']}\nSpecialization: {doctor['Specialization']}\nMobile: {doctor['Mobile']}\nEmail: {doctor['Email']}")

            # Prompt the user to enter new details for the doctor
            new_name = simpledialog.askstring("Edit Doctor Info", "Enter new Name:", initialvalue=doctor['Name'])
            new_specialization = simpledialog.askstring("Edit Doctor Info", "Enter new Specialization:", initialvalue=doctor['Specialization'])
            new_mobile = simpledialog.askstring("Edit Doctor Info", "Enter new Mobile:", initialvalue=doctor['Mobile'])
            new_email = simpledialog.askstring("Edit Doctor Info", "Enter new Email:", initialvalue=doctor['Email'])

            if new_name and new_specialization and new_mobile and new_email:
                self.doctors[int(doctor_id)] = {
                    "Name": new_name,
                    "Specialization": new_specialization,
                    "Mobile": new_mobile,
                    "Email": new_email
                }
                messagebox.showinfo("Success", "Doctor info updated successfully")
            else:
                messagebox.showerror("Error", "All fields are required")
        else:
            messagebox.showerror("Error", "Invalid Doctor ID")

    def clear_doctor_entries(self):
        self.doctor_name_entry.delete(0, tk.END)
        self.specialization_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def back_to_dashboard(self):
        self.root.destroy()
        self.parent.deiconify()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class PatientManagement:
    def _init_(self, root, parent):
        self.root = root
        self.parent = parent
        self.root.title("Patient Management System")
        self.root.configure(background='#C2EDFB')

        # Welcome label
        welcome_label = tk.Label(self.root, text="Welcome to the MediManager", font=("Arial", 24))
        welcome_label.pack(pady=20)

        # Set window icon
        self.root.iconbitmap(r'C:\Users\debi2\OneDrive\Desktop\hsm_new\icon.ico')

        # Set window to full size
        self.set_full_size()

        self.add_patient_frame = tk.Frame(root, background='#C2EDFB')
        self.add_patient_frame.pack(side=tk.TOP, fill=tk.X)

        # Increase font size for labels
        label_font = ('Times New Roman', 15)

        tk.Label(self.add_patient_frame, text="Patient Name:", background='#C2EDFB', font=label_font).grid(row=0, column=0, padx=5, pady=(20, 5))
        self.patient_name_entry = tk.Entry(self.add_patient_frame, font=label_font)
        self.patient_name_entry.grid(row=0, column=1, padx=5, pady=(20, 5))

        tk.Label(self.add_patient_frame, text="Age:", background='#C2EDFB', font=label_font).grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.add_patient_frame, font=label_font)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.add_patient_frame, text="Gender:", background='#C2EDFB', font=label_font).grid(row=2, column=0, padx=5, pady=5)
        self.gender_entry = tk.Entry(self.add_patient_frame, font=label_font)
        self.gender_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.add_patient_frame, text="Diagnosis:", background='#C2EDFB', font=label_font).grid(row=3, column=0, padx=5, pady=5)
        self.diagnosis_entry = tk.Entry(self.add_patient_frame, font=label_font)
        self.diagnosis_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.add_patient_frame, text="Date of Admission:", background='#C2EDFB', font=label_font).grid(row=4, column=0, padx=5, pady=5)
        self.admission_date_entry = tk.Entry(self.add_patient_frame, font=label_font)
        self.admission_date_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.add_patient_frame, text="Date of Discharge:", background='#C2EDFB', font=label_font).grid(row=5, column=0, padx=5, pady=5)
        self.discharge_date_entry = tk.Entry(self.add_patient_frame, font=label_font)
        self.discharge_date_entry.grid(row=5, column=1, padx=5, pady=5)

        # Increase size of buttons
        button_font = ('Helvetica', 10)
        button_width = 15
        button_height = 2

        self.add_patient_button = tk.Button(self.add_patient_frame, text="Add Patient", command=self.add_patient, font=button_font, width=button_width, height=button_height)
        self.add_patient_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.view_patient_frame = tk.Frame(root, background='#C2EDFB')
        self.view_patient_frame.pack(side=tk.TOP, fill=tk.X)

        self.view_patient_button = tk.Button(self.view_patient_frame, text="View Patients", command=self.view_patients, font=button_font, width=button_width, height=button_height)
        self.view_patient_button.pack(pady=10)

        self.edit_patient_frame = tk.Frame(root, background='#C2EDFB')
        self.edit_patient_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(self.edit_patient_frame, text="Patient ID to Edit:", background='#C2EDFB', font=label_font).grid(row=0, column=0, padx=5, pady=5)
        self.patient_id_entry = tk.Entry(self.edit_patient_frame, font=label_font)
        self.patient_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.edit_patient_button = tk.Button(self.edit_patient_frame, text="Edit Patient Info", command=self.edit_patient, font=button_font, width=button_width, height=button_height)
        self.edit_patient_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.patient_list_text = tk.Text(root, height=10, width=80)
        self.patient_list_text.pack(pady=10)

        self.back_button = tk.Button(root, text="Back to Dashboard", command=self.back_to_dashboard, font=button_font, width=button_width, height=button_height)
        self.back_button.pack(pady=10)

        self.patients = {}

    def set_full_size(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")

    def add_patient(self):
        name = self.patient_name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        diagnosis = self.diagnosis_entry.get()
        admission_date = self.admission_date_entry.get()
        discharge_date = self.discharge_date_entry.get()

        if name and age and gender and diagnosis and admission_date and discharge_date:
            PATIENT = (name, age, gender, diagnosis, admission_date, discharge_date)
            result = db.add_patient(*PATIENT)
            if result:
                patient_id = len(self.patients) + 1
                self.patients[patient_id] = {
                    "Name": name,
                    "Age": age,
                    "Gender": gender,
                    "Diagnosis": diagnosis,
                    "Admission Date": admission_date,
                    "Discharge Date": discharge_date
                }
                messagebox.showinfo("Success", f"Patient added with ID: {patient_id}")
                self.clear_patient_entries()
        else:
            messagebox.showerror("Error", "All fields are required")

    def view_patients(self):
        self.patient_list_text.delete(1.0, tk.END)
        if self.patients:
            for patient_id, patient in self.patients.items():
                self.patient_list_text.insert(tk.END, f"Patient ID: {patient_id}\nName: {patient['Name']}\nAge: {patient['Age']}\nGender: {patient['Gender']}\nDiagnosis: {patient['Diagnosis']}\nAdmission Date: {patient['Admission Date']}\nDischarge Date: {patient['Discharge Date']}\n\n")
        else:
            self.patient_list_text.insert(tk.END, "No patients found")

    def edit_patient(self):
        patient_id = self.patient_id_entry.get()
        if patient_id.isdigit() and int(patient_id) in self.patients:
            patient = self.patients[int(patient_id)]
            messagebox.showinfo("Edit Patient Info", f"Patient ID: {patient_id}\nName: {patient['Name']}\nAge: {patient['Age']}\nGender: {patient['Gender']}\nDiagnosis: {patient['Diagnosis']}\nAdmission Date: {patient['Admission Date']}\nDischarge Date: {patient['Discharge Date']}")

            # Prompt the user to enter new details for the patient
            new_name = simpledialog.askstring("Edit Patient Info", "Enter new Name:", initialvalue=patient['Name'])
            new_age = simpledialog.askstring("Edit Patient Info", "Enter new Age:", initialvalue=patient['Age'])
            new_gender = simpledialog.askstring("Edit Patient Info", "Enter new Gender:", initialvalue=patient['Gender'])
            new_diagnosis = simpledialog.askstring("Edit Patient Info", "Enter new Diagnosis:", initialvalue=patient['Diagnosis'])
            new_admission_date = simpledialog.askstring("Edit Patient Info", "Enter new Date of Admission:", initialvalue=patient['Admission Date'])
            new_discharge_date = simpledialog.askstring("Edit Patient Info", "Enter new Date of Discharge:", initialvalue=patient['Discharge Date'])

            if new_name and new_age and new_gender and new_diagnosis and new_admission_date and new_discharge_date:
                self.patients[int(patient_id)] = {
                    "Name": new_name,
                    "Age": new_age,
                    "Gender": new_gender,
                    "Diagnosis": new_diagnosis,
                    "Admission Date": new_admission_date,
                    "Discharge Date": new_discharge_date
                }
                messagebox.showinfo("Success", "Patient info updated successfully")
            else:
                messagebox.showerror("Error", "All fields are required")
        else:
            messagebox.showerror("Error", "Invalid Patient ID")

    def clear_patient_entries(self):
        self.patient_name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.diagnosis_entry.delete(0, tk.END)
        self.admission_date_entry.delete(0, tk.END)
        self.discharge_date_entry.delete(0, tk.END)

    def back_to_dashboard(self):
        self.root.destroy()
        self.parent.deiconify()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class BedManagement:
    def _init_(self, root, parent):
        self.root = root
        self.parent = parent
        self.root.title("Bed Management System")

        # Welcome label
        welcome_label = tk.Label(self.root, text="Welcome to the MediManager", font=("Arial", 24))
        welcome_label.pack(pady=20)

        # Set window icon 
        self.root.iconbitmap(r'C:\Users\debi2\OneDrive\Desktop\hsm_new\icon.ico')

        # Set window to full size
        self.set_full_size()

        self.beds_frame = tk.Frame(root)
        self.beds_frame.pack(fill=tk.BOTH, expand=True)

        self.show_beds_section()

    def set_full_size(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")

    def show_beds_section(self):
        for widget in self.beds_frame.winfo_children():
            widget.destroy()

        title_label = tk.Label(self.beds_frame, text="Beds", font=("Arial", 15, "bold"), bg='white')
        title_label.pack(pady=10)

        no_beds_available = True

        button_font = ("Arial", 15)
        button_padding = {"padx": 15, "pady": 10}
        button_bg = "#CAFCED"  
        button_fg = "black" 

        # Calculate total available beds
        total_beds = sum(beds.values())

        for bed_type, count in beds.items():
            if count > 0:
                no_beds_available = False
                percentage = (count / total_beds) * 100
                bed_button = tk.Button(
                    self.beds_frame,
                    text=f"{bed_type}: {count} available",
                    command=lambda bt=bed_type: self.book_bed(bt),
                    font=button_font,
                    bg=button_bg,
                    fg=button_fg
                )
                bed_button.pack(fill=tk.X, **button_padding)

        if no_beds_available:
            no_beds_label = tk.Label(self.beds_frame, text="No beds available in any category.", bg='white', fg='red')
            no_beds_label.pack(pady=5)

        bookings_label = tk.Label(self.beds_frame, text="Bookings", font=("Arial", 15, "bold"), bg='white')
        bookings_label.pack(pady=10)

        for booking in bed_bookings:
            booking_label = tk.Label(self.beds_frame, text=booking, bg='white')
            booking_label.pack(pady=2)

        # Back to Dashboard button
        self.back_button = tk.Button(
            self.beds_frame,
            text="Back to Dashboard",
            command=self.back_to_dashboard,
            font=button_font,
            bg=button_bg,
            fg=button_fg
        )
        self.back_button.pack(fill=tk.X, **button_padding)

    def book_bed(self, bed_type):
        if beds[bed_type] > 0:
            patient_name = simpledialog.askstring("Patient Name", "Enter patient's name:")
            if patient_name:
                booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                beds[bed_type] -= 1
                booking_info = f"{patient_name} booked {bed_type} on {booking_time}"
                bed_bookings.append(booking_info)
                messagebox.showinfo("Booking Confirmed", f"Bed booked for {patient_name}\nType: {bed_type}\nTime: {booking_time}")
                self.show_beds_section()  # Refresh beds section after booking
            else:
                messagebox.showwarning("Booking Cancelled", "Booking cancelled. No patient name entered.")
        else:
            messagebox.showerror("No Beds Available", f"No available {bed_type}.")

    def back_to_dashboard(self):
        self.root.destroy()
        self.parent.deiconify()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class BillingManagement:
    def _init_(self, root, parent):
        self.root = root
        self.parent = parent
        self.root.title("Billing Management System")
        self.root.configure(background='#C3E7F3')

        # Set window icon 
        self.root.iconbitmap(r'C:\Users\debi2\OneDrive\Desktop\hsm_new\icon.ico')

        # Set window to full size
        self.set_full_size()

        welcome_label = tk.Label(self.root, text="Welcome to the MediManager", font=("Arial", 24))
        welcome_label.pack(pady=20)

        # Font configuration
        self.default_font = ("Times New Roman", 15)  # Default font family and size

        self.add_billing_frame = tk.Frame(root, background='#C3E7F3')
        self.add_billing_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(self.add_billing_frame, text="Patient Name:", font=self.default_font, background='#C3E7F3').grid(row=0, column=0, padx=5, pady=5)
        self.patient_name_entry = tk.Entry(self.add_billing_frame, font=self.default_font)
        self.patient_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.add_billing_frame, text="Doctor Fees:", font=self.default_font, background='#C3E7F3').grid(row=1, column=0, padx=5, pady=5)
        self.doctor_fees_entry = tk.Entry(self.add_billing_frame, font=self.default_font)
        self.doctor_fees_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.add_billing_frame, text="Bed Charges:", font=self.default_font, background='#C3E7F3').grid(row=2, column=0, padx=5, pady=5)
        self.bed_charges_entry = tk.Entry(self.add_billing_frame, font=self.default_font)
        self.bed_charges_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.add_billing_frame, text="Medicine Cost:", font=self.default_font, background='#C3E7F3').grid(row=3, column=0, padx=5, pady=5)
        self.medicine_cost_entry = tk.Entry(self.add_billing_frame, font=self.default_font)
        self.medicine_cost_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.add_billing_frame, text="Miscellaneous:", font=self.default_font, background='#C3E7F3').grid(row=4, column=0, padx=5, pady=5)
        self.miscellaneous_entry = tk.Entry(self.add_billing_frame, font=self.default_font)
        self.miscellaneous_entry.grid(row=4, column=1, padx=5, pady=5)

        self.add_billing_button = tk.Button(self.add_billing_frame, text="Generate Bill", font=self.default_font, command=self.add_billing, width=20)
        self.add_billing_button.grid(row=5, column=0, columnspan=2, pady=10)  # Increased pady for button spacing

        self.view_billing_frame = tk.Frame(root, background='#C3E7F3')
        self.view_billing_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        self.view_bills_button = tk.Button(self.view_billing_frame, text="View Bills", font=self.default_font, command=self.view_bills, width=20)
        self.view_bills_button.pack(pady=10)  # Increased pady for button spacing

        self.back_button = tk.Button(root, text="Back to Dashboard", font=self.default_font, command=self.back_to_dashboard, width=20)
        self.back_button.pack(side=tk.BOTTOM, pady=20)

        self.billing_list = []  # List to store billing data

        # Style configuration
        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=25, borderwidth=1, relief="solid")
        self.style.map('Treeview', background=[('selected', '#c3e7f3')])

        self.style.layout("Treeview", [
            ("Treeview.treearea", {"sticky": "nswe"}),
            ("Treeview.padding", {"sticky": "nswe", "children": [
                ("Treeview.treearea", {"sticky": "nswe"})
            ]})
        ])

    def set_full_size(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")

    def add_billing(self):
        patient_name = self.patient_name_entry.get()
        doctor_fees = self.doctor_fees_entry.get()
        bed_charges = self.bed_charges_entry.get()
        medicine_cost = self.medicine_cost_entry.get()
        miscellaneous = self.miscellaneous_entry.get()

        total_cost = float(doctor_fees) + float(bed_charges) + float(medicine_cost) + float(miscellaneous)

        billing = {"patient_name": patient_name, "doctor_fees": doctor_fees, "bed_charges": bed_charges, "medicine_cost": medicine_cost, "miscellaneous": miscellaneous, "total_cost": total_cost}
        self.billing_list.append(billing)

        messagebox.showinfo("Success", f"Bill generated successfully\nTotal Cost: {total_cost}")
        self.clear_entries()

    def clear_entries(self):
        self.patient_name_entry.delete(0, tk.END)
        self.doctor_fees_entry.delete(0, tk.END)
        self.bed_charges_entry.delete(0, tk.END)
        self.medicine_cost_entry.delete(0, tk.END)
        self.miscellaneous_entry.delete(0, tk.END)

    def view_bills(self):
        if not self.billing_list:
            messagebox.showinfo("Information", "No bills generated yet")
            return

        view_window = tk.Toplevel(self.root)
        view_window.title("View Bills")

        # Set window icon 
        view_window.iconbitmap(r'C:\Users\debi2\OneDrive\Desktop\hsm_new\icon.ico')

        columns = ("patient_name", "doctor_fees", "bed_charges", "medicine_cost", "miscellaneous", "total_cost")

        tree = ttk.Treeview(view_window, columns=columns, show="headings", style="Treeview")
        tree.heading("patient_name", text="Patient Name")
        tree.heading("doctor_fees", text="Doctor Fees")
        tree.heading("bed_charges", text="Bed Charges")
        tree.heading("medicine_cost", text="Medicine Cost")
        tree.heading("miscellaneous", text="Miscellaneous")
        tree.heading("total_cost", text="Total Cost")

        for bill in self.billing_list:
            tree.insert("", tk.END, values=(bill['patient_name'], bill['doctor_fees'], bill['bed_charges'], bill['medicine_cost'], bill['miscellaneous'], bill['total_cost']))

        tree.pack(fill=tk.BOTH, expand=True)

    def back_to_dashboard(self):
        self.root.destroy()
        self.parent.deiconify()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


if _name_ == "_main_":
    root = tk.Tk()
    login_app = LoginWindow(root)
    root.mainloop()
