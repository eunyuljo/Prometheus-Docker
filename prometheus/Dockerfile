# Prometheus 공식 이미지 사용
FROM prom/prometheus

# 작업 디렉토리 설정
WORKDIR /etc/prometheus

# 로컬에 저장된 prometheus.yml을 복사한다.
ADD prometheus.yml /etc/prometheus/
ADD alert_rules.yml /etc/prometheus/

# 데이터를 저장할 볼륨 생성
VOLUME [ "/prometheus" ]

# Prometheus 실행 (ENTRYPOINT + CMD 방식)
# ENTRYPOINT는 반드시 실행되어야하는 기본 실행 파일을 의미한다.
ENTRYPOINT [ "/bin/prometheus" ]

# CMD는 ENTRYPOINT에서 실행할 기본 인자를 지정한다.
# /bin/prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/prometheus 이 설정을 의미하는 것이다.

CMD [ "--config.file=/etc/prometheus/prometheus.yml", "--storage.tsdb.path=/prometheus" ]

# Prometheus UI 포트 오픈
EXPOSE 9090
