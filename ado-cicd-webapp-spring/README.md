# Spring Web Application CI/CD Demo
[![Build Status](https://dev.azure.com/hyukjun/spring-demo/_apis/build/status/hyukjuns.spring-webapp-cicd-demo?branchName=main)](https://dev.azure.com/hyukjun/spring-demo/_build/latest?definitionId=30&branchName=main)
![badge](https://vsrm.dev.azure.com/hyukjun/_apis/public/Release/badge/12662097-5691-4bfb-b701-d4340345b1fc/7/13)
## 요약
Azure DevOps를 사용해 Spring Framework Web application을 빌드하고, Azure App Service - Webapp에 배포하는 CI/CD 데모
* Source repository는 Azure Repos에 Github repository를 import하여 사용할 수 있습니다.
## 데모 환경
### Spring Framework Project
[spring-boot settings](https://start.spring.io/)

    - Spring Initailizer
        - Maven Project
        - Java Version: 8 (OpenJDK 1.8)
        - Spring Boot: > 2.6.0
        - Packaging: War
        - Dependancies   
            - Spring Web
            - Thymeleaf
            - Spring Boot DevTools
### Azure
    - App Service
        - Webapp for Linux
            - Slot: Production, Dev
            - Runtime stack: Java 1.8, Tomcat 8.5 (TOMCAT|8.5-jre8)
### Azure DevOps (CI/CD Platform)
    - CI: Pipelines
    - CD: Releases
## 데모 시나리오
![cicd](images/ci_cd.png)
### CI (Build Pipeline)
- Source Merge -> Maven package -> Rename ROOT.war -> Publish Artifact

![ci](images/ci.png)
### CD (Release Pipeline)
- Deploy to Dev Slot -> Deploy to Staging Slot -> Swap Slot: Staging and Production

![cd](images/cd.png)

### 파이프라인 완료 후 Production Slot

![prod](images/result.png)

---
## Commands
### Run
#### mvnw
```
mvnw spring-boot:run
```
#### war
```
java -jar <WARFILE>.war
```
### Build
```
mvnw package
```
### Java Command
Compile -> .class
```
javac <JAVAFILE>.java
```
Excuting Class
```
java <ClassName>
```
Excuting JAR or WAR
```
java -jar <FILENAME>.jar or <FILENAME>.war 
```
#### Reference
[Spring GetStarted](https://spring.io/guides/gs/serving-web-content/)
 
