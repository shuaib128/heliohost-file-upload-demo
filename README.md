# FlaskApp Deployment Guide

This guide will help you deploy your Flask application on HelioHost using Plesk.

## Steps to Deploy

### 1. Login to HelioHost

1. Go to [HelioHost](https://www.heliohost.org/) and log in with your credentials.

### 2. Access Plesk Control Panel

1. Once logged in, navigate to the Plesk control panel.

### 3. Navigate to the Files Section

1. In the Plesk control panel, find and click on **Files** in the left-hand menu under the application section.

### 4. Create the Project Directory

1. Within the **Files** section, go to the `httpdocs` directory.
2. Create a new folder named `FlaskApp` (or any other name you prefer).

### 5. Set Up Project Files

In the `FlaskApp` directory, create the following files and folders:

- `requirements.txt`
- `flask.wsgi`
- `app.py`
- `.htaccess`
- `templates` (folder)
- `static` (folder)

### 6. Configure `flask.wsgi`

Create a file named `flask.wsgi` with the following content:

```python
import os
import sys

# Edit your path below
sys.path.append("/home/username/httpdocs/FlaskApp")

sys.path.insert(0, os.path.dirname(__file__))
from app import app as application

# Set this to something harder to guess
application.secret_key = 'your_secret_key'
```
### 7. Configure `.htaccess`

Create a file named `.htaccess` with the following content:

```apache
Options +ExecCGI
RewriteEngine On
RewriteBase /
RewriteRule ^(media/.*)$ - [L]
RewriteRule ^(admin_media/.*)$ - [L]
RewriteRule ^(flask\.wsgi/.*)$ - [L]
RewriteRule ^(.*)$ FlaskApp/flask.wsgi/$1 [QSA,PT,L]
```
Important: Ensure that in the .htaccess file, the path FlaskApp/flask.wsgi matches the name of your project folder.

### 8. Accessing Your Application
Your Flask application should be accessible at:
```
http://shuiab.helioho.st/FlaskApp
````