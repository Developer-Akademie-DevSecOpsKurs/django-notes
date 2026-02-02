FROM python:3.12

ARG _WORKDIR=/app
WORKDIR ${_WORKDIR}

COPY . ${_WORKDIR}

RUN pip install -r requirements.txt

EXPOSE 8000

# WORKDIR /app/src/
RUN chmod +x entrypoint.sh

RUN groupadd -r djangogroup && useradd -r -g djangogroup djangouser
USER djangouser:djangogroup

ENTRYPOINT [ "/bin/sh", "-c", "./entrypoint.sh" ]
