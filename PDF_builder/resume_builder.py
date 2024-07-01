import markdown2
import pdfkit
from resume_util import Job, Education, Skills, Certification, Project, Award, Language, VolunteerExperience, ProfessionalMembership, Publication
class Resume:
    def __init__(self, name, contact_info, summary):
        """
        Initialize a new Resume instance.

        :param name: Name of the person (e.g., 'John Doe')
        :param contact_info: Contact information (e.g., 'Email: john.doe@example.com | Phone: (123) 456-7890')
        :param summary: Professional summary (e.g., 'Data Scientist with 5+ years of experience...')
        """
        self.name = name
        self.contact_info = contact_info
        self.summary = summary
        self.jobs = []
        self.education_list = []
        self.skills = Skills()
        self.certifications = []
        self.projects = []
        self.awards = []
        self.languages = []
        self.volunteer_experiences = []
        self.professional_memberships = []
        self.publications = []

    def add_job(self, job):
        """
        Add a job to the resume.

        :param job: An instance of the Job class
        """
        self.jobs.append(job)
    
    def add_education(self, education):
        """
        Add an education entry to the resume.

        :param education: An instance of the Education class
        """
        self.education_list.append(education)

    def set_skills(self, soft_skills=None, hard_skills=None):
        """
        Set the skills for the resume.

        :param soft_skills: List of soft skills
        :param hard_skills: List of hard skills
        """
        self.skills = Skills(soft_skills, hard_skills)
    
    def add_certification(self, certification):
        """
        Add a certification to the resume.

        :param certification: An instance of the Certification class
        """
        self.certifications.append(certification)

    def add_project(self, project):
        """
        Add a project to the resume.

        :param project: An instance of the Project class
        """
        self.projects.append(project)

    def add_award(self, award):
        """
        Add an award to the resume.

        :param award: An instance of the Award class
        """
        self.awards.append(award)

    def add_language(self, language):
        """
        Add a language to the resume.

        :param language: An instance of the Language class
        """
        self.languages.append(language)

    def add_volunteer_experience(self, volunteer_experience):
        """
        Add a volunteer experience to the resume.

        :param volunteer_experience: An instance of the VolunteerExperience class
        """
        self.volunteer_experiences.append(volunteer_experience)

    def add_professional_membership(self, professional_membership):
        """
        Add a professional membership to the resume.

        :param professional_membership: An instance of the ProfessionalMembership class
        """
        self.professional_memberships.append(professional_membership)

    def add_publication(self, publication):
        """
        Add a publication to the resume.

        :param publication: An instance of the Publication class
        """
        self.publications.append(publication)

    def __str__(self):
        """
        Return a Markdown string representation of the Resume instance.
        """
        job_experience = '\n\n'.join(str(job) for job in self.jobs)
        education = '\n\n'.join(str(edu) for edu in self.education_list)
        skills = str(self.skills)
        certifications = '\n\n'.join(str(cert) for cert in self.certifications)
        projects = '\n\n'.join(str(proj) for proj in self.projects)
        awards = '\n\n'.join(str(award) for award in self.awards)
        languages = '\n\n'.join(str(lang) for lang in self.languages)
        volunteer_experiences = '\n\n'.join(str(ve) for ve in self.volunteer_experiences)
        professional_memberships = '\n\n'.join(str(pm) for pm in self.professional_memberships)
        publications = '\n\n'.join(str(pub) for pub in self.publications)

        return (f"# {self.name}\n\n"
                f"{self.contact_info}\n\n"
                f"## Professional Summary\n\n"
                f"{self.summary}\n\n"
                f"## Work Experience\n\n"
                f"{job_experience}\n\n"
                f"## Education\n\n"
                f"{education}\n\n"
                f"## Skills\n\n"
                f"{skills}\n\n"
                f"## Certifications\n\n"
                f"{certifications}\n\n"
                f"## Projects\n\n"
                f"{projects}\n\n"
                f"## Awards\n\n"
                f"{awards}\n\n"
                f"## Languages\n\n"
                f"{languages}\n\n"
                f"## Volunteer Experience\n\n"
                f"{volunteer_experiences}\n\n"
                f"## Professional Memberships\n\n"
                f"{professional_memberships}\n\n"
                f"## Publications\n\n"
                f"{publications}")

    def to_dict(self):
        """
        Convert the Resume instance to a dictionary.

        :return: A dictionary representation of the resume
        """
        return {
            'name': self.name,
            'contact_info': self.contact_info,
            'summary': self.summary,
            'jobs': [job.to_dict() for job in self.jobs],
            'education': [edu.to_dict() for edu in self.education_list],
            'skills': self.skills.to_dict(),
            'certifications': [cert.to_dict() for cert in self.certifications],
            'projects': [proj.to_dict() for proj in self.projects],
            'awards': [award.to_dict() for award in self.awards],
            'languages': [lang.to_dict() for lang in self.languages],
            'volunteer_experiences': [ve.to_dict() for ve in self.volunteer_experiences],
            'professional_memberships': [pm.to_dict() for pm in self.professional_memberships],
            'publications': [pub.to_dict() for pub in self.publications]
        }

    def generate_markdown(self):
        """
        Generate the Markdown text for the resume.

        :return: A Markdown string of the resume
        """
        return str(self)

    def save_markdown(self, file_path):
        """
        Save the Markdown text to a file.

        :param file_path: Path to the Markdown file
        """
        with open(file_path, 'w') as file:
            file.write(self.generate_markdown())

    def convert_to_pdf(self, md_file_path, pdf_file_path):
        """
        Convert the Markdown file to a PDF file.

        :param md_file_path: Path to the Markdown file
        :param pdf_file_path: Path to the output PDF file
        """
        with open(md_file_path, 'r') as file:
            markdown_text = file.read()
        
        html_text = markdown2.markdown(markdown_text)
        pdfkit.from_string(html_text, pdf_file_path)

    def generate_resume(self, md_file_path, pdf_file_path):
        """
        Generate the resume in Markdown format and convert it to a PDF file.

        :param md_file_path: Path to the Markdown file
        :param pdf_file_path: Path to the output PDF file
        """
        self.save_markdown(md_file_path)
        self.convert_to_pdf(md_file_path, pdf_file_path)
        print(f"Resume has been updated and saved to {pdf_file_path}.")
