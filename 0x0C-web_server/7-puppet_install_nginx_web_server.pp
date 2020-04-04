#  Install Nginx web server
exec { 'config':
  provider => shell,
  command  => 'sudo apt-get update; sudo apt-get -y install nginx; echo "Holberton School" > /var/www/html/index.nginx-debian.html; sed -i "48i location /redirect_me{\nrewrite ^/(.*)$ https://www.youtube.com/watch?v=XPwo6giiZ_o permanent;\n}\n" /etc/nginx/sites-available/default; sudo service nginx restart'
}
