from fpdf import FPDF  # Make sure fpdf is installed: pip install fpdf

class PDFGenerator:
    def __init__(self, person, file_path):
        self.person = person
        self.file_path = file_path

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Resume", ln=True, align='C')
        pdf.ln(10)

        # Contact Info
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(200, 10, txt="Contact Info", ln=True)
        pdf.set_font("Arial", size=12)
        for field, value in self.person.contact_info.items():
            pdf.cell(200, 10, txt=f"{field}: {value}", ln=True)
        pdf.ln(10)

        # Summary
        if self.person.summary:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Summary", ln=True)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=self.person.summary.text)
            pdf.ln(10)

        # Skills
        if self.person.skills:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Skills", ln=True)
            pdf.set_font("Arial", size=12)
            for skill in self.person.skills:
                pdf.cell(200, 10, txt=skill.name, ln=True)
            pdf.ln(10)

        # Experiences
        if self.person.experiences:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Experiences", ln=True)
            pdf.set_font("Arial", size=12)
            for exp in self.person.experiences:
                pdf.cell(200, 10, txt=f"{exp.title} at {exp.company} ({exp.start_date} to {exp.end_date})", ln=True)
                pdf.multi_cell(0, 10, txt=exp.description)
            pdf.ln(10)

        # Education
        if self.person.education:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Education", ln=True)
            pdf.set_font("Arial", size=12)
            for edu in self.person.education:
                edu_text = f"{edu.degree} in {edu.major}" if edu.major else edu.degree
                pdf.cell(200, 10, txt=f"{edu_text}, {edu.institution} ({edu.start_date} to {edu.end_date})", ln=True)
                if edu.minor:
                    pdf.cell(200, 10, txt=f"Minor: {edu.minor}", ln=True)
                if edu.additional_info:
                    pdf.multi_cell(0, 10, txt=edu.additional_info)
            pdf.ln(10)

        # Certifications
        if self.person.certifications:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Certifications", ln=True)
            pdf.set_font("Arial", size=12)
            for cert in self.person.certifications:
                cert_text = f"{cert.name}, {cert.issuing_org} (Issued: {cert.issue_date}"
                if cert.expiration_date:
                    cert_text += f", Expires: {cert.expiration_date})"
                else:
                    cert_text += ")"
                pdf.cell(200, 10, txt=cert_text, ln=True)
            pdf.ln(10)

        # Awards
        if self.person.awards:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Awards", ln=True)
            pdf.set_font("Arial", size=12)
            for award in self.person.awards:
                pdf.cell(200, 10, txt=f"{award.name} ({award.date})", ln=True)
                pdf.multi_cell(0, 10, txt=award.description)
            pdf.ln(10)

        # Projects
        if self.person.projects:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Projects", ln=True)
            pdf.set_font("Arial", size=12)
            for proj in self.person.projects:
                pdf.cell(200, 10, txt=f"{proj.title} ({proj.start_date} to {proj.end_date})", ln=True)
                pdf.multi_cell(0, 10, txt=proj.description)
                pdf.cell(200, 10, txt=f"Technologies used: {proj.technologies}", ln=True)
            pdf.ln(10)

        # Publications
        if self.person.publications:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Publications", ln=True)
            pdf.set_font("Arial", size=12)
            for pub in self.person.publications:
                pdf.cell(200, 10, txt=f"{pub.title} in {pub.journal} ({pub.date})", ln=True)
                pdf.multi_cell(0, 10, txt=pub.description)
            pdf.ln(10)

        # Volunteer Experiences
        if self.person.volunteer_experiences:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Volunteer Experiences", ln=True)
            pdf.set_font("Arial", size=12)
            for vol in self.person.volunteer_experiences:
                pdf.cell(200, 10, txt=f"{vol.role} at {vol.organization} ({vol.start_date} to {vol.end_date})", ln=True)
                pdf.multi_cell(0, 10, txt=vol.description)
            pdf.ln(10)

        # Languages
        if self.person.languages:
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(200, 10, txt="Languages", ln=True)
            pdf.set_font("Arial", size=12)
            for lang in self.person.languages:
                pdf.cell(200, 10, txt=f"{lang.name}: {lang.proficiency}", ln=True)
            pdf.ln(10)

        pdf.output(self.file_path)
