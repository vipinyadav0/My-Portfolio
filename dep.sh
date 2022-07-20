git add . && git commit -m "Starting the deployment on heroku"
git push origin master
git push heroku master
heroku run python3 manage.py migrate