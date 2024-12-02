FROM postgres:17.2

ENV POSTGRES_DB=SSHiverMeTimbers
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

COPY SSHiverMeTimbersDB.sql /docker-entrypoint-initdb.d/

EXPOSE 5432