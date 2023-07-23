# spring-vmss-cicd-demo
Azure DevOps를 사용한 Spring Application to Azure VMSS CI/CD 데모

## Sample Spring Project
### Spring Framework
- Spring Initailizer
    - Maven Project
    - Java Version: 8 (OpenJDK 1.8)
    - Spring Boot: > 2.6.0
    - Packaging: War
    - Dependancies   
        - Spring Web
        - Thymeleaf
        - Spring Boot DevTools

## Azure DevOps
- Build Pipeline (CI/CD(Delivery))
    - Maven Build
    - Rename War
    - Packer Build
        - Ubuntu 18.04
        - JDK 1.8
        - Tomcat 8.5
        - Spring Web Application
- Release Pipeline(CD(Deployment))
    - VMSS 배포
    - BLUE/GREEN 스왑