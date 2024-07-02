from fpdf import FPDF  # Make sure fpdf is installed: pip install fpdf

class PDFGenerator:
    def __init__(self, resume, file_path):
        self.resume = resume
        self.file_path = file_path

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Resume", ln=True, align='C')
        pdf.ln(10)

        # Skills
        if self.resume.skills:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Skills", ln=True)
            pdf.set_font("Arial", size=12)
            for skill in self.resume.skills:
                pdf.cell(200, 10, txt=skill, ln=True)
            pdf.ln(10)

        # Awards
        if self.resume.awards:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Awards", ln=True)
            pdf.set_font("Arial", size=12)
            for award in self.resume.awards:
                pdf.cell(200, 10, txt=f"{award.title} - {award.organization} ({award.date})", ln=True)
            pdf.ln(10)

        # Languages
        if self.resume.languages:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Languages", ln=True)
            pdf.set_font("Arial", size=12)
            for language in self.resume.languages:
                pdf.cell(200, 10, txt=f"{language.name} - {language.proficiency}", ln=True)
            pdf.ln(10)

        # Volunteer Experiences
        if self.resume.volunteer_experiences:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Volunteer Experiences", ln=True)
            pdf.set_font("Arial", size=12)
            for experience in self.resume.volunteer_experiences:
                pdf.cell(200, 10, txt=f"{experience.organization} - {experience.role} ({experience.start_date} to {experience.end_date})", ln=True)
                pdf.multi_cell(0, 10, txt=experience.description)
            pdf.ln(10)

        # Professional Memberships
        if self.resume.professional_memberships:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Professional Memberships", ln=True)
            pdf.set_font("Arial", size=12)
            for membership in self.resume.professional_memberships:
                pdf.cell(200, 10, txt=f"{membership.organization} - {membership.role} ({membership.start_date} to {membership.end_date})", ln=True)
            pdf.ln(10)

        # Publications
        if self.resume.publications:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Publications", ln=True)
            pdf.set_font("Arial", size=12)
            for publication in self.resume.publications:
                pdf.cell(200, 10, txt=f"{publication.title} - {publication.publication_date}", ln=True)
                pdf.multi_cell(0, 10, txt=publication.details)
            pdf.ln(10)

        # Job Experiences
        if self.resume.job_experiences:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Job Experiences", ln=True)
            pdf.set_font("Arial", size=12)
            for experience in self.resume.job_experiences:
                pdf.cell(200, 10, txt=f"{experience.company} - {experience.role} ({experience.start_date} to {experience.end_date})", ln=True)
                pdf.multi_cell(0, 10, txt=experience.description)
            pdf.ln(10)

        pdf.output(self.file_path)
