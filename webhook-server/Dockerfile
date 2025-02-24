# Python 3.9 기반의 경량 Alpine 이미지 사용
FROM python:3.9-slim

# 표준 출력 버퍼링 비활성화 (실시간 로그 출력)
ENV PYTHONUNBUFFERED=1

# 작업 디렉토리 생성
WORKDIR /app

# Flask 애플리케이션 파일 복사
COPY webhook_server.py /app/webhook_server.py

# 필요한 Python 패키지 설치
RUN pip install flask

# Flask 애플리케이션 실행
CMD ["python", "/app/webhook_server.py"]
