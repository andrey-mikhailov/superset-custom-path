FROM apache/superset:1.3.2

USER root
COPY ./valamis/ /app/valamis/
RUN chown -R superset:superset /app/valamis/
RUN chown -R superset:superset /app/superset/static/

# psycopg2 and redis are taken from original helm charts https://github.com/apache/superset/blob/cc1c6c1bb60b6357348028209062772927fd39ca/helm/superset/values.yaml#L33
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends mc && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install --no-cache-dir psycopg2==2.8.6 redis==3.5.3 \
    pip install --no-cache-dir clickhouse-driver==0.2.2 clickhouse-sqlalchemy==0.1.6


RUN PYTHONPATH="/app/pythonpath:/app/valamis"

ENV PYTHONPATH "${PYTHONPATH}:/app/valamis"


USER superset
# fix urls
RUN python /app/valamis/replace_url.py

