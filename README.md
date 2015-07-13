# ddwrt_timeclock
I had a goal of using an older DDWRT router I had laying around as a time clock for our office.
Having to maintain a timesheet is frustrating when technology could be used to make it a trival task.

Unforunately we're busy doing other things besides finishing this, so the project is moving at a rather slow pace.

Included is an example.json file, and the DDWRT parser class has a 'USE_EXAMPLE' property so if you're like me 
don't have a DDWRT router at home to use to experiment you can use the example instead.

# how it works
  *Copy settings-example.json to settings.json, adjust to match your configuration;
  
  *Set main.py on a cron (we're doing 5min intervals)
  
  *Setup django to run the web application (we're currently using the developer preview `python manage.py runserver`)
  
main.py then posts to the django service via the 'post_url' in settings.json and django manages all login times

# python requirements (python 2.7)
django

request

# install
install to any directory with `git clone https://github.com/GJRDiesel/ddwrt_timeclock.git`

create a cron for main.py `crontab -e`

create a new superuser `python manage.py createsuperuser`

run the main.py to find out current employees hostnames `python main.py`

create the sqllite db `python manage.py migrate`

start django *DEVELOPMENT* web server `python manage.py runserver [ip]:[port]`

login to admin with the new super user you created and add employees, then go to hostnames and add any hostname you want to track for each employee


# ddwrt? rasberry pi? why?
These are things we had laying around and we're using already.

# python?
Yeah... I don't have much experience with it, this is my hello-world project for python.
