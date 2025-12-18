# Vulnerable Dockerfile - FOR SECURITY TESTING ONLY
FROM python:latest

ADD . /app
WORKDIR /app

ENV DATABASE_PASSWORD=supersecret123
ENV API_KEY=sk-1234567890abcdef
ENV AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
ENV AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

RUN apt-get update && apt-get install -y curl wget netcat telnet openssh-client
RUN pip install -r requirements.txt

ADD https://example.com/script.sh /tmp/script.sh
RUN chmod +x /tmp/script.sh

EXPOSE 22
EXPOSE 80
EXPOSE 443
EXPOSE 3306
EXPOSE 5432
EXPOSE 6379
EXPOSE 8080

CMD python src/app.py
