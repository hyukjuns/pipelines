# python 개발 환경
### Ubuntu 18.04
1. python3 업그레이드 pip, venv 설치
```
sudo apt update && sudo apt upgrade
sudo apt install python3[sudo apt upgrade python3]
sudo apt install python3-pip
apt install python3-venv
```
2. 가상 환경 만들기
```
python3 -m venv venv
source .venv/bin/activate
```
3. 비활성화
```
deactivate
```
4. 필요한 패키지 설치 및 requirements.txt 만들기
```
pip3 install <PACKAGE_NAME>
pip3 freeze > requirements.txt
```
5. 이후 재사용시 필요한 패키지 설치(이미지 만들때 RUN에 추가)
```
pip3 install -r requirements.txt
```

### pip
Python용 표준 패키지 관리자인 pip<bt>
pip를 사용하면 Python 표준 라이브러리에 포함되지 않은 추가 패키지를 설치하고 관리할 수 있습니다.
### venv
<p>
간단한 가상 환경을 만들고 관리하는 데 사용되는 표준 모듈인 venv<br>
Python 개발 프로젝트에는 가상 환경을 사용하는 것이 좋습니다. 가상 환경을 만들면 프로젝트 도구를 격리하고 버전이 다른 프로젝트의 도구와 충돌하지 않도록 방지할 수 있습니다. 예를 들어 Django 1.2 웹 프레임워크가 필요한 이전 웹 프로젝트를 유지 관리할 수 있지만, Django 2.2를 사용하면 흥미로운 새 프로젝트가 제공됩니다. 가상 환경 외부에서 Django를 전역적으로 업데이트하면 나중에 일부 버전 관리 문제가 발생할 수 있습니다. 가상 환경에서는 실수로 인한 버전 충돌 방지 외에도 관리자 권한 없이 패키지를 설치하고 관리할 수 있습니다.
</p>

### Reference
[ms python dev](https://docs.microsoft.com/ko-kr/windows/python/web-frameworks)
