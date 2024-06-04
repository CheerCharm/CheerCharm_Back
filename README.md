# 🍀응원이 부적해 BACKEND🍀
🦁이화여대 멋쟁이사자처럼 10기 졸업 프로젝트 

### 💚[배포 링크](https://cheer-charm.swygbro.com/) 

### 💚[프로젝트 소개](https://www.swygbro.com/contents/9f8a0d54-f110-4eb0-b3fc-262a8c3da2ed)
링크를 공유해 친구들의 응원을 모아서 나만의 부적을 만들어 저장하는 서비스

### 💚기술 스택
| <image src="https://user-images.githubusercontent.com/69039161/215253421-51587157-d431-42b6-9727-549054c5dc80.png" width=100> | <image src="https://user-images.githubusercontent.com/69039161/215253483-61e98ba8-e8bf-48f9-9035-11cd2718ea5e.png" width=100> | <image src="https://user-images.githubusercontent.com/69039161/215253535-0c29e1d3-c407-4102-abba-5b2be2954248.png" width=100> |
| ---------- | ---------- | ---------- |
| Django | AWS | github actions |

### 💚개발 기능
- 내가 지은 이름과 내가 고른 디자인의 **커스텀 부적**을 생성, 링크 공유 
- 친구의 부적에 **익명으로 닉네임과 내용**을 남겨 응원    
- 응원이 모두 모이면 **완성된 부적 이미지**를 저장하여 공유    
- 부적을 생성한 사람만 열람할 수 있는 **비공개 응원 내용**    
- **마이페이지**에서 언제든 내 부적들을 다시 보고 삭제    
- 로그인, 회원가입, **카카오 로그인** 지원

### 💚파일 구조
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

### 💚Contributors
| 이나경 | 조현영 | 최유미 |
| ---------- | ---------- | ---------- |
| [@rinarina0429](https://github.com/rinarina0429) | [@aqswa](https://github.com/aqswa) | [@yumiiiiiii](https://github.com/yumiiiiiii) |
