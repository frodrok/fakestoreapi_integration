# Setup

apt install -y redis postgresql

service redis start
service postgresql start

sudo su - postgres
psql
postgres=# create database django;
postgres=# create user django with password 'django';
postgres=# alter role django set client_encoding to 'utf8';
postgres=# alter role django set default_transaction_isolation to 'read committed';
postgres=# alter role django set timezone to 'UTC';
postgres=# grant all privileges on database django to django;
\q
exit

python3 -m virtualenv django-venv

. django-venv/bin/activate

pip3 install "setuptools<58.0.0"
pip3 install -r requirements.txt

# Set database connection values
export DB_PORT=5432
export DB_HOST="localhost"
export DB_USER="django"
export DB_PASSWORD="django"
export DB_NAME="django"

python3 manage.py makemigrations fakestoreapi_integration
python3 manage.py makemigrations django_q

python3 manage.py migrate
python3 manage.py schedule_init

### Run the scheduled jobs in the background
python3 manage.py qcluster &

python3 manage.py runserver 0.0.0.0:8000

curl http://localhost:8000/products

