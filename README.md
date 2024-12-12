# SSH-Camera : Recipe Suggestion Program Prototype

This repository contains a simple prototype for the **Recipe Suggestion Program**, which recommends recipes based on user-provided ingredients using a PostgreSQL database. This is complete with a graphical  user interface developed using the PyQt5 library.

## Prerequisites

1. Have Python installed.
2. Have Git installed.
3. Have Docker Desktop installed.
4. Have PostrgeSQL installed (incase Docker container doesn't work).

## Set up
1. Open a terminal, git clone the repository and navigate to it.
2. Create an isolated virtual environment using Python's venv: "python -m venv venv"
3. Activate the virtual environment, Windows terminal: "venv\Scripts\activate" , macOS/Linux terminal: "source venv/bin/activate"
4. Use pip to install the required dependencies listed in requirements.txt: "pip install -r requirements.txt"

   
1. Build Docker image and container of database in terminal: "docker compose up"
2. Run main.py in terminal: "python main.py" - If program is working fine, skip to instruction 9.
3. If there are issues with docker container of database, try deleting db_data folder and running "docker compose up" again. If that does not work either, you will have to set up the database locally using PostgreSQL. Create a database in Postgres called "SSHiverMeTimbers", then in a terminal: "psql -U [username] -d SSHiverMeTimbers -f SSHiverMeTimbersDB.sql"
4. Run main.py in terminal: "python main.py"
5. Once completed with the program, "docker compose down" to stop and remove container.


