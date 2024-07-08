import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import resume_util
from pdf_generator import PDFGenerator
from resume_management import ResumeManager

class ResumeBuilderUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Builder")
        self.person = resume_util.Person(contact_info={})
        
        # Main UI Components
        self.create_widgets()
        
    def create_widgets(self):
        # Create a frame for the tabs
        tab_frame = ttk.Frame(self.root)
        tab_frame.pack(padx=10, pady=10, fill='x')
        
        # Tabs
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(expand=1, fill='both')

        self.create_contact_tab()
        self.create_skills_tab()
        self.create_education_tab()
        self.create_certifications_tab()
        self.create_projects_tab()
        self.create_awards_tab()
        self.create_publications_tab()
        self.create_volunteer_experiences_tab()
        self.create_jobs_tab()
        self.create_languages_tab()

        # Save and Load Resume Buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Save Resume", command=self.save_resume).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Load Resume", command=self.load_resume).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Convert to PDF", command=self.convert_to_pdf).pack(side=tk.LEFT, padx=5)

    def create_contact_tab(self):
        contact_frame = ttk.Frame(self.tabs)
        self.tabs.add(contact_frame, text='Contact Info')

        self.contact_fields = {
            "Name": tk.StringVar(),
            "Phone Number": tk.StringVar(),
            "Email": tk.StringVar(),
            "LinkedIn": tk.StringVar(),
            "Repository Link": tk.StringVar(),
            "Address": tk.StringVar()
        }

        row = 0
        for field, var in self.contact_fields.items():
            ttk.Label(contact_frame, text=field).grid(row=row, column=0, sticky='w')
            ttk.Entry(contact_frame, textvariable=var).grid(row=row, column=1, padx=5, pady=5, sticky='ew')
            row += 1

    def create_skills_tab(self):
        skills_frame = ttk.Frame(self.tabs)
        self.tabs.add(skills_frame, text='Skills')

        ttk.Label(skills_frame, text="Skill").grid(row=0, column=0, sticky='w')
        self.skill_name_entry = ttk.Entry(skills_frame)
        self.skill_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        self.is_hard_skill_var = tk.BooleanVar()
        ttk.Checkbutton(skills_frame, text="Hard Skill", variable=self.is_hard_skill_var).grid(row=0, column=2, padx=5, pady=5)

        ttk.Button(skills_frame, text="Add Skill", command=self.add_skill).grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(skills_frame, text="Skills List").grid(row=1, column=0, columnspan=2, sticky='w')
        self.skills_listbox = tk.Listbox(skills_frame)
        self.skills_listbox.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky='ew')

    def create_education_tab(self):
        education_frame = ttk.Frame(self.tabs)
        self.tabs.add(education_frame, text='Education')

        self.education_fields = {
            "Degree": tk.StringVar(),
            "Major": tk.StringVar(),
            "Minor": tk.StringVar(),
            "Institution": tk.StringVar(),
            "Start Date": tk.StringVar(),
            "End Date": tk.StringVar(),
            "Additional Info": tk.StringVar()
        }

        row = 0
        for field, var in self.education_fields.items():
            ttk.Label(education_frame, text=field).grid(row=row, column=0, sticky='w')
            ttk.Entry(education_frame, textvariable=var).grid(row=row, column=1, padx=5, pady=5, sticky='ew')
            row += 1

        ttk.Button(education_frame, text="Add Education", command=self.add_education).grid(row=row, column=1, padx=5, pady=5)

    def create_certifications_tab(self):
        certifications_frame = ttk.Frame(self.tabs)
        self.tabs.add(certifications_frame, text='Certifications')

        self.certification_fields = {
            "Name": tk.StringVar(),
            "Issuing Organization": tk.StringVar(),
            "Issue Date": tk.StringVar(),
            "Expiration Date": tk.StringVar()
        }

        row = 0
        for field, var in self.certification_fields.items():
            ttk.Label(certifications_frame, text=field).grid(row=row, column=0, sticky='w')
            ttk.Entry(certifications_frame, textvariable=var).grid(row=row, column=1, padx=5, pady=5, sticky='ew')
            row += 1

        ttk.Button(certifications_frame, text="Add Certification", command=self.add_certification).grid(row=row, column=1, padx=5, pady=5)

    def create_projects_tab(self):
        projects_frame = ttk.Frame(self.tabs)
        self.tabs.add(projects_frame, text='Projects')

        self.project_fields = {
            "Title": tk.StringVar(),
            "Description": tk.StringVar(),
            "Technologies": tk.StringVar(),
            "Start Date": tk.StringVar(),
            "End Date": tk.StringVar()
        }

        row = 0
        for field, var in self.project_fields.items():
            ttk.Label(projects_frame, text=field).grid(row=row, column=0, sticky='w')
            ttk.Entry(projects_frame, textvariable=var).grid(row=row, column=1, padx=5, pady=5, sticky='ew')
            row += 1

        ttk.Button(projects_frame, text="Add Project", command=self.add_project).grid(row=row, column=1, padx=5, pady=5)

    def create_awards_tab(self):
        awards_frame = ttk.Frame(self.tabs)
        self.tabs.add(awards_frame, text='Awards')

        self.award_fields = {
            "Name": tk.StringVar(),
            "Description": tk.StringVar(),
            "Date": tk.StringVar()
        }

        row = 0
        for field, var in self.award_fields.items():
            ttk.Label(awards_frame, text=field).grid(row=row, column=0, sticky='w')
            ttk.Entry(awards_frame, textvariable=var).grid(row=row, column=1, padx=5, pady=5, sticky='ew')
            row += 1

        ttk.Button(awards_frame, text="Add Award", command=self.add_award).grid(row=row, column=1, padx=5, pady=5)

    def create_publications_tab(self):
        publications_frame = ttk.Frame(self.tabs)
        self.tabs.add(publications_frame, text='Publications')

        self.publication_fields = {
            "Title": tk.StringVar(),
            "Journal": tk.StringVar(),
            "Date": tk.StringVar(),
            "Description": tk.StringVar()
        }

        row = 0
        for field, var in self.publication_fields.items():
            ttk.Label(publications_frame, text=field).grid(row=row, column=0, sticky='w')
            ttk.Entry(publications_frame, textvariable=var).grid(row=row, column=1, padx=5, pady=5, sticky='ew')
            row += 1

        ttk.Button(publications_frame, text="Add Publication", command=self.add_publication).grid(row=row, column=1, padx=5, pady=5)

    def create_volunteer_experiences_tab(self):
        volunteer_experiences_frame = ttk.Frame(self.tabs)
        self.tabs.add(volunteer_experiences_frame, text='Volunteer Experiences')

        self.volunteer_fields = {
            "Role": tk.StringVar(),
            "Organization": tk.StringVar(),
            "Start Date": tk.StringVar(),
            "End Date": tk.StringVar(),
            "Description": tk.StringVar()
        }

        row = 0
        for field, var in self.volunteer_fields.items():
            ttk.Label(volunteer_experiences_frame, text=field).grid(row=row, column=0, sticky='w')
            ttk.Entry(volunteer_experiences_frame, textvariable=var).grid(row=row, column=1, padx=5, pady=5, sticky='ew')
            row += 1

        ttk.Button(volunteer_experiences_frame, text="Add Volunteer Experience", command=self.add_volunteer_experience).grid(row=row, column=1, padx=5, pady=5)

    def create_jobs_tab(self):
        jobs_frame = ttk.Frame(self.tabs)
        self.tabs.add(jobs_frame, text='Jobs')

        self.job_fields = {
            "Title": tk.StringVar(),
            "Company": tk.StringVar(),
            "Start Date": tk.StringVar(),
            "End Date": tk.StringVar(),
            "Description": tk.StringVar()
        }

        row = 0
        for field, var in self.job_fields.items():
            ttk.Label(jobs_frame, text=field).grid(row=row, column=0, sticky='w')
            ttk.Entry(jobs_frame, textvariable=var).grid(row=row, column=1, padx=5, pady=5, sticky='ew')
            row += 1

        ttk.Button(jobs_frame, text="Add Job", command=self.add_job).grid(row=row, column=1, padx=5, pady=5)

    def create_languages_tab(self):
        languages_frame = ttk.Frame(self.tabs)
        self.tabs.add(languages_frame, text='Languages')

        self.language_fields = {
            "Name": tk.StringVar(),
            "Proficiency": tk.StringVar()
        }

        row = 0
        for field, var in self.language_fields.items():
            ttk.Label(languages_frame, text=field).grid(row=row, column=0, sticky='w')
            ttk.Entry(languages_frame, textvariable=var).grid(row=row, column=1, padx=5, pady=5, sticky='ew')
            row += 1

        ttk.Button(languages_frame, text="Add Language", command=self.add_language).grid(row=row, column=1, padx=5, pady=5)

    def add_skill(self):
        skill_name = self.skill_name_entry.get()
        is_hard_skill = self.is_hard_skill_var.get()

        if skill_name:
            skill_type = 'Hard' if is_hard_skill else 'Soft'
            self.skills_listbox.insert(tk.END, f"{skill_name} ({skill_type})")
            self.person.add_skill(skill_name, is_hard_skill)
            self.skill_name_entry.delete(0, tk.END)

    def add_education(self):
        education_data = {field: var.get() for field, var in self.education_fields.items()}
        self.person.add_education(**education_data)
        messagebox.showinfo("Success", "Education added successfully.")

    def add_certification(self):
        certification_data = {field: var.get() for field, var in self.certification_fields.items()}
        self.person.add_certification(**certification_data)
        messagebox.showinfo("Success", "Certification added successfully.")

    def add_project(self):
        project_data = {field: var.get() for field, var in self.project_fields.items()}
        self.person.add_project(**project_data)
        messagebox.showinfo("Success", "Project added successfully.")

    def add_award(self):
        award_data = {field: var.get() for field, var in self.award_fields.items()}
        self.person.add_award(**award_data)
        messagebox.showinfo("Success", "Award added successfully.")

    def add_publication(self):
        publication_data = {field: var.get() for field, var in self.publication_fields.items()}
        self.person.add_publication(**publication_data)
        messagebox.showinfo("Success", "Publication added successfully.")

    def add_volunteer_experience(self):
        volunteer_data = {field: var.get() for field, var in self.volunteer_fields.items()}
        self.person.add_volunteer_experience(**volunteer_data)
        messagebox.showinfo("Success", "Volunteer experience added successfully.")

    def add_job(self):
        job_data = {field: var.get() for field, var in self.job_fields.items()}
        self.person.add_job(**job_data)
        messagebox.showinfo("Success", "Job added successfully.")

    def add_language(self):
        language_data = {field: var.get() for field, var in self.language_fields.items()}
        self.person.add_language(**language_data)
        messagebox.showinfo("Success", "Language added successfully.")

    def save_resume(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            self.person.save_to_file(file_path)
            messagebox.showinfo("Success", "Resume saved successfully.")

    def load_resume(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            self.person.load_from_file(file_path)
            self.update_ui_from_person()
            messagebox.showinfo("Success", "Resume loaded successfully.")

    def update_ui_from_person(self):
        for field, var in self.contact_fields.items():
            var.set(self.person.contact_info.get(field, ""))

        # Clear the skills listbox
        self.skills_listbox.delete(0, tk.END)
        for skill in self.person.skills:
            skill_type = 'Hard' if skill.is_hard else 'Soft'
            self.skills_listbox.insert(tk.END, f"{skill.name} ({skill_type})")

    def convert_to_pdf(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            pdf_gen = PDFGenerator(self.person, file_path)
            pdf_gen.generate_pdf()
            messagebox.showinfo("Success", "PDF generated successfully.")
