# resume_management.py

import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk  # Import ttk for Notebook
from resume_util import (
    Resume, Skill, Certification, Project, Award, Language, VolunteerExperience,
    ProfessionalMembership, Publication
)
from pdf_generator import PDFGenerator

class ResumeBuilderUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Resume Builder")
        self.master.geometry("600x600")
        self.master.configure(bg='#ecf0f1')

        self.resume_manager = ResumeManager()
        
        # Create and pack the tab control
        self.tab_control = ttk.Notebook(self.master)  # Use ttk.Notebook instead of tk.Notebook
        self.tab_control.pack(expand=1, fill="both")

        self.basic_info_tab = tk.Frame(self.tab_control, bg='#ecf0f1')
        self.skills_tab = tk.Frame(self.tab_control, bg='#ecf0f1')
        self.certifications_tab = tk.Frame(self.tab_control, bg='#ecf0f1')
        self.projects_tab = tk.Frame(self.tab_control, bg='#ecf0f1')
        self.awards_tab = tk.Frame(self.tab_control, bg='#ecf0f1')
        self.languages_tab = tk.Frame(self.tab_control, bg='#ecf0f1')
        self.volunteer_tab = tk.Frame(self.tab_control, bg='#ecf0f1')
        self.memberships_tab = tk.Frame(self.tab_control, bg='#ecf0f1')
        self.publications_tab = tk.Frame(self.tab_control, bg='#ecf0f1')

        self.tab_control.add(self.basic_info_tab, text='Basic Info')
        self.tab_control.add(self.skills_tab, text='Skills')
        self.tab_control.add(self.certifications_tab, text='Certifications')
        self.tab_control.add(self.projects_tab, text='Projects')
        self.tab_control.add(self.awards_tab, text='Awards')
        self.tab_control.add(self.languages_tab, text='Languages')
        self.tab_control.add(self.volunteer_tab, text='Volunteer Experiences')
        self.tab_control.add(self.memberships_tab, text='Professional Memberships')
        self.tab_control.add(self.publications_tab, text='Publications')

        # Initialize all the widgets
        self.create_basic_info_widgets()
        self.create_skills_widgets()
        self.create_certifications_widgets()
        self.create_projects_widgets()
        self.create_awards_widgets()
        self.create_languages_widgets()
        self.create_volunteer_widgets()
        self.create_memberships_widgets()
        self.create_publications_widgets()

        # Add Save Button
        self.save_button = tk.Button(self.master, text="Save Resume to PDF", command=self.save_resume_to_pdf, font=('Helvetica', 14, 'bold'), bg='#2ecc71', fg='#ffffff')
        self.save_button.pack(pady=20)

    def create_basic_info_widgets(self):
        title = tk.Label(self.basic_info_tab, text="Basic Information", font=('Helvetica', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=10)

        tk.Label(self.basic_info_tab, text="Name:", bg='#ecf0f1', font=('Helvetica', 12)).pack(pady=5, anchor='w', padx=10)
        self.name_entry = tk.Entry(self.basic_info_tab, width=50)
        self.name_entry.pack(pady=5)

        tk.Label(self.basic_info_tab, text="Contact Info:", bg='#ecf0f1', font=('Helvetica', 12)).pack(pady=5, anchor='w', padx=10)
        self.contact_entry = tk.Entry(self.basic_info_tab, width=50)
        self.contact_entry.pack(pady=5)

        tk.Label(self.basic_info_tab, text="Summary:", bg='#ecf0f1', font=('Helvetica', 12)).pack(pady=5, anchor='w', padx=10)
        self.summary_text = tk.Text(self.basic_info_tab, width=50, height=5)
        self.summary_text.pack(pady=5)

        self.save_basic_info_button = tk.Button(self.basic_info_tab, text="Save Basic Info", command=self.save_basic_info, font=('Helvetica', 12), bg='#3498db', fg='#ffffff')
        self.save_basic_info_button.pack(pady=10)

    def create_skills_widgets(self):
        title = tk.Label(self.skills_tab, text="Skills", font=('Helvetica', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=10)

        self.add_skill_button = tk.Button(self.skills_tab, text="Add Skill", command=self.add_skill, font=('Helvetica', 12), bg='#3498db', fg='#ffffff')
        self.add_skill_button.pack(pady=5)

        self.skill_listbox = tk.Listbox(self.skills_tab, width=50)
        self.skill_listbox.pack(pady=5)

    def create_certifications_widgets(self):
        title = tk.Label(self.certifications_tab, text="Certifications", font=('Helvetica', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=10)

        self.add_certification_button = tk.Button(self.certifications_tab, text="Add Certification", command=self.add_certification, font=('Helvetica', 12), bg='#3498db', fg='#ffffff')
        self.add_certification_button.pack(pady=5)

        self.certification_listbox = tk.Listbox(self.certifications_tab, width=50)
        self.certification_listbox.pack(pady=5)

    def create_projects_widgets(self):
        title = tk.Label(self.projects_tab, text="Projects", font=('Helvetica', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=10)

        self.add_project_button = tk.Button(self.projects_tab, text="Add Project", command=self.add_project, font=('Helvetica', 12), bg='#3498db', fg='#ffffff')
        self.add_project_button.pack(pady=5)

        self.project_listbox = tk.Listbox(self.projects_tab, width=50)
        self.project_listbox.pack(pady=5)

    def create_awards_widgets(self):
        title = tk.Label(self.awards_tab, text="Awards", font=('Helvetica', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=10)

        self.add_award_button = tk.Button(self.awards_tab, text="Add Award", command=self.add_award, font=('Helvetica', 12), bg='#3498db', fg='#ffffff')
        self.add_award_button.pack(pady=5)

        self.award_listbox = tk.Listbox(self.awards_tab, width=50)
        self.award_listbox.pack(pady=5)

    def create_languages_widgets(self):
        title = tk.Label(self.languages_tab, text="Languages", font=('Helvetica', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=10)

        self.add_language_button = tk.Button(self.languages_tab, text="Add Language", command=self.add_language, font=('Helvetica', 12), bg='#3498db', fg='#ffffff')
        self.add_language_button.pack(pady=5)

        self.language_listbox = tk.Listbox(self.languages_tab, width=50)
        self.language_listbox.pack(pady=5)

    def create_volunteer_widgets(self):
        title = tk.Label(self.volunteer_tab, text="Volunteer Experiences", font=('Helvetica', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=10)

        self.add_volunteer_button = tk.Button(self.volunteer_tab, text="Add Volunteer Experience", command=self.add_volunteer_experience, font=('Helvetica', 12), bg='#3498db', fg='#ffffff')
        self.add_volunteer_button.pack(pady=5)

        self.volunteer_listbox = tk.Listbox(self.volunteer_tab, width=50)
        self.volunteer_listbox.pack(pady=5)

    def create_memberships_widgets(self):
        title = tk.Label(self.memberships_tab, text="Professional Memberships", font=('Helvetica', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=10)

        self.add_membership_button = tk.Button(self.memberships_tab, text="Add Professional Membership", command=self.add_professional_membership, font=('Helvetica', 12), bg='#3498db', fg='#ffffff')
        self.add_membership_button.pack(pady=5)

        self.membership_listbox = tk.Listbox(self.memberships_tab, width=50)
        self.membership_listbox.pack(pady=5)

    def create_publications_widgets(self):
        title = tk.Label(self.publications_tab, text="Publications", font=('Helvetica', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=10)

        self.add_publication_button = tk.Button(self.publications_tab, text="Add Publication", command=self.add_publication, font=('Helvetica', 12), bg='#3498db', fg='#ffffff')
        self.add_publication_button.pack(pady=5)

        self.publication_listbox = tk.Listbox(self.publications_tab, width=50)
        self.publication_listbox.pack(pady=5)

    def save_basic_info(self):
        name = self.name_entry.get()
        contact_info = self.contact_entry.get()
        summary = self.summary_text.get("1.0", tk.END).strip()
        if name and contact_info:
            self.resume_manager.resume.name = name
            self.resume_manager.resume.contact_info = contact_info
            self.resume_manager.resume.summary = summary
            messagebox.showinfo("Info", "Basic Information Saved Successfully!")
        else:
            messagebox.showerror("Error", "Please enter both name and contact info!")

    def add_skill(self):
        name = simpledialog.askstring("Skill", "Enter Skill Name:")
        level = simpledialog.askstring("Skill", "Enter Skill Level:")
        if name and level:
            skill = Skill(name=name, level=level)
            self.resume_manager.add_skill(skill)
            self.skill_listbox.insert(tk.END, f"{name}: {level}")

    def add_certification(self):
        title = simpledialog.askstring("Certification", "Enter Certification Title:")
        organization = simpledialog.askstring("Certification", "Enter Certification Organization:")
        date = simpledialog.askstring("Certification", "Enter Certification Date:")
        if title and organization and date:
            certification = Certification(title=title, organization=organization, date=date)
            self.resume_manager.add_certification(certification)
            self.certification_listbox.insert(tk.END, f"{title} - {organization} ({date})")

    def add_project(self):
        title = simpledialog.askstring("Project", "Enter Project Title:")
        description = simpledialog.askstring("Project", "Enter Project Description:")
        role = simpledialog.askstring("Project", "Enter Your Role:")
        start_date = simpledialog.askstring("Project", "Enter Project Start Date:")
        end_date = simpledialog.askstring("Project", "Enter Project End Date:")
        if title and description and role and start_date and end_date:
            project = Project(title=title, description=description, role=role, start_date=start_date, end_date=end_date)
            self.resume_manager.add_project(project)
            self.project_listbox.insert(tk.END, f"{title}: {description} ({role}, {start_date} to {end_date})")

    def add_award(self):
        title = simpledialog.askstring("Award", "Enter Award Title:")
        issuer = simpledialog.askstring("Award", "Enter Award Issuer:")
        date = simpledialog.askstring("Award", "Enter Award Date:")
        if title and issuer and date:
            award = Award(title=title, issuer=issuer, date=date)
            self.resume_manager.add_award(award)
            self.award_listbox.insert(tk.END, f"{title} - {issuer} ({date})")

    def add_language(self):
        name = simpledialog.askstring("Language", "Enter Language Name:")
        proficiency = simpledialog.askstring("Language", "Enter Language Proficiency Level:")
        if name and proficiency:
            language = Language(name=name, proficiency=proficiency)
            self.resume_manager.add_language(language)
            self.language_listbox.insert(tk.END, f"{name}: {proficiency}")

    def add_volunteer_experience(self):
        organization = simpledialog.askstring("Volunteer Experience", "Enter Organization Name:")
        role = simpledialog.askstring("Volunteer Experience", "Enter Volunteer Role:")
        start_date = simpledialog.askstring("Volunteer Experience", "Enter Start Date:")
        end_date = simpledialog.askstring("Volunteer Experience", "Enter End Date:")
        responsibilities = simpledialog.askstring("Volunteer Experience", "Enter Responsibilities:")
        if organization and role and start_date and end_date and responsibilities:
            volunteer_experience = VolunteerExperience(organization=organization, role=role, start_date=start_date, end_date=end_date, responsibilities=responsibilities)
            self.resume_manager.add_volunteer_experience(volunteer_experience)
            self.volunteer_listbox.insert(tk.END, f"{organization}: {role} ({start_date} to {end_date})")

    def add_professional_membership(self):
        organization = simpledialog.askstring("Professional Membership", "Enter Organization Name:")
        role = simpledialog.askstring("Professional Membership", "Enter Membership Role:")
        start_date = simpledialog.askstring("Professional Membership", "Enter Start Date:")
        end_date = simpledialog.askstring("Professional Membership", "Enter End Date:")
        if organization and role and start_date and end_date:
            membership = ProfessionalMembership(organization=organization, role=role, start_date=start_date, end_date=end_date)
            self.resume_manager.add_professional_membership(membership)
            self.membership_listbox.insert(tk.END, f"{organization}: {role} ({start_date} to {end_date})")

    def add_publication(self):
        title = simpledialog.askstring("Publication", "Enter Publication Title:")
        author = simpledialog.askstring("Publication", "Enter Author Name:")
        date = simpledialog.askstring("Publication", "Enter Publication Date:")
        if title and author and date:
            publication = Publication(title=title, author=author, date=date)
            self.resume_manager.add_publication(publication)
            self.publication_listbox.insert(tk.END, f"{title} by {author} ({date})")

    def save_resume_to_pdf(self):
        pdf_generator = PDFGenerator(self.resume_manager.resume)
        pdf_generator.generate_pdf()
        messagebox.showinfo("Info", "Resume saved to PDF successfully!")

# Instantiate ResumeManager class
class ResumeManager:
    def __init__(self):
        self.resume = Resume()
        
    def add_skill(self, skill):
        self.resume.skills.append(skill)
        
    def add_certification(self, certification):
        self.resume.certifications.append(certification)
        
    def add_project(self, project):
        self.resume.projects.append(project)
        
    def add_award(self, award):
        self.resume.awards.append(award)
        
    def add_language(self, language):
        self.resume.languages.append(language)
        
    def add_volunteer_experience(self, volunteer_experience):
        self.resume.volunteer_experiences.append(volunteer_experience)
        
    def add_professional_membership(self, membership):
        self.resume.professional_memberships.append(membership)
        
    def add_publication(self, publication):
        self.resume.publications.append(publication)
