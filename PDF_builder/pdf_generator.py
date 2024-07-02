# pdf_generator.py

from fpdf import FPDF  # Make sure fpdf is installed: pip install fpdf
from resume_util import format_for_ats

class PDFGenerator:
    def __init__(self, person, file_path, platform="Taleo"):
        self.person = person
        self.file_path = file_path
        self.platform = platform

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()

        # Format content for ATS
        content = self.get_resume_content()
        formatted_content, font = format_for_ats(content, self.platform)
        
        pdf.set_font(font, size=12)

        for line in formatted_content:
            pdf.multi_cell(0, 10, txt=line)

        pdf.output(self.file_path)

    def get_resume_content(self):
        # Convert the person's resume data to a dictionary format for easier processing
        resume_data = {
            "Contact Information": [f"{key}: {value}" for key, value in self.person.contact_info.items()],
            "Summary": [self.person.summary.text] if self.person.summary else [],
            "Work Experience": [f"{exp.title} at {exp.company} ({exp.start_date} to {exp.end_date})\n{exp.description}" for exp in self.person.experiences],
            "Education": [f"{edu.degree} in {edu.major} from {edu.institution} ({edu.start_date} to {edu.end_date})" for edu in self.person.education],
            "Skills": [skill.name for skill in self.person.skills],
            "Certifications": [f"{cert.name}, {cert.issuing_org} (Issued: {cert.issue_date}, Expires: {cert.expiration_date or 'N/A'})" for cert in self.person.certifications],
            "Projects": [f"{proj.title} ({proj.start_date} to {proj.end_date})\n{proj.description}\nTechnologies used: {proj.technologies}" for proj in self.person.projects],
            "Awards": [f"{award.name} ({award.date})\n{award.description}" for award in self.person.awards],
            "Publications": [f"{pub.title} in {pub.journal} ({pub.date})\n{pub.description}" for pub in self.person.publications],
            "Volunteer Experiences": [f"{vol.role} at {vol.organization} ({vol.start_date} to {vol.end_date})\n{vol.description}" for vol in self.person.volunteer_experiences],
            "Languages": [f"{lang.name}: {lang.proficiency}" for lang in self.person.languages],
        }

        return resume_data
