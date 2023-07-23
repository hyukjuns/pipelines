![Publish Docker image](https://github.com/namhj94/Actions-ghcr-CI-CD-Pipeline/workflows/Publish%20Docker%20image/badge.svg)
# Github Action & Github Container Registry
## Description
Github Container Registry 사용과 Github Action을 통한 CI 연습
## Step
1. Dockerfile로 이미지 빌드 
2. CI를 위한 GithubAction pipeline 작성
3. Github Container Registry에 자동으로 이미지 Push
## CI/CD(Delivery) Pipeline
```
code commit & push -> Build Dockerfile -> image -> Push to ghcr.io
```
# Image Usage
### build Dockerfile
```
docker build -t <IMAGENAME> .
```
### Run Image
```
docker run --rm -d -p HOSTPORT:CONTAINERPORT ghcr.io/namhj94/<IMAGENAME>
```
