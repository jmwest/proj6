# SERVER SPECIFIC VARIABLES
SERVER=class6.eecs.umich.edu	# TODO set your server here!
PORT1=2000												# TODO set your ports here!
PORT2=2001

# GROUP VARIABLES
GROUP=group61											# TODO set you group number
SECRET=rkrjjwkx1or										# TODO set your secret

# STATIC RESOURCE PATH						# TODO make sure you have a backup folder
IMAGES=static/images							# and that the paths are correct
IMAGES_BACKUP=static/images_backup

# SQL SCRIPT PATH									# TODO make sure paths are correct
SQL_CREATE=tbl_create.sql
SQL_LOAD=wikipedia.sql

# PA4_CPP PATH
PA4_CPP=index_server/

# ASSIGNMENT VARIABLES
PA=db														# TODO project number here (for sql)

# SCRIPT COMMANDS
echo "Searching for gunicorn process on $(whoami)..."
GUNI_PID=$(ps aux | grep $(whoami) | grep '[g]unicorn' | awk '{print $2}')
if [ -z "$GUNI_PID" ]; then
	echo "No gunicorn process found."
else
	kill $GUNI_PID
	echo "Gunicorn process terminated."
fi

echo "Searching for CPP process on $(whoami)..."
CPP_PID=$(ps aux | grep $(whoami) | grep 'indexServer' | awk '{print $2}')
if [ -z "$CPP_PID" ]; then
	echo "No C++ process found."
else
	kill $CPP_PID
	echo "C++ process terminated."
fi

# echo "Resetting SQL database..."
# cd flask/sql/
# SQL_QUERY="drop database $GROUP$PA; create database $GROUP$PA; use $GROUP$PA; source $SQL_CREATE; source $SQL_LOAD;"
# mysql -u $GROUP -p"$SECRET" -e "$SQL_QUERY"
# echo "Done."
# cd ..

cd flask/
# gunicorn -b class6.eecs.umich.edu:2000 -b class6.eecs.umich.edu:2001 -D app:app
echo "Starting server on $SERVER at ports $PORT1 and $PORT2..."
gunicorn -b  $SERVER:$PORT1 -b $SERVER:$PORT2 -D app:app
echo "Done."
cd ..

echo "Starting index server."
make -C $PA4_CPP p6
echo "Done."
