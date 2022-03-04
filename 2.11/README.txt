Torivahti script will monitor and display particular items in certain period of time.
docker-compose.yml explanation:
- download python
- mount torivahti.py to volume
- set tty to true to disable the warning
- run script with python

In this script, it will fetch computer stuff from tori.fi, latest 10 items and repeats that every 120 seconds.
The amount of items and frequency can be defined in docker-compose.yml in the part where python script is run, passing 
as the first argument: amount of items, second argument: frequency to refresh.

USAGE:
- copy files to some directory on your computer with docker installed
- run "docker-compose up"
