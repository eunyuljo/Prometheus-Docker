# Grafana 공식 이미지 사용
FROM grafana/grafana-oss:latest

# 환경 변수 설정
ENV GF_SECURITY_ADMIN_USER=admin
ENV GF_SECURITY_ADMIN_PASSWORD=admin
ENV GF_USERS_ALLOW_SIGN_UP=false
ENV GF_AUTH_ANONYMOUS_ENABLED=true
ENV GF_AUTH_ANONYMOUS_ORG_ROLE=Viewer
ENV GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource,grafana-worldmap-panel
ENV GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH=/etc/grafana/dashboards/aws-overview.json

# 프로비저닝 설정 파일들 복사
COPY provisioning/ /etc/grafana/provisioning/
COPY dashboards/ /etc/grafana/dashboards/

# 사용자 권한 설정 (grafana 사용자로 변경)
COPY --chown=grafana:grafana provisioning/ /etc/grafana/provisioning/
COPY --chown=grafana:grafana dashboards/ /etc/grafana/dashboards/

# 포트 오픈
EXPOSE 3000
