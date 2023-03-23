# colout
This is a small estimating tool

### ENV (Example) ###
# export DBSERVER="localhost"
# export DBUSER="postgres"
# export DB="colout"
# export DBPASS="colout"
#
# psql -h $DBSERVER -U $DBUSER -d $DB -p 5432

### Recreate the tables ###
python ./recreate_tables.py

### DB unit tests ###
python -m unittest discover ./tests/


