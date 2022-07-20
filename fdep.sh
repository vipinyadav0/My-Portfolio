heroku config:set SECRET_KEY='django-insecure-hra4(y&o8+n-4oh*-$@^qvotl!9)&8slpaum-utw$e07l(1kvr'
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set DISABLE_COLLECTSTATIC=1
git add . && git commit -m "Starting the deployment on heroku"
git push origin master
git push heroku master