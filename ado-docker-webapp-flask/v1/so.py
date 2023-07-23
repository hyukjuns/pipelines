import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python&sort=i"

# step 1. 마지막 페이지 정보 추출하기
def get_last_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
  last_page = pages[-2].get_text().strip()
  return int(last_page)

# step 2. 페이지 당 구인정보 추출
def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping SO: Page: {page}")
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
      job = extract_job_info(result)
      jobs.append(job)
  return jobs

# step 3. 한 페이지 안에 있는 구인항목 정보 추출
def extract_job_info(html):
  title = html.find("h2", {"class": "mb4"}).find("a")["title"]
  # unpacking value
  company, location= html.find("h3",{"class": "mb4"}).find_all("span", recursive=False)
  company = company.get_text(strip=True).strip("-").strip("\n") # or "\r"
  location = location.get_text(strip=True).strip("-").strip("\n")
  job_id = html["data-jobid"]
  return {
    'title': title,
    'company': company,
    'location': location,
    "apply_link": f"https://stackoverflow.com/jobs/{job_id}"
    }

def get_jobs():
  last_page = get_last_pages()
  jobs = extract_jobs(last_page)
  return jobs