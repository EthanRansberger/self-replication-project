# resume.py

from resume_util import Job, Education, Skills, Certification, Project, Award, Language, VolunteerExperience, ProfessionalMembership, Publication

class Resume:
    def __init__(self, name, contact_info, summary):
        self.name = name
        self.contact_info = contact_info
        self.summary = summary
        self.jobs = []
        self.educations = []
        self.skills = Skills()
        self.certifications = []
        self.projects = []
        self.awards = []
        self.languages = []
        self.volunteer_experiences = []
        self.professional_memberships = []
        self.publications = []

    def add_job(self, job):
        self.jobs.append(job)

    def add_education(self, education):
        self.educations.append(education)

    def add_certification(self, certification):
        self.certifications.append(certification)

    def add_project(self, project):
        self.projects.append(project)

    def add_award(self, award):
        self.awards.append(award)

    def add_language(self, language):
        self.languages.append(language)

    def add_volunteer_experience(self, volunteer_experience):
        self.volunteer_experiences.append(volunteer_experience)

    def add_professional_membership(self, membership):
        self.professional_memberships.append(membership)

    def add_publication(self, publication):
        self.publications.append(publication)

    def generate_resume(self, md_file_path, pdf_file_path):
        with open(md_file_path, 'w') as file:
            file.write(f"# {self.name}\n")
            file.write(f"**Contact Info:** {self.contact_info}\n\n")
            file.write(f"## Professional Summary\n{self.summary}\n\n")

            if self.jobs:
                file.write("## Experience\n")
                for job in self.jobs:
                    file.write(f"**{job.title}** at {job.company} ({job.start_date} - {job.end_date})\n")
                    file.write("### Responsibilities:\n")
                    for responsibility in job.responsibilities:
                        file.write(f"- {responsibility}\n")
                    file.write("### Achievements:\n")
                    for achievement in job.achievements:
                        file.write(f"- {achievement}\n")
                    file.write("\n")

            if self.educations:
                file.write("## Education\n")
                for education in self.educations:
                    file.write(f"{education.degree} in {education.field_of_study} from {education.institution} ({education.graduation_year})\n")
                file.write("\n")

            if self.skills.hard_skills or self.skills.soft_skills:
                file.write("## Skills\n")
                if self.skills.hard_skills:
                    file.write(f"**Hard Skills:** {', '.join(self.skills.hard_skills)}\n")
                if self.skills.soft_skills:
                    file.write(f"**Soft Skills:** {', '.join(self.skills.soft_skills)}\n")
                file.write("\n")

            if self.certifications:
                file.write("## Certifications\n")
                for cert in self.certifications:
                    file.write(f"{cert.name} from {cert.issuing_organization} ({cert.issue_date} - {cert.expiration_date if cert.expiration_date else 'Present'})\n")
                file.write("\n")

            if self.projects:
                file.write("## Projects\n")
                for project in self.projects:
                    file.write(f"**{project.title}** ({project.date}): {project.description} using {', '.join(project.technologies)}\n")
                file.write("\n")

            if self.awards:
                file.write("## Awards\n")
                for award in self.awards:
                    file.write(f"{award.title} from {award.awarding_organization} ({award.date}): {award.description}\n")
                file.write("\n")

            if self.languages:
                file.write("## Languages\n")
                for lang in self.languages:
                    file.write(f"{lang.language} - {lang.proficiency_level}\n")
                file.write("\n")

            if self.volunteer_experiences:
                file.write("## Volunteer Experience\n")
                for exp in self.volunteer_experiences:
                    file.write(f"**{exp.role}** at {exp.organization} ({exp.start_date} - {exp.end_date})\n")
                    file.write("### Responsibilities:\n")
                    for responsibility in exp.responsibilities:
                        file.write(f"- {responsibility}\n")
                    file.write("\n")

            if self.professional_memberships:
                file.write("## Professional Memberships\n")
                for membership in self.professional_memberships:
                    file.write(f"{membership.membership_type} membership at {membership.organization} ({membership.start_date} - {membership.end_date if membership.end_date else 'Present'})\n")
                file.write("\n")

            if self.publications:
                file.write("## Publications\n")
                for pub in self.publications:
                    file.write(f"{pub.title} published in {pub.journal} ({pub.date}) - Link: {pub.link if pub.link else 'N/A'}\n")
                file.write("\n")
