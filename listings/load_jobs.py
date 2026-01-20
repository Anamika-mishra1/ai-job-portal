import os
import django
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()

from listings.models import Job

# Clear existing
Job.objects.all().delete()

# Load jobs
with open('jobs_naukri.json') as f:
    jobs_data = json.load(f)
    
# Save to DB
created = 0
for job_data in jobs_data:
    Job.objects.create(**job_data)
    created += 1

print(f"✅ {created} Gurgaon jobs loaded to Django DB!")
