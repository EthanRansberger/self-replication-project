# pdf_generator.py

from fpdf import FPDF

class PDFGenerator:
    def __init__(self, resume):
        self.resume = resume

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt=self.resume.name, ln=True, align='C')
        pdf.cell(200, 10, txt=self.resume.contact_info, ln=True, align='C')
        pdf.ln(10)

        pdf.multi_cell(0, 10, txt=self.resume.summary)
        pdf.ln(10)

        if self.resume.skills:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(200, 10, txt="Skills", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for skill in self.resume.skills:
                pdf.cell(200, 10, txt=f"{skill.name}: {skill.level}", ln=True, align='L')
            pdf.ln(10)

        if self.resume.certifications:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(200, 10, txt="Certifications", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for certification in self.resume.certifications:
                pdf.cell(200, 10, txt=f"{certification.title} - {certification.organization} ({certification.date})", ln=True, align='L')
            pdf.ln(10)

        if self.resume.projects:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(200, 10, txt="Projects", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for project in self.resume.projects:
                pdf.cell(200, 10, txt=f"{project.title}: {project.description} ({project.role}, {project.start_date} to {project.end_date})", ln=True, align='L')
            pdf.ln(10)

        if self.resume.awards:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(200, 10, txt="Awards", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for award in self.resume.awards:
                pdf.cell(200, 10, txt=f"{award.title} - {award.issuer} ({award.date})", ln=True, align='L')
            pdf.ln(10)

        if self.resume.languages:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(200, 10, txt="Languages", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for language in self.resume.languages:
                pdf.cell(200, 10, txt=f"{language.name}: {language.proficiency}", ln=True, align='L')
            pdf.ln(10)

        if self.resume.volunteer_experiences:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(200, 10, txt="Volunteer Experiences", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for experience in self.resume.volunteer_experiences:
                pdf.cell(200, 10, txt=f"{experience.organization}: {experience.role} ({experience.start_date} to {experience.end_date})", ln=True, align='L')
            pdf.ln(10)

        if self.resume.professional_memberships:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(200, 10, txt="Professional Memberships", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for membership in self.resume.professional_memberships:
                pdf.cell(200, 10, txt=f"{membership.organization}: {membership.role} ({membership.start_date} to {membership.end_date})", ln=True, align='L')
            pdf.ln(10)

        if self.resume.publications:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(200, 10, txt="Publications", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for publication in self.resume.publications:
                pdf.cell(200, 10, txt=f"{publication.title} by {publication.author} ({publication.date})", ln=True, align='L')
            pdf.ln(10)

        pdf.output("resume.pdf")
