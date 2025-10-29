import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Search query
search_url = "https://www.naukri.com/devops-engineer-jobs-in-hyderabad"
response = requests.get(search_url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract job titles and links
jobs = []
for job in soup.select("a.title")[:10]:
    title = job.text.strip()
    link = job["href"]
    jobs.append(f"{title}\n{link}")

# Email setup
sender_email = "prakashreddy22.v@gmail.com"
receiver_email = "prakashreddy22.v@gmail.com"
password = "YOUR_APP_PASSWORD"

body = f"DevOps Engineer Jobs in Hyderabad ({datetime.now().strftime('%Y-%m-%d %H:%M')})\n\n" + "\n\n".join(jobs)
msg = MIMEText(body)
msg["Subject"] = "🔔 Daily DevOps Jobs in Hyderabad"
msg["From"] = sender_email
msg["To"] = receiver_email

# Send mail
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.send_message(msg)

print("✅ Email sent with job listings!")
