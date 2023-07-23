# Usage
### Local Excute
```
python app.py
```
### Dockerfile
```
FROM python:3.8-slim-buster

WORKDIR /app #app home

COPY requirements.txt requirements.txt # 필요한 패키지 정보
RUN pip3 install -r requirements.txt # 필요한 패키지 모두 설치

COPY . . # 필요 파일들 복사

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"] # app 실행
```
## Azure webapps 배포시 유의사항
### 애플리케이션 설정
<P>애플리케이션 설정은 암호화된 채널을 통해 미사용 상태와 전송 상태에서 암호화됩니다. 아래 제어를 사용하여 브라우저에 일반 텍스트로 표시하도록 선택할 수 있습니다. 애플리케이션 설정은 런타임 시 애플리케이션에서 액세스하는 환경 변수로 노출됩니다.</P>

### port 설정(랜덤->5000)
```
az webapp config appsettings set --resource-group <group-name> --name <app-name> --settings WEBSITES_PORT=8000
```
<P>
portal에선 설정->구성 탭에서 WEBSITES_PORT를 5000번으로 수정
</P>

### Reference
[Link to docs](https://docs.microsoft.com/ko-kr/azure/app-service/configure-custom-container?pivots=container-linux)