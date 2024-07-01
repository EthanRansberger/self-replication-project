# resume_util.py

class Resume:
    def __init__(self, name, contact_info, summary):
        self.name = name
        self.contact_info = contact_info
        self.summary = summary
        self.education = []
        self.skills = []
        self.certifications = []
        self.projects = []
        self.awards = []
        self.languages = []
        self.volunteer_experience = []
        self.professional_memberships = []
        self.publications = []

    def add_education(self, education):
        self.education.append(education)

    def add_skill(self, skill):
        self.skills.append(skill)

    def add_certification(self, certification):
        self.certifications.append(certification)

    def add_project(self, project):
        self.projects.append(project)

    def add_award(self, award):
        self.awards.append(award)

    def add_language(self, language):
        self.languages.append(language)

    def add_volunteer_experience(self, volunteer_experience):
        self.volunteer_experience.append(volunteer_experience)

    def add_professional_membership(self, professional_membership):
        self.professional_memberships.append(professional_membership)

    def add_publication(self, publication):
        self.publications.append(publication)

    def save_to_pdf(self, filename):
        # Implementation for saving resume to a PDF
        pass
