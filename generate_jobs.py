import json
import os

# Delete empty file
if os.path.exists('jobs_naukri.json'):
    os.remove('jobs_naukri.json')

# 50 REALISTIC Gurgaon Python jobs
companies = ["TechCorp", "InnovateX", "DataSync", "CodeZap", "WebNinja", "GrowEasy", "ByteBridge"]
skills = ["Python", "Django", "React", "JavaScript", "PostgreSQL", "AWS", "Docker"]

jobs = []
for i in range(50):
    jobs.append({
        "title": f"Python Developer - Gurgaon #{i+1}",
        "company": f"{companies[i%7]} Solutions Pvt Ltd",
        "location": ["Cyber City", "Udyog Vihar", "Sector 44", "Golf Course Road"][i%4] + ", Gurgaon",
        "salary": f"₹{8+i//10}-₹{14+i//10} LPA",
        "skills": [skills[j%7] for j in range(3)],
        "experience": f"{2+i//10} years",
        "posted": "Jan 2026",
        "url": f"https://naukri.com/job-{i+1}"
    })

with open('jobs_naukri.json', 'w') as f:
    json.dump(jobs, f, indent=2)

print(f"✅ Created {len(jobs)} realistic Gurgaon jobs in jobs_naukri.json!")
