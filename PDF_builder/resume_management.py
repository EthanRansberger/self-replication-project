import json
import resume_util

class ResumeManager:
    def __init__(self):
        self.resume = resume_util.Resume()

    def load_resume_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            
            # Correct JSON data if necessary
            data = self.correct_json_data(data)
            
            # Load data into the resume object
            self.resume = resume_util.Resume(
                contact_info=data.get('contact_info', {}),
                skills=[resume_util.Skill(**skill) for skill in data.get('skills', [])],
                experience=[resume_util.Experience(**exp) for exp in data.get('experience', [])],
                education=[resume_util.Education(**edu) for edu in data.get('education', [])],
                certifications=[resume_util.Certification(**cert) for cert in data.get('certifications', [])],
                projects=[resume_util.Project(**proj) for proj in data.get('projects', [])]
            )
        except json.JSONDecodeError:
            print("Error decoding JSON file. Ensure the JSON file is correctly formatted.")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Please provide a valid JSON file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def correct_json_data(self, data):
        # Implement your JSON data correction logic here
        for key, value in data.items():
            if isinstance(value, str) and value.startswith("{"):
                try:
                    data[key] = json.loads(value)  # Attempt to parse as JSON
                except json.JSONDecodeError:
                    continue  # If parsing fails, leave the data as-is
        return data

    def save_resume_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.resume.to_dict(), file, indent=4)

    def add_skill(self, name):
        self.resume.add_skill(resume_util.Skill(name))

    def add_experience(self, job_title, company, start_date, end_date):
        self.resume.add_experience(resume_util.Experience(job_title, company, start_date, end_date))

    def add_education(self, degree, institution, start_date, end_date):
        self.resume.add_education(resume_util.Education(degree, institution, start_date, end_date))

    def add_certification(self, name, issuing_organization, issue_date, expiration_date=None):
        self.resume.add_certification(resume_util.Certification(name, issuing_organization, issue_date, expiration_date))

    def add_project(self, title, description, technologies, start_date, end_date):
        self.resume.add_project(resume_util.Project(title, description, technologies, start_date, end_date))
