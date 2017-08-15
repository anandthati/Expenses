init:
	virtualenv ~/falcon
	. ~/falcon/bin/activate && pip install -r falcon/requirements.txt && python setup.py develop

runserver:
	python graph/manage.py runserver --settings=graph.settings

collectstatic:
	python graph/manage.py collectstatic --noinput
