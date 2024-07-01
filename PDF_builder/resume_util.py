# create classes for things like "job_item"
class Job:
    def __init__(self, title, company, start_date, end_date, responsibilities, achievements):
        """
        Initialize a new Job instance.

        :param title: Job title (e.g., 'Data Scientist')
        :param company: Name of the company (e.g., 'Tech Innovations Inc.')
        :param start_date: Start date of the job (e.g., 'Jan 2022')
        :param end_date: End date of the job (e.g., 'Present' or 'Dec 2023')
        :param responsibilities: List of job responsibilities
        :param achievements: List of job achievements
        """
        self.title = title
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.responsibilities = responsibilities
        self.achievements = achievements

    def __str__(self):
        """
        Return a string representation of the Job instance.
        """
        resp_str = '\n'.join(f'- {resp}' for resp in self.responsibilities)
        achv_str = '\n'.join(f'- {achv}' for achv in self.achievements)
        return (f"**{self.title}** at {self.company}\n"
                f"*{self.start_date} - {self.end_date}*\n\n"
                f"Responsibilities:\n{resp_str}\n\n"
                f"Achievements:\n{achv_str}\n")

    def add_responsibility(self, responsibility):
        """
        Add a new responsibility to the job.

        :param responsibility: Responsibility to add
        """
        self.responsibilities.append(responsibility)

    def add_achievement(self, achievement):
        """
        Add a new achievement to the job.

        :param achievement: Achievement to add
        """
        self.achievements.append(achievement)

    def update_end_date(self, end_date):
        """
        Update the end date of the job.

        :param end_date: New end date
        """
        self.end_date = end_date

    def to_dict(self):
        """
        Convert the Job instance to a dictionary.

        :return: A dictionary representation of the job
        """
        return {
            'title': self.title,
            'company': self.company,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'responsibilities': self.responsibilities,
            'achievements': self.achievements
        }
class Education:
    def __init__(self, degree, field_of_study, institution, graduation_year):
        """
        Initialize a new Education instance.

        :param degree: Degree obtained (e.g., 'M.Sc.')
        :param field_of_study: Field of study (e.g., 'Computer Science')
        :param institution: Name of the institution (e.g., 'XYZ University')
        :param graduation_year: Year of graduation (e.g., '2019')
        """
        self.degree = degree
        self.field_of_study = field_of_study
        self.institution = institution
        self.graduation_year = graduation_year

    def __str__(self):
        """
        Return a string representation of the Education instance.
        """
        return (f"{self.degree} in {self.field_of_study}\n"
                f"from {self.institution}\n"
                f"Graduation Year: {self.graduation_year}")

    def update_graduation_year(self, year):
        """
        Update the graduation year of the education.

        :param year: New graduation year
        """
        self.graduation_year = year

    def to_dict(self):
        """
        Convert the Education instance to a dictionary.

        :return: A dictionary representation of the education
        """
        return {
            'degree': self.degree,
            'field_of_study': self.field_of_study,
            'institution': self.institution,
            'graduation_year': self.graduation_year
        }
class Skills:
    def __init__(self, soft_skills=None, hard_skills=None):
        self.soft_skills = soft_skills if soft_skills is not None else []
        self.hard_skills = hard_skills if hard_skills is not None else []

    def __str__(self):
        soft_skills_str = '\n'.join(f'- {skill}' for skill in self.soft_skills)
        hard_skills_str = '\n'.join(f'- {skill}' for skill in self.hard_skills)
        return (f"**Soft Skills:**\n{soft_skills_str}\n\n"
                f"**Hard Skills:**\n{hard_skills_str}")

    def add_soft_skill(self, skill):
        if skill not in self.soft_skills:
            self.soft_skills.append(skill)

    def add_hard_skill(self, skill):
        if skill not in self.hard_skills:
            self.hard_skills.append(skill)

    def remove_soft_skill(self, skill):
        if skill in self.soft_skills:
            self.soft_skills.remove(skill)

    def remove_hard_skill(self, skill):
        if skill in self.hard_skills:
            self.hard_skills.remove(skill)

    def to_dict(self):
        return {
            'soft_skills': self.soft_skills,
            'hard_skills': self.hard_skills
        }
class Certification:
    def __init__(self, name, issuing_organization, issue_date, expiration_date=None):
        """
        Initialize a new Certification instance.

        :param name: Name of the certification (e.g., 'Certified Data Scientist')
        :param issuing_organization: Organization that issued the certification (e.g., 'Data Science Institute')
        :param issue_date: Date the certification was issued (e.g., '2022-01-15')
        :param expiration_date: Date the certification expires (optional, e.g., '2025-01-15')
        """
        self.name = name
        self.issuing_organization = issuing_organization
        self.issue_date = issue_date
        self.expiration_date = expiration_date

    def __str__(self):
        exp_date = self.expiration_date if self.expiration_date else 'N/A'
        return (f"**{self.name}**\n"
                f"Issued by: {self.issuing_organization}\n"
                f"Issue Date: {self.issue_date}\n"
                f"Expiration Date: {exp_date}")

    def to_dict(self):
        return {
            'name': self.name,
            'issuing_organization': self.issuing_organization,
            'issue_date': self.issue_date,
            'expiration_date': self.expiration_date
        }
