# resume_builder_ui.py
import tkinter as tk
from tkinter import simpledialog, messagebox
from resume_management import ResumeManager
from pdf_generator import PDFGenerator

class ResumeBuilderUI:
    def __init__(self, master):
        self.master = master
        master.title("Resume Builder")
        master.geometry("800x600")
        master.configure(bg='#ecf0f1')

        self.resume_manager = ResumeManager()

        # Tabs
        self.tab_control = tk.Notebook(master)

        # Basic Info Tab
        self.basic_info_tab = tk.Frame(self.tab_control, bg='#f0f0f0')
        self.tab_control.add(self.basic_info_tab, text="Basic Info")

        # Skills Tab
        self.skills_tab = tk.Frame(self.tab_control, bg='#f0f0f0')
        self.tab_control.add(self.skills_tab, text="Skills")

        # Certifications Tab
        self.certifications_tab = tk.Frame(self.tab_control, bg='#f0f0f0')
        self.tab_control.add(self.certifications_tab, text="Certifications")

        # Projects Tab
        self.projects_tab = tk.Frame(self.tab_control, bg='#f0f0f0')
        self.tab_control.add(self.projects_tab, text="Projects")

        # Awards Tab
        self.awards_tab = tk.Frame(self.tab_control, bg='#f0f0f0')
        self.tab_control.add(self.awards_tab, text="Awards")

        # Languages Tab
        self.languages_tab = tk.Frame(self.tab_control, bg='#f0f0f0')
        self.tab_control.add(self.languages_tab, text="Languages")

        # Volunteer Experiences Tab
        self.volunteer_tab = tk.Frame(self.tab_control, bg='#f0f0f0')
        self.tab_control.add(self.volunteer_tab, text="Volunteer Experiences")

        # Professional Memberships Tab
        self.memberships_tab = tk.Frame(self.tab_control, bg='#f0f0f0')
        self.tab_control.add(self.memberships_tab, text="Professional Memberships")

        # Publications Tab
        self.publications_tab = tk.Frame(self.tab_control, bg='#f0f0f0')
        self.tab_control.add(self.publications_tab, text="Publications")

        self.tab_control.pack(expand=1, fill='both')

        # Basic Info Tab
        self.basic_info_title = tk.Label(self.basic_info_tab, text="Basic Information", font=('Helvetica', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        self.basic_info_title.pack(pady=10)

        self.name_label = tk.Label(self.basic_info_tab, text="Name:", font=('Helvetica', 12), bg='#f0f0f0', fg='#2c3e50')
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.basic_info_tab, width=50)
        self.name_entry.pack(pady=5)

        self.contact_label = tk.Label(self.basic_info_tab, text="Contact Information:", font=('Helvetica', 12), bg='#f0f0f0', fg='#2c3e50')
        self.contact_label.pack(pady=5)
        self.contact_entry = tk.Entry(self.basic_info_tab, width=50)
        self.contact_entry.pack(pady=5)

        self.summary_label = tk.Label(self.basic_info_tab, text="Summary:", font=('Helvetica', 12), bg='#f0f0f0', fg='#2c3e50')
        self.summary_label.pack(pady=5)
        self.summary_text = tk.Text(self.basic_info_tab, height=4, width=50)
        self.summary_text.pack(pady=5)

        self.save_button = tk.Button(self.basic_info_tab, text="Save", command=self.save_basic_info, font=('Helvetica', 12), bg='#3498db', fg='#ffffff')
        self.save_button.pack(pady=10)

        # Other Tabs UI Code (like above)

        # Save and Generate PDF Buttons
        self.save_button = tk.Button(master, text="Save Resume", command=self.save_resume, font=('Helvetica', 14), bg='#27ae60', fg='#ffffff')
        self.save_button.pack(pady=5, side='left', padx=10)

        self.generate_pdf_button = tk.Button(master, text="Generate PDF", command=self.generate_pdf, font=('Helvetica', 14), bg='#e74c3c', fg='#ffffff')
        self.generate_pdf_button.pack(pady=5, side='left', padx=10)

    def save_basic_info(self):
        name = self.name_entry.get()
        contact_info = self.contact_entry.get()
        summary = self.summary_text.get("1.0", tk.END).strip()
        self.resume_manager.create_resume(name, contact_info, summary)
        messagebox.showinfo("Info", "Basic Info saved successfully!")

    def save_resume(self):
        resume = self.resume_manager.get_resume()
        if resume:
            # Perform saving actions, e.g., save to JSON
            messagebox.showinfo("Info", "Resume saved successfully!")
        else:
            messagebox.showerror("Error", "No resume to save!")

    def generate_pdf(self):
        resume = self.resume_manager.get_resume()
        if resume:
            pdf_generator = PDFGenerator(resume)
            pdf_generator.generate_pdf('resume.pdf')
            messagebox.showinfo("Info", "PDF generated successfully!")
        else:
            messagebox.showerror("Error", "No resume to generate PDF!")
