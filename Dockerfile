FROM python:3.12-alpine

ARG _WORKDIR=/app
WORKDIR ${_WORKDIR}

COPY . ${_WORKDIR}

RUN pip install -r requirements.txt

EXPOSE 8000

# WORKDIR /app/src/
RUN chmod +x entrypoint.sh
RUN addgroup -S djangogroup && adduser -S djangouser -G djangogroup && \
    chown -R djangouser:djangogroup ${_WORKDIR}
USER djangouser

ENTRYPOINT [ "/bin/sh", "-c", "./entrypoint.sh" ]