class Project:
    def __init__(self, title, description, technologies, start_date, end_date):
        """
        Initialize a new Project instance.

        :param title: Title of the project (e.g., 'Customer Churn Prediction')
        :param description: Brief description of the project
        :param technologies: Technologies used (e.g., ['Python', 'Scikit-learn'])
        :param start_date: Start date of the project (e.g., '2022-01-01')
        :param end_date: End date of the project (e.g., '2022-06-30')
        """
        self.title = title
        self.description = description
        self.technologies = technologies
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        tech_str = ', '.join(self.technologies)
        return (f"**{self.title}**\n"
                f"*{self.start_date} - {self.end_date}*\n\n"
                f"{self.description}\n\n"
                f"Technologies Used: {tech_str}")

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'technologies': self.technologies,
            'start_date': self.start_date,
            'end_date': self.end_date
        }
class Award:
    def __init__(self, title, awarding_organization, date, description):
        """
        Initialize a new Award instance.

        :param title: Title of the award (e.g., 'Employee of the Month')
        :param awarding_organization: Organization that gave the award (e.g., 'Tech Innovations Inc.')
        :param date: Date of the award (e.g., '2023-03-01')
        :param description: Description of the award or reason for receiving it
        """
        self.title = title
        self.awarding_organization = awarding_organization
        self.date = date
        self.description = description

    def __str__(self):
        return (f"**{self.title}**\n"
                f"Awarded by: {self.awarding_organization}\n"
                f"Date: {self.date}\n"
                f"Description: {self.description}")

    def to_dict(self):
        return {
            'title': self.title,
            'awarding_organization': self.awarding_organization,
            'date': self.date,
            'description': self.description
        }
class Language:
    def __init__(self, name, proficiency):
        """
        Initialize a new Language instance.

        :param name: Name of the language (e.g., 'Spanish')
        :param proficiency: Proficiency level (e.g., 'Fluent', 'Intermediate', 'Basic')
        """
        self.name = name
        self.proficiency = proficiency

    def __str__(self):
        return f"**{self.name}**: {self.proficiency}"

    def to_dict(self):
        return {
            'name': self.name,
            'proficiency': self.proficiency
        }
class VolunteerExperience:
    def __init__(self, role, organization, start_date, end_date, responsibilities):
        """
        Initialize a new VolunteerExperience instance.

        :param role: Role in the volunteer position (e.g., 'Volunteer Data Analyst')
        :param organization: Organization where the volunteer work was done (e.g., 'Local Food Bank')
        :param start_date: Start date of the volunteer experience (e.g., '2021-01-01')
        :param end_date: End date of the volunteer experience (e.g., '2021-12-31')
        :param responsibilities: List of responsibilities (e.g., ['Analyzed data trends', 'Created reports'])
        """
        self.role = role
        self.organization = organization
        self.start_date = start_date
        self.end_date = end_date
        self.responsibilities = responsibilities

    def __str__(self):
        resp_str = '\n'.join(f'- {resp}' for resp in self.responsibilities)
        return (f"**{self.role}** at {self.organization}\n"
                f"*{self.start_date} - {self.end_date}*\n\n"
                f"Responsibilities:\n{resp_str}")

    def to_dict(self):
        return {
            'role': self.role,
            'organization': self.organization,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'responsibilities': self.responsibilities
        }
class ProfessionalMembership:
    def __init__(self, organization, membership_type, join_date, expiration_date=None):
        """
        Initialize a new ProfessionalMembership instance.

        :param organization: Organization of the membership (e.g., 'Data Science Association')
        :param membership_type: Type of membership (e.g., 'Full Member', 'Associate Member')
        :param join_date: Date of joining (e.g., '2022-05-01')
        :param expiration_date: Date of expiration (optional, e.g., '2025-05-01')
        """
        self.organization = organization
        self.membership_type = membership_type
        self.join_date = join_date
        self.expiration_date = expiration_date

    def __str__(self):
        exp_date = self.expiration_date if self.expiration_date else 'N/A'
        return (f"**{self.organization}**\n"
                f"Membership Type: {self.membership_type}\n"
                f"Join Date: {self.join_date}\n"
                f"Expiration Date: {exp_date}")

    def to_dict(self):
        return {
            'organization': self.organization,
            'membership_type': self.membership_type,
            'join_date': self.join_date,
            'expiration_date': self.expiration_date
        }
class Publication:
    def __init__(self, title, journal, date, link=None):
        """
        Initialize a new Publication instance.

        :param title: Title of the publication (e.g., 'A Study on Machine Learning Algorithms')
        :param journal: Journal or conference where it was published (e.g., 'Journal of Machine Learning')
        :param date: Date of publication (e.g., '2023-04-15')
        :param link: Optional link to the publication
        """
        self.title = title
        self.journal = journal
        self.date = date
        self.link = link

    def __str__(self):
        link_str = f" [Link]({self.link})" if self.link else ''
        return (f"**{self.title}**\n"
                f"Published in: {self.journal}\n"
                f"Date: {self.date}{link_str}")

    def to_dict(self):
        return {
            'title': self.title,
            'journal': self.journal,
            'date': self.date,
            'link': self.link
        }
