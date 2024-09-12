# LinkedIn Resume Parser and Job Matcher

This repository contains a set of Python scripts for parsing LinkedIn profiles and job descriptions, as well as matching profiles to job descriptions based on various criteria. The tools included in this repository help in extracting and analyzing key details from resumes and job postings to facilitate efficient job matching.

## Features

- **LinkedIn Profile Parsing:** Extracts detailed information from LinkedIn profiles, including name, title, experience, education, skills, and certifications.
- **Job Description Parsing:** Extracts essential information from job descriptions, including title, required experience, preferred education, skills, and certifications.
- **Profile-to-Job Matching:** Scores and ranks profiles against job descriptions based on skills, certifications, experience, and education to find the best matches.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/RautuA/LinkedIn-Resume-Parser-and-Job-Matcher.git
    cd LinkedIn-Resume-Parser-and-Job-Matcher
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download the spaCy language model:**

    ```bash
    python -m spacy download en_core_web_sm
    ```

## Usage

Here’s a brief overview of how to use the scripts:

1. **Parsing LinkedIn Profiles:**

    Use the `parse_linkedin_profile` function to extract details from LinkedIn profile text.

2. **Parsing Job Descriptions:**

    Use the `parse_job_description` function to extract details from job description text.

3. **Matching Profiles to Jobs:**

    Use the `match_profiles_to_jobs` function to score and rank profiles against job descriptions based on various criteria.

### Example

```python
import re
import pandas as pd
import spacy
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

# Example LinkedIn profile and job description texts
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

job_text = """Title: Senior Data Scientist
Required Experience:
- 5+ years in data science or machine learning roles
- Expertise in Python, SQL, Machine Learning, and Data Analysis
Preferred Education:
- M.Sc. or Ph.D. in Data Science or related fields
Required Certifications:
- AWS Certified Solutions Architect
Skills:
- Python, Machine Learning, SQL, Data Analysis, AWS
"""

# Example usage
profile = parse_linkedin_profile(profile_text)
job = parse_job_description(job_text)
profiles = {"Sparla": profile}
jobs = {"Senior Data Scientist": job}
matches = match_profiles_to_jobs(profiles, jobs)
print(matches)
```

## Requirements

- `pandas`
- `spacy`
- `nltk`
- `sklearn`
- `en_core_web_sm`


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
