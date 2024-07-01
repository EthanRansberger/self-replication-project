# resume_util.py

class Resume:
    def __init__(self):
        self.name = ""
        self.contact_info = ""
        self.summary = ""
        self.skills = []
        self.certifications = []
        self.projects = []
        self.awards = []
        self.languages = []
        self.volunteer_experiences = []
        self.professional_memberships = []
        self.publications = []

class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Certification:
    def __init__(self, title, organization, date):
        self.title = title
        self.organization = organization
        self.date = date

class Project:
    def __init__(self, title, description, role, start_date, end_date):
        self.title = title
        self.description = description
        self.role = role
        self.start_date = start_date
        self.end_date = end_date

class Award:
    def __init__(self, title, issuer, date):
        self.title = title
        self.issuer = issuer
        self.date = date

class Language:
    def __init__(self, name, proficiency):
        self.name = name
        self.proficiency = proficiency

class VolunteerExperience:
    def __init__(self, organization, role, start_date, end_date, responsibilities):
        self.organization = organization
        self.role = role
        self.start_date = start_date
        self.end_date = end_date
        self.responsibilities = responsibilities

class ProfessionalMembership:
    def __init__(self, organization, role, start_date, end_date):
        self.organization = organization
        self.role = role
        self.start_date = start_date
        self.end_date = end_date

class Publication:
    def __init__(self, title, authors, publication_date):
        self.title = title
        self.authors = authors
        self.publication_date = publication_date

class JobBank:
    def __init__(self):
        self.jobs = []

    def add_job(self, title, description, skills):
        self.jobs.append({"title": title, "description": description, "skills": skills})
