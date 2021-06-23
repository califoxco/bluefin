# BLUEFIN

BLUEFIN is a MVP that has the ability to browse all available properties, Filter properties by attribute, show detailed page for each one of them, and grants the site administrator the freedom to update their database with ease.

# Installation
### 1. Create a virtual environment
```
  virtualenv -p python3 env
```

### 2. Activate virtual environment
```
. env/bin/activate
```

### 3. Install from requirements.txt
```
  pip install -r .\base\requirements.txt
```

### 4. Start Local Server
```
  python .\base\manage.py runserver
```

### 5. Visit Local Host
localhost is ususally http://127.0.0.1:8000/

# Features
* Search Bar - type in the any address or keyword, click search
* Filter Bar - type in price range, or number of bedrooms, or choose property type, click submit
* Detail View - Click on home images to view detail
* Admin Panel - modifies database easily, elaborated below

# Admin Panel
1. To visit the admin page, go to http://127.0.0.1:8000/admin, here you will need to enter the username and passwords
2. username: 'admin', passwords: 'admin'
3. You can always create more admins by using the below code
```
python base\manage.py createsuperuser
```
4. you can choose Owner or Property to visit/modify the data. Please play around with it to try out the filter/search functionailty 

### If you have any questions, please ask me via my email. Thanks!
### Jiaming(Alex) Yang
