##! make
all: local_init local_setup

local_init:
	sudo apt-get update --fix-missing -y
	sudo apt-get install python-pip -y
	sudo pip install virtualenv ansible

local_setup:
	ansible-playbook deploy/vagrant.yml

run:
	../venv/bin/python app/manage.py runserver 0.0.0.0:8000
