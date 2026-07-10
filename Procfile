web: python manage.py migrate --noinput && python manage.py loaddata fixtures/deploy_data.json && python -m gunicorn kilimo_hub.wsgi:application --log-file -
