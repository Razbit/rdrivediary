#Setting up Apache
##Ubuntu
Install Apache and Python. Enable Apache's CGI functionality
```sudo apt-get install apache2
sudo apt-get install python
sudo a2enmod cgi
```

Add the following to your /etc/apache2/apache2.conf:
```<Directory /var/www/path/to/rdrivediary/cgi-bin>
	Options ExecCGI
	SetHandler cgi-script
</Directory>
```

More information: https://www.linux.com/community/blogs/129-servers/757148-configuring-apache2-to-run-python-scripts

