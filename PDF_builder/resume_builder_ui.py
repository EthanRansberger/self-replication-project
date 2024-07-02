# resume_builder_ui.py

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

        # ATS Platform Selection
        ttk.Label(button_frame, text="Select ATS Platform:").pack(side=tk.LEFT, padx=5)
        self.ats_platform_var = tk.StringVar(value="Taleo")
        self.ats_platform_menu = ttk.Combobox(button_frame, textvariable=self.ats_platform_var)
        self.ats_platform_menu['values'] = ("Taleo", "Workday")
        self.ats_platform_menu.pack(side=tk.LEFT, padx=5)

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
            skill_type = "Hard Skill" if is_hard_skill else "Soft Skill"
            skill_entry = f"{skill_name} ({skill_type})"
            self.skills_listbox.insert(tk.END, skill_entry)
            self.person.add_skill(skill_name)
            self.skill_name_entry.delete(0, tk.END)
            self.is_hard_skill_var.set(False)

    def add_education(self):
        degree = self.education_fields["Degree"].get()
        major = self.education_fields["Major"].get()
        minor = self.education_fields["Minor"].get()
        institution = self.education_fields["Institution"].get()
        start_date = self.education_fields["Start Date"].get()
        end_date = self.education_fields["End Date"].get()
        additional_info = self.education_fields["Additional Info"].get()
        if degree and institution and start_date and end_date:
            self.person.add_education(degree, institution, start_date, end_date, major, minor, additional_info)
            for field in self.education_fields.values():
                field.set("")

    def add_certification(self):
        name = self.certification_fields["Name"].get()
        issuing_org = self.certification_fields["Issuing Organization"].get()
        issue_date = self.certification_fields["Issue Date"].get()
        expiration_date = self.certification_fields["Expiration Date"].get()
        if name and issuing_org and issue_date:
            self.person.add_certification(name, issuing_org, issue_date, expiration_date)
            for field in self.certification_fields.values():
                field.set("")

    def add_project(self):
        title = self.project_fields["Title"].get()
        description = self.project_fields["Description"].get()
        technologies = self.project_fields["Technologies"].get()
        start_date = self.project_fields["Start Date"].get()
        end_date = self.project_fields["End Date"].get()
        if title and description and technologies and start_date and end_date:
            self.person.add_project(title, description, technologies, start_date, end_date)
            for field in self.project_fields.values():
                field.set("")

    def add_award(self):
        name = self.award_fields["Name"].get()
        description = self.award_fields["Description"].get()
        date = self.award_fields["Date"].get()
        if name and description and date:
            self.person.add_award(name, description, date)
            for field in self.award_fields.values():
                field.set("")

    def add_publication(self):
        title = self.publication_fields["Title"].get()
        journal = self.publication_fields["Journal"].get()
        date = self.publication_fields["Date"].get()
        description = self.publication_fields["Description"].get()
        if title and journal and date and description:
            self.person.add_publication(title, journal, date, description)
            for field in self.publication_fields.values():
                field.set("")

    def add_volunteer_experience(self):
        role = self.volunteer_fields["Role"].get()
        organization = self.volunteer_fields["Organization"].get()
        start_date = self.volunteer_fields["Start Date"].get()
        end_date = self.volunteer_fields["End Date"].get()
        description = self.volunteer_fields["Description"].get()
        if role and organization and start_date and end_date and description:
            self.person.add_volunteer_experience(role, organization, start_date, end_date, description)
            for field in self.volunteer_fields.values():
                field.set("")

    def add_job(self):
        title = self.job_fields["Title"].get()
        company = self.job_fields["Company"].get()
        start_date = self.job_fields["Start Date"].get()
        end_date = self.job_fields["End Date"].get()
        description = self.job_fields["Description"].get()
        if title and company and start_date and end_date and description:
            self.person.add_experience(title, company, start_date, end_date, description)
            for field in self.job_fields.values():
                field.set("")

    def add_language(self):
        name = self.language_fields["Name"].get()
        proficiency = self.language_fields["Proficiency"].get()
        if name and proficiency:
            self.person.add_language(name, proficiency)
            for field in self.language_fields.values():
                field.set("")

    def save_resume(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            self.person.save_to_json(filename)
            messagebox.showinfo("Success", "Resume saved successfully!")

    def load_resume(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            self.person = resume_util.Person.load_from_json(filename)
            messagebox.showinfo("Success", "Resume loaded successfully!")

    def convert_to_pdf(self):
        filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if filename:
            ats_platform = self.ats_platform_var.get()
            pdf_generator = PDFGenerator(self.person, filename, platform=ats_platform)
            pdf_generator.generate_pdf()
            messagebox.showinfo("Success", "Resume converted to PDF successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeBuilderUI(root)
    root.mainloop()
