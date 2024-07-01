# resume_util.py

class Job:
    def __init__(self, title, company, start_date, end_date, responsibilities=None, achievements=None):
        self.title = title
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.responsibilities = responsibilities if responsibilities is not None else []
        self.achievements = achievements if achievements is not None else []

    def add_responsibility(self, responsibility):
        self.responsibilities.append(responsibility)

    def add_achievement(self, achievement):
        self.achievements.append(achievement)

    def __repr__(self):
        return f"{self.title} at {self.company} ({self.start_date} - {self.end_date})"

class Education:
    def __init__(self, degree, field_of_study, institution, graduation_year):
        self.degree = degree
        self.field_of_study = field_of_study
        self.institution = institution
        self.graduation_year = graduation_year

    def __repr__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution} ({self.graduation_year})"

class Skills:
    def __init__(self):
        self.hard_skills = []
        self.soft_skills = []

    def add_skill(self, skill, skill_type):
        if skill_type == 'hard':
            self.hard_skills.append(skill)
        elif skill_type == 'soft':
            self.soft_skills.append(skill)
        else:
            raise ValueError("Skill type must be 'hard' or 'soft'")

    def __repr__(self):
        return f"Hard Skills: {', '.join(self.hard_skills)} | Soft Skills: {', '.join(self.soft_skills)}"

class Certification:
    def __init__(self, name, issuing_organization, issue_date, expiration_date=None):
        self.name = name
        self.issuing_organization = issuing_organization
        self.issue_date = issue_date
        self.expiration_date = expiration_date

    def __repr__(self):
        return f"{self.name} from {self.issuing_organization} ({self.issue_date} - {self.expiration_date if self.expiration_date else 'Present'})"

class Project:
    def __init__(self, title, description, technologies, date):
        self.title = title
        self.description = description
        self.technologies = technologies
        self.date = date

    def __repr__(self):
        return f"{self.title} ({self.date}): {self.description} using {', '.join(self.technologies)}"

class Award:
    def __init__(self, title, awarding_organization, date, description):
        self.title = title
        self.awarding_organization = awarding_organization
        self.date = date
        self.description = description

    def __repr__(self):
        return f"{self.title} from {self.awarding_organization} ({self.date}): {self.description}"

class Language:
    def __init__(self, language, proficiency_level):
        self.language = language
        self.proficiency_level = proficiency_level

    def __repr__(self):
        return f"{self.language} - {self.proficiency_level}"

class VolunteerExperience:
    def __init__(self, role, organization, start_date, end_date, responsibilities=None):
        self.role = role
        self.organization = organization
        self.start_date = start_date
        self.end_date = end_date
        self.responsibilities = responsibilities if responsibilities is not None else []

    def add_responsibility(self, responsibility):
        self.responsibilities.append(responsibility)

    def __repr__(self):
        return f"{self.role} at {self.organization} ({self.start_date} - {self.end_date})"

class ProfessionalMembership:
    def __init__(self, organization, membership_type, start_date, end_date=None):
        self.organization = organization
        self.membership_type = membership_type
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"{self.membership_type} membership at {self.organization} ({self.start_date} - {self.end_date if self.end_date else 'Present'})"

class Publication:
    def __init__(self, title, journal, date, link=None):
        self.title = title
        self.journal = journal
        self.date = date
        self.link = link

    def __repr__(self):
        return f"{self.title} published in {self.journal} ({self.date}) - Link: {self.link if self.link else 'N/A'}"
