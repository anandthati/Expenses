init:
	virtualenv ~/falcon
	. ~/falcon/bin/activate && pip install -r falcon/requirements.txt && python setup.py develop

runserver:
	python graph/manage.py runserver --settings=graph.settings

collectstatic:
	python graph/manage.py collectstatic --noinput

migrate:
	python graph/manage.py makemigrations --settings=graph.settings && python graph/manage.py migrate --settings=graph.settings
