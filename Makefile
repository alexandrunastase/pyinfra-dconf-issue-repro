up: init
	pyinfra inventory.py up.py -vv --debug

init:
	sudo -l 