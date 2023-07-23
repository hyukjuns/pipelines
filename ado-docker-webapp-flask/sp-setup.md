# Azure Service Principal Setup
Azure DevOps Pipeline이 사용할 Service Principal 생성
### ServicePrincipal 생성
1. Azure portal에서 App 등록
2. 암호 생성(Client Secret)
3. 구독 id, 앱 id, 앱 secret, 테넌트 id 기록
4. Azure Webapp에 IAM 설정(배포시킬 리소스에 IAM등록)
### Azure DevOps에 Service Connection 등록
Azure DevOps에 생성한 SP정보 등록하여 파이프라인에서 Azure Webapp에 Application을 자동으로 배포할 수 있도록 함  