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

SSH into machine and run server.

```sh
(local machine) $ vagrant ssh
(vagrant vm) $ virtualenv venv
(vagrant vm) $ source venv/bin/activate
(vagrant vm) $ pip install -r requirements.txt
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