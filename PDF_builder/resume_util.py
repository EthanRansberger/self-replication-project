# resume_util.py

class Skill:
    def __init__(self, name):
        self.name = name

class Experience:
    def __init__(self, title, company, start_date, end_date):
        self.title = title
        self.company = company
        self.start_date = start_date
        self.end_date = end_date

class Education:
    def __init__(self, degree, institution, start_date, end_date):
        self.degree = degree
        self.institution = institution
        self.start_date = start_date
        self.end_date = end_date

class Certification:
    def __init__(self, name, issuing_org, issue_date, expiration_date=None):
        self.name = name
        self.issuing_org = issuing_org
        self.issue_date = issue_date
        self.expiration_date = expiration_date

class Project:
    def __init__(self, title, description, technologies, start_date, end_date):
        self.title = title
        self.description = description
        self.technologies = technologies
        self.start_date = start_date
        self.end_date = end_date

class Person:
    def __init__(self, contact_info):
        self.contact_info = contact_info
        self.skills = []
        self.experiences = []
        self.education = []
        self.certifications = []
        self.projects = []

    def add_skill(self, skill_name):
        self.skills.append(Skill(skill_name))

    def add_experience(self, title, company, start_date, end_date):
        self.experiences.append(Experience(title, company, start_date, end_date))

    def add_education(self, degree, institution, start_date, end_date):
        self.education.append(Education(degree, institution, start_date, end_date))

    def add_certification(self, name, issuing_org, issue_date, expiration_date=None):
        self.certifications.append(Certification(name, issuing_org, issue_date, expiration_date))

    def add_project(self, title, description, technologies, start_date, end_date):
        self.projects.append(Project(title, description, technologies, start_date, end_date))

    def generate_resume(self, job_description):
        # Tailor the resume to the job description
        tailored_resume = {
            "contact_info": self.contact_info,
            "skills": [skill.name for skill in self.skills if skill.name in job_description],
            "experiences": [vars(exp) for exp in self.experiences],
            "education": [vars(edu) for edu in self.education],
            "certifications": [vars(cert) for cert in self.certifications],
            "projects": [vars(proj) for proj in self.projects]
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
            person.skills = [Skill(**skill) for skill in data['skills']]
            person.experiences = [Experience(**exp) for exp in data['experiences']]
            person.education = [Education(**edu) for edu in data['education']]
            person.certifications = [Certification(**cert) for cert in data['certifications']]
            person.projects = [Project(**proj) for proj in data['projects']]
            return person
