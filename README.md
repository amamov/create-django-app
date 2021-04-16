# django basic boilerplate version 3.1.4

## 0. base setup

1. [install git](https://github.com/amamov/cs001/tree/main/5%20GIT)

2. [install python and python environment]()

## 1. git clone and initialize git

1. clone this pack.

```shell
git clone https://github.com/amamov/django-basic-boilerplate.git
```

2. initialize git

```shell
rm -rf .git
```

## 2. create environment

## 3. install base django config

```shell
pip3 install -r requirements.txt
```

## 4. create env file

```shell
touch .env
```

```.env
SECRET_KEY="$z^z2@050!rw#sdqctujoq6w02$6ykd8z039uaawa1f)y^!p-o"
...
```

## 5. migrate

```shell
python manage.py migrate
```
