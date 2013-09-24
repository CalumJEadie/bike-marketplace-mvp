bike-marketplace-mvp
====================

Bike Marketplace MVP.

Developing locally
------------------

See http://docs.vagrantup.com/v2/getting-started/index.html for more information.

Boot up a local Virtual Machine using Vagrant.

```sh
(local machine) $ vagrant up
```

SSH into machine and install.

```sh
(local machine) $ vagrant ssh
(vagrant vm) $ virtualenv venv
(vagrant vm) $ source venv/bin/activate
(vagrant vm) $ pip install -r requirements.txt
```

Run server.

```sh
# Get IP address of VM.
(vagrant vm) $ ifconfig | grep 'inet addr'
(vagrant vm) $ python manage.py runserver 0.0.0.0:8000
```

View in browser on host machine.

```sh
# e.g.
open http://10.250.7.241:8000/
```

Deploying to Heroku
-------------------

See https://devcenter.heroku.com/articles/getting-started-with-django for more information.

Create a Heroku app if one hasn't already been created.

```sh
$ heroku create bike-marketplace-mvp
```

Push code to Heroku remote to deploy.

```sh
$ git push heroku master
```