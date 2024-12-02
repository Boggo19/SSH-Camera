FROM postgres:17.2

ENV POSTGRES_DB=SSHiverMeTimbers
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

COPY sshdb_dump.sql /docker-entrypoint-initdb.d/
