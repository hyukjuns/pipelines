import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

# step 1. 마지막 페이지 정보 추출하기
def get_last_pages():
  # page info 추출
  result = requests.get(URL)
  #indeed_result.text -> html 전부 불러옴
  # bs4로 html 파싱하여 html 정보 조작 가능하게 함
  soup = BeautifulSoup(result.text, "html.parser")
  # 페이지 링크 찾기 시작
  pagination = soup.find("div", {"class": "pagination"})
  links = pagination.find_all('a') # to list, a 찾아서 리스트로 만듦
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))
  max_page = pages[-1]
  return max_page

# step 2. 페이지 당 직업 정보 추출하기
def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping Indeed: Page: {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for res in results:
      job = extract_job_info(res)
      jobs.append(job)
  return jobs

# step 3. 한 페이지 안에 있는 구인항목 정보 추출
def extract_job_info(html):
  title = html.find("h2", {"class": "title"}).find("a")["title"]
  company = html.find("span", {"class": "company"})
  if company:
    company_anchor = company.find("a")
    if company_anchor is not None:
      company = str(company_anchor.string)
    else:
      company = str(company.string)
    company = company.strip()
  else:
    company = None
  location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
  job_id = html["data-jk"]
  return {
    'title': title,
    'company': company,
    'location': location,
    'link': f"https://www.indeed.com/viewjob?jk={job_id}"
  }

def get_jobs():
  last_pages = get_last_pages()
  jobs = extract_jobs(last_pages)
  return jobs