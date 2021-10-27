FROM postgres:latest

# install Python 3
RUN apt-get update && apt-get install -y python3 python3-pip vim curl
RUN apt-get install postgresql-server-dev-10 gcc python3-dev musl-dev -y
RUN pip3 install psycopg2
USER postgres

# expose Postgres port
EXPOSE 5432 5002

# bind mount Postgres volumes for persistent data
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

