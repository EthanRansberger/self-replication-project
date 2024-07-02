class Skill:
    def __init__(self, name):
        self.name = name

class Experience:
    def __init__(self, title, company, start_date, end_date, description):
        self.title = title
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.description = description

class Education:
    def __init__(self, degree, institution, start_date, end_date, major=None, minor=None, additional_info=None):
        self.degree = degree
        self.institution = institution
        self.start_date = start_date
        self.end_date = end_date
        self.major = major
        self.minor = minor
        self.additional_info = additional_info

class Certification:
    def __init__(self, name, issuing_org, issue_date, expiration_date=None):
        self.name = name
        self.issuing_org = issuing_org
        self.issue_date = issue_date
        self.expiration_date = expiration_date

class Award:
    def __init__(self, name, description, date):
        self.name = name
        self.description = description
        self.date = date

class Project:
    def __init__(self, title, description, technologies, start_date, end_date):
        self.title = title
        self.description = description
        self.technologies = technologies
        self.start_date = start_date
        self.end_date = end_date

class Publication:
    def __init__(self, title, journal, date, description):
        self.title = title
        self.journal = journal
        self.date = date
        self.description = description

class VolunteerExperience:
    def __init__(self, role, organization, start_date, end_date, description):
        self.role = role
        self.organization = organization
        self.start_date = start_date
        self.end_date = end_date
        self.description = description

class Language:
    def __init__(self, name, proficiency):
        self.name = name
        self.proficiency = proficiency

class Summary:
    def __init__(self, text):
        self.text = text

class Job:
    def __init__(self, title, company, description, requirements):
        self.title = title
        self.company = company
        self.description = description
        self.requirements = requirements

class Person:
    def __init__(self, contact_info):
        self.contact_info = contact_info
        self.summary = None
        self.skills = []
        self.experiences = []
        self.education = []
        self.certifications = []
        self.awards = []
        self.projects = []
        self.publications = []
        self.volunteer_experiences = []
        self.languages = []

    def add_skill(self, skill_name):
        self.skills.append(Skill(skill_name))

    def add_experience(self, title, company, start_date, end_date, description):
        self.experiences.append(Experience(title, company, start_date, end_date, description))

    def add_education(self, degree, institution, start_date, end_date, major=None, minor=None, additional_info=None):
        self.education.append(Education(degree, institution, start_date, end_date, major, minor, additional_info))

    def add_certification(self, name, issuing_org, issue_date, expiration_date=None):
        self.certifications.append(Certification(name, issuing_org, issue_date, expiration_date))

    def add_award(self, name, description, date):
        self.awards.append(Award(name, description, date))

    def add_project(self, title, description, technologies, start_date, end_date):
        self.projects.append(Project(title, description, technologies, start_date, end_date))

    def add_publication(self, title, journal, date, description):
        self.publications.append(Publication(title, journal, date, description))

    def add_volunteer_experience(self, role, organization, start_date, end_date, description):
        self.volunteer_experiences.append(VolunteerExperience(role, organization, start_date, end_date, description))

    def add_language(self, name, proficiency):
        self.languages.append(Language(name, proficiency))

    def add_summary(self, text):
        self.summary = Summary(text)

    def generate_resume(self, job_description):
        # Tailor the resume to the job description
        tailored_resume = {
            "contact_info": self.contact_info,
            "summary": self.summary.text if self.summary else None,
            "skills": [skill.name for skill in self.skills if skill.name in job_description],
            "experiences": [vars(exp) for exp in self.experiences],
            "education": [vars(edu) for edu in self.education],
            "certifications": [vars(cert) for cert in self.certifications],
            "awards": [vars(award) for award in self.awards],
            "projects": [vars(proj) for proj in self.projects],
            "publications": [vars(pub) for pub in self.publications],
            "volunteer_experiences": [vars(vol) for vol in self.volunteer_experiences],
            "languages": [vars(lang) for lang in self.languages]
        }
        return tailored_resume

    def save_to_json(self, filename):
        import json
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f, default=lambda o: o.__dict__, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        import json
        with open(filename, 'r') as f:
            data = json.load(f)
            person = cls(data['contact_info'])
            person.summary = Summary(data['summary']['text']) if data['summary'] else None
            person.skills = [Skill(**skill) for skill in data['skills']]
            person.experiences = [Experience(**exp) for exp in data['experiences']]
            person.education = [Education(**edu) for edu in data['education']]
            person.certifications = [Certification(**cert) for cert in data['certifications']]
            person.awards = [Award(**award) for award in data['awards']]
            person.projects = [Project(**proj) for proj in data['projects']]
            person.publications = [Publication(**pub) for pub in data['publications']]
            person.volunteer_experiences = [VolunteerExperience(**vol) for vol in data['volunteer_experiences']]
            person.languages = [Language(**lang) for lang in data['languages']]
            return person

class Resume:
    def __init__(self, person, job):
        self.person = person
        self.job = job

    def tailor_resume(self):
        return self.person.generate_resume(self.job.description)

    def save_resume(self, filename):
        tailored_resume = self.tailor_resume()
        self.person.save_to_json(filename)
        return tailored_resume

    @classmethod
    def load_resume(cls, person_filename, job):
        person = Person.load_from_json(person_filename)
        return cls(person, job)
