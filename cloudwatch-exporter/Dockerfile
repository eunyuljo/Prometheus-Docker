FROM prom/cloudwatch-exporter
COPY cloudwatch.yml /config/config.yml
WORKDIR /config
ENV AWS_REGION=ap-northeast-2
ENV AWS_ROLE_ARN=arn:aws:iam::977099011692:role/Prometheus-CloudWatch-Role
