import re
import pandas as pd

def parse_linkedin_profile(profile_text):
    profile_data = {}

    name_match = re.search(r"Name:\s*(.*)", profile_text)
    profile_data['name'] = name_match.group(1) if name_match else "Unknown"

    title_match = re.search(r"Title:\s*(.*)", profile_text)
    profile_data['title'] = title_match.group(1) if title_match else "Unknown"

    experience_match = re.findall(r"- (.*), (.*) \((\d{4})-(\d{4})\)", profile_text)
    profile_data['experience'] = [{'title': exp[0], 'company': exp[1], 'from': exp[2], 'to': exp[3]} for exp in experience_match]

    education_match = re.findall(r"- (.*), (.*) \((\d{4})\)", profile_text)
    profile_data['education'] = [{'degree': edu[0], 'institution': edu[1], 'year': edu[2]} for edu in education_match]

    skills_match = re.search(r"Skills:\s*(.*)", profile_text)
    profile_data['skills'] = skills_match.group(1).split(", ") if skills_match else []

    cert_match = re.search(r"Certifications:\s*(.*)", profile_text)
    profile_data['certifications'] = cert_match.group(1).split(", ") if cert_match else []

    return profile_data

profile_text = """Name: Sparla
Title: Data Scientist
Experience:
- Data Scientist, ABC Corp (2018-2023)
- Data Analyst, XYZ Inc. (2015-2018)
Education:
- M.Sc. in Data Science, University of California (2015)
- B.Sc. in Computer Science, Stanford University (2013)
Skills:
- Python, Machine Learning, Data Analysis, SQL, Excel
Certifications:
- Google Data Engineer Certification
- AWS Certified Solutions Architect
"""

profile = parse_linkedin_profile(profile_text)

profile_df = pd.DataFrame([{
    'name': profile['name'],
    'title': profile['title'],
    'skills': ', '.join(profile['skills']),
    'certifications': ', '.join(profile['certifications'])
}])

experience_df = pd.DataFrame(profile['experience'])
education_df = pd.DataFrame(profile['education'])

print("Profile Information:")
print(profile_df)
print("\nExperience:")
print(experience_df)
print("\nEducation:")
print(education_df)