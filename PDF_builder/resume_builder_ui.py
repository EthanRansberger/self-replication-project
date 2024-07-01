import tkinter as tk
from tkinter import ttk, messagebox
from resume_util import Job, Education, Skills, Certification, Project, Award, Language, VolunteerExperience, ProfessionalMembership, Publication
from resume import Resume
class ResumeBuilderUI:
    def __init__(self, root):
        self.resume = Resume(
            name='',
            contact_info='',
            summary=''
        )

        self.job_bank = []

        self.root = root
        self.root.title("Resume Builder")
        self.create_widgets()

    def create_widgets(self):
        # Name
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry = tk.Entry(self.root, width=50)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Contact Info
        tk.Label(self.root, text="Contact Info:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.contact_info_entry = tk.Entry(self.root, width=50)
        self.contact_info_entry.grid(row=1, column=1, padx=10, pady=5)

        # Summary
        tk.Label(self.root, text="Professional Summary:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.summary_text = tk.Text(self.root, height=5, width=50)
        self.summary_text.grid(row=2, column=1, padx=10, pady=5)

        # Job Bank Management
        tk.Button(self.root, text="Manage Job Bank", command=self.manage_job_bank).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Add Job", command=self.add_job_from_bank).grid(row=3, column=1, padx=10, pady=10)

        # Add Education Button
        self.add_education_button = tk.Button(self.root, text="Add Education", command=self.add_education_form)
        self.add_education_button.grid(row=4, column=0, padx=10, pady=10)

        # Save Resume Button
        self.save_resume_button = tk.Button(self.root, text="Save Resume", command=self.save_resume)
        self.save_resume_button.grid(row=4, column=1, padx=10, pady=10)

    def add_job_from_bank(self):
        form_window = tk.Toplevel(self.root)
        form_window.title("Add Job from Bank")

        tk.Label(form_window, text="Select Job:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        job_selector = ttk.Combobox(form_window, values=[job['title'] for job in self.job_bank], width=40)
        job_selector.grid(row=0, column=1, padx=10, pady=5)

        def add_selected_job():
            selected_job_title = job_selector.get()
            job = next((job for job in self.job_bank if job['title'] == selected_job_title), None)
            if job:
                job_instance = Job(
                    title=job['title'],
                    company=job['company'],
                    start_date=job['start_date'],
                    end_date=job['end_date'],
                    responsibilities=job['responsibilities'],
                    achievements=job['achievements']
                )
                self.resume.add_job(job_instance)
                form_window.destroy()
                messagebox.showinfo("Info", "Job added successfully!")
            else:
                messagebox.showerror("Error", "No job selected!")

        tk.Button(form_window, text="Add Selected Job", command=add_selected_job).grid(row=1, column=0, columnspan=2, pady=10)

    def manage_job_bank(self):
        form_window = tk.Toplevel(self.root)
        form_window.title("Manage Job Bank")

        tk.Label(form_window, text="Title:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        title_entry = tk.Entry(form_window, width=40)
        title_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_window, text="Company:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        company_entry = tk.Entry(form_window, width=40)
        company_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_window, text="Start Date:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        start_date_entry = tk.Entry(form_window, width=40)
        start_date_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_window, text="End Date:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        end_date_entry = tk.Entry(form_window, width=40)
        end_date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(form_window, text="Responsibilities (comma-separated):").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        responsibilities_entry = tk.Entry(form_window, width=40)
        responsibilities_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(form_window, text="Achievements (comma-separated):").grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        achievements_entry = tk.Entry(form_window, width=40)
        achievements_entry.grid(row=5, column=1, padx=10, pady=5)

        def save_job_to_bank():
            job = {
                'title': title_entry.get(),
                'company': company_entry.get(),
                'start_date': start_date_entry.get(),
                'end_date': end_date_entry.get(),
                'responsibilities': responsibilities_entry.get().split(','),
                'achievements': achievements_entry.get().split(',')
            }
            self.job_bank.append(job)
            form_window.destroy()
            messagebox.showinfo("Info", "Job added to bank successfully!")

        tk.Button(form_window, text="Save Job to Bank", command=save_job_to_bank).grid(row=6, column=0, columnspan=2, pady=10)

    def add_education_form(self):
        form_window = tk.Toplevel(self.root)
        form_window.title("Add Education")

        tk.Label(form_window, text="Degree:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        degree_entry = tk.Entry(form_window, width=40)
        degree_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_window, text="Field of Study:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        field_of_study_entry = tk.Entry(form_window, width=40)
        field_of_study_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_window, text="Institution:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        institution_entry = tk.Entry(form_window, width=40)
        institution_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_window, text="Graduation Year:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        graduation_year_entry = tk.Entry(form_window, width=40)
        graduation_year_entry.grid(row=3, column=1, padx=10, pady=5)

        def save_education():
            education = Education(
                degree=degree_entry.get(),
                field_of_study=field_of_study_entry.get(),
                institution=institution_entry.get(),
                graduation_year=graduation_year_entry.get()
            )
            self.resume.add_education(education)
            form_window.destroy()
            messagebox.showinfo("Info", "Education added successfully!")

        tk.Button(form_window, text="Save Education", command=save_education).grid(row=4, column=0, columnspan=2, pady=10)

    def save_resume(self):
        md_file_path = 'resume.md'
        pdf_file_path = 'resume.pdf'
        self.resume.name = self.name_entry.get()
        self.resume.contact_info = self.contact_info_entry.get()
        self.resume.summary = self.summary_text.get("1.0", tk.END).strip()
        self.resume.generate_resume(md_file_path, pdf_file_path)

        messagebox.showinfo("Info", f"Resume saved to {pdf_file_path}.")

# Create the main window
root = tk.Tk()
app = ResumeBuilderUI(root)
root.mainloop()
