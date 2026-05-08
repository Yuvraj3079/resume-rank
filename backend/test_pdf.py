from pypdf import PdfReader

reader = PdfReader("sample_resume.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()

print(text[:2000])