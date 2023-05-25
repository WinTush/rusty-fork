web: python manage.py collectstatic --noinput && python manage.py migrate && gunicorn config.wsgi --config="docker/gunicorn.conf.py"
