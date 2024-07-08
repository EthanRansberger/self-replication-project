# PDF_builder/tests/test_resume_util.py

import unittest
from PDF_builder.src.resume_util import Skill, Experience, Education, Certification, Person

class TestResumeUtil(unittest.TestCase):

    def test_skill(self):
        skill = Skill("Python")
        self.assertEqual(skill.name, "Python")

    def test_experience(self):
        exp = Experience("Developer", "Company", "2020-01", "2020-12", "Developed software")
        self.assertEqual(exp.title, "Developer")
        self.assertEqual(exp.company, "Company")

    def test_education(self):
        edu = Education("Bachelor's", "University", "2015", "2019")
        self.assertEqual(edu.degree, "Bachelor's")
        self.assertEqual(edu.institution, "University")

    def test_certification(self):
        cert = Certification("Cert", "Org", "2020-01")
        self.assertEqual(cert.name, "Cert")
        self.assertEqual(cert.issuing_org, "Org")

    def test_person(self):
        person = Person({"name": "John Doe"})
        self.assertEqual(person.contact_info["name"], "John Doe")

if __name__ == '__main__':
    unittest.main()
