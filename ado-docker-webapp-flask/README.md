# Develop Flask Web Application and CI in Azure DevOps
[![Build Status](https://dev.azure.com/hyukjun/flask-demo/_apis/build/status/hyukjuns.flask-webapp-cicd-demo?branchName=master)](https://dev.azure.com/hyukjun/flask-demo/_build/latest?definitionId=32&branchName=master)
## Application Info
## Job Info Scrapping Web Application
### Language & Framework 
- Lang: Python 3.8.6
- Framework: Flask 1.1.2
### Version 1
- Packages: requests, BeautifulSoup4, CSV
- Scrapping python job information in StackOverflow and Indeed
- Save scrapped information to .csv file

### Version 2
- Framework: Flask
- Packages: requests, BeautifulSoup4, CSV
- Scrapping every jobs in StackOverflow
- Spread in to html page
---
## CI Info
### Platform
- Azure DevOps
    - CI Pipelines (azure-pipelines.yml)
### CI
1. Source Integration in github
2. Build Dockerfile
3. Push Image to Dockerhub
