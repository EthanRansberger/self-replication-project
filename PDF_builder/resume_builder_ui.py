# resume_builder_ui.py

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import resume_util

class ResumeBuilderUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Builder")
        self.person = resume_util.Person(contact_info="")
        
        # Main UI Components
        self.create_widgets()
        
    def create_widgets(self):
        # Create a frame for the form
        form_frame = ttk.Frame(self.root)
        form_frame.pack(padx=10, pady=10, fill='x')
        
        # Contact Info
        ttk.Label(form_frame, text="Contact Info").grid(row=0, column=0, sticky='w')
        self.contact_info_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.contact_info_var).grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        
        # Add Skills
        ttk.Label(form_frame, text="Add Skill").grid(row=1, column=0, sticky='w')
        self.skill_entry = ttk.Entry(form_frame)
        self.skill_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
        ttk.Button(form_frame, text="Add Skill", command=self.add_skill).grid(row=1, column=2, padx=5, pady=5)
        
        # Skills Listbox
        ttk.Label(form_frame, text="Skills").grid(row=2, column=0, sticky='w')
        self.skills_listbox = tk.Listbox(form_frame)
        self.skills_listbox.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky='ew')

        # Add Experience
        ttk.Label(form_frame, text="Add Experience").grid(row=3, column=0, sticky='w')
        self.experience_title = ttk.Entry(form_frame)
        self.experience_title.grid(row=3, column=1, padx=5, pady=5, sticky='ew')
        self.experience_company = ttk.Entry(form_frame)
        self.experience_company.grid(row=4, column=1, padx=5, pady=5, sticky='ew')
        self.experience_start_date = ttk.Entry(form_frame)
        self.experience_start_date.grid(row=5, column=1, padx=5, pady=5, sticky='ew')
        self.experience_end_date = ttk.Entry(form_frame)
        self.experience_end_date.grid(row=6, column=1, padx=5, pady=5, sticky='ew')
        ttk.Button(form_frame, text="Add Experience", command=self.add_experience).grid(row=7, column=1, padx=5, pady=5)

        # Add Education
        ttk.Label(form_frame, text="Add Education").grid(row=8, column=0, sticky='w')
        self.education_degree = ttk.Entry(form_frame)
        self.education_degree.grid(row=8, column=1, padx=5, pady=5, sticky='ew')
        self.education_institution = ttk.Entry(form_frame)
        self.education_institution.grid(row=9, column=1, padx=5, pady=5, sticky='ew')
        self.education_start_date = ttk.Entry(form_frame)
        self.education_start_date.grid(row=10, column=1, padx=5, pady=5, sticky='ew')
        self.education_end_date = ttk.Entry(form_frame)
        self.education_end_date.grid(row=11, column=1, padx=5, pady=5, sticky='ew')
        ttk.Button(form_frame, text="Add Education", command=self.add_education).grid(row=12, column=1, padx=5, pady=5)

        # Add Certification
        ttk.Label(form_frame, text="Add Certification").grid(row=13, column=0, sticky='w')
        self.certification_name = ttk.Entry(form_frame)
        self.certification_name.grid(row=13, column=1, padx=5, pady=5, sticky='ew')
        self.certification_issuing_org = ttk.Entry(form_frame)
        self.certification_issuing_org.grid(row=14, column=1, padx=5, pady=5, sticky='ew')
        self.certification_issue_date = ttk.Entry(form_frame)
        self.certification_issue_date.grid(row=15, column=1, padx=5, pady=5, sticky='ew')
        self.certification_expiration_date = ttk.Entry(form_frame)
        self.certification_expiration_date.grid(row=16, column=1, padx=5, pady=5, sticky='ew')
        ttk.Button(form_frame, text="Add Certification", command=self.add_certification).grid(row=17, column=1, padx=5, pady=5)

        # Certifications Listbox
        ttk.Label(form_frame, text="Certifications").grid(row=18, column=0, sticky='w')
        self.certifications_listbox = tk.Listbox(form_frame)
        self.certifications_listbox.grid(row=18, column=1, columnspan=2, padx=5, pady=5, sticky='ew')

        # Add Project
        ttk.Label(form_frame, text="Add Project").grid(row=19, column=0, sticky='w')
        self.project_title = ttk.Entry(form_frame)
        self.project_title.grid(row=19, column=1, padx=5, pady=5, sticky='ew')
        self.project_description = ttk.Entry(form_frame)
        self.project_description.grid(row=20, column=1, padx=5, pady=5, sticky='ew')
        self.project_technologies = ttk.Entry(form_frame)
        self.project_technologies.grid(row=21, column=1, padx=5, pady=5, sticky='ew')
        self.project_start_date = ttk.Entry(form_frame)
        self.project_start_date.grid(row=22, column=1, padx=5, pady=5, sticky='ew')
        self.project_end_date = ttk.Entry(form_frame)
        self.project_end_date.grid(row=23, column=1, padx=5, pady=5, sticky='ew')
        ttk.Button(form_frame, text="Add Project", command=self.add_project).grid(row=24, column=1, padx=5, pady=5)

        # Projects Listbox
        ttk.Label(form_frame, text="Projects").grid(row=25, column=0, sticky='w')
        self.projects_listbox = tk.Listbox(form_frame)
        self.projects_listbox.grid(row=25, column=1, columnspan=2, padx=5, pady=5, sticky='ew')

        # Save Resume Button
        ttk.Button(form_frame, text="Save Resume", command=self.save_resume).grid(row=26, column=1, padx=5, pady=5)

    def add_skill(self):
        skill = self.skill_entry.get()
        if skill:
            self.person.add_skill(skill)
            self.skills_listbox.insert(tk.END, skill)
            self.skill_entry.delete(0, tk.END)

    def add_experience(self):
        title = self.experience_title.get()
        company = self.experience_company.get()
        start_date = self.experience_start_date.get()
        end_date = self.experience_end_date.get()
        if title and company and start_date and end_date:
            self.person.add_experience(title, company, start_date, end_date)
            self.experience_title.delete(0, tk.END)
            self.experience_company.delete(0, tk.END)
            self.experience_start_date.delete(0, tk.END)
            self.experience_end_date.delete(0, tk.END)

    def add_education(self):
        degree = self.education_degree.get()
        institution = self.education_institution.get()
        start_date = self.education_start_date.get()
        end_date = self.education_end_date.get()
        if degree and institution and start_date and end_date:
            self.person.add_education(degree, institution, start_date, end_date)
            self.education_degree.delete(0, tk.END)
            self.education_institution.delete(0, tk.END)
            self.education_start_date.delete(0, tk.END)
            self.education_end_date.delete(0, tk.END)

    def add_certification(self):
        name = self.certification_name.get()
        issuing_org = self.certification_issuing_org.get()
        issue_date = self.certification_issue_date.get()
        expiration_date = self.certification_expiration_date.get()
        if name and issuing_org and issue_date:
            self.person.add_certification(name, issuing_org, issue_date, expiration_date)
            self.certification_name.delete(0, tk.END)
            self.certification_issuing_org.delete(0, tk.END)
            self.certification_issue_date.delete(0, tk.END)
            self.certification_expiration_date.delete(0, tk.END)
            self.certifications_listbox.insert(tk.END, name)

    def add_project(self):
        title = self.project_title.get()
        description = self.project_description.get()
        technologies = self.project_technologies.get()
        start_date = self.project_start_date.get()
        end_date = self.project_end_date.get()
        if title and description and technologies and start_date and end_date:
            self.person.add_project(title, description, technologies, start_date, end_date)
            self.project_title.delete(0, tk.END)
            self.project_description.delete(0, tk.END)
            self.project_technologies.delete(0, tk.END)
            self.project_start_date.delete(0, tk.END)
            self.project_end_date.delete(0, tk.END)
            self.projects_listbox.insert(tk.END, title)

    def save_resume(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            self.person.save_to_json(filename)
            messagebox.showinfo("Success", "Resume saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeBuilderUI(root)
    root.mainloop()
