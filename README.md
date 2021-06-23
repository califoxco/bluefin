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
