FROM tiangolo/uwsgi-nginx-flask

# 작업 디렉토리 설정
WORKDIR /app

# 호스트(로컬)의 파일을 컨테이너 내부로 복사
COPY ./app /app

# 컨테이너 내부에서 실행할 명령
CMD ["python", "./main.py"]