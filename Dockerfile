FROM python:3.12

ARG _WORKDIR=/app
WORKDIR ${_WORKDIR}

COPY . ${_WORKDIR}

# WORKDIR /foo
# RUN pwd

RUN pip install -r requirements.txt

EXPOSE 8000

# WORKDIR /app/src/
RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/bin/sh", "-c", "./entrypoint.sh" ]
