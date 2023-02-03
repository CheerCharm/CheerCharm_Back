# CheerCharm

### 기술스택

| <image src="https://user-images.githubusercontent.com/69039161/215253421-51587157-d431-42b6-9727-549054c5dc80.png" width=100> | <image src="https://user-images.githubusercontent.com/69039161/215253483-61e98ba8-e8bf-48f9-9035-11cd2718ea5e.png" width=100> | <image src="https://user-images.githubusercontent.com/69039161/215253535-0c29e1d3-c407-4102-abba-5b2be2954248.png" width=100> |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 장고                                                                                                                          | AWS                                                                                                                           | github actions                                                                                                                |

### 프로젝트 소개

링크를 공유해 친구들의 응원을 모아서 나만의 부적을 만들어 저장하는 서비스

### 개발 기능

- 부적 만들기
- 응원하기
- 부적 생성 완료 후 저장하기
- 앱, 소셜 계정 생성

### 파일 구조

📦CheerCharm  
 ┣ 📂.github  
 ┃ ┗ 📂workflows  
 ┃ ┃ ┗ 📜deploy.yml  
 ┣ 📂accounts  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜**init**.py  
 ┣ 📂charms  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜**init**.py  
 ┣ 📂CheerCharm  
 ┃ ┣ 📂settings  
 ┃ ┃ ┣ 📜base.py  
 ┃ ┃ ┣ 📜dev.py  
 ┃ ┃ ┣ 📜prod.py  
 ┃ ┃ ┗ 📜**init**.py  
 ┃ ┣ 📜asgi.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜wsgi.py  
 ┃ ┗ 📜**init**.py  
 ┣ 📂cheers  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜**init**.py  
 ┣ 📂config  
 ┃ ┣ 📂docker  
 ┃ ┣ 📂nginx  
 ┃ ┗ 📂scripts  
 ┣ 📜.env.prod  
 ┣ 📜docker-compose.prod.yml  
 ┣ 📜Dockerfile.prod  
 ┣ 📜manage.py  
 ┣ 📜README.md  
 ┗ 📜requirements.txt

### Contributors

|                                             |                                         |                                    |
| ------------------------------------------- | --------------------------------------- | ---------------------------------- |
| [이나경](https://github.com/rinarina0429) | [조현영](https://github.com/yumiiiiiii) | [최유미](https://github.com/aqswa) |
