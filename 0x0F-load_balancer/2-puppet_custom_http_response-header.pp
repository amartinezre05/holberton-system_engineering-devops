#  Install Nginx web server
exec { 'config':
  provider => shell,
  command  => 'sudo apt-get update; sudo apt-get -y install nginx; sed -i "/http {/a \ \nadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf; sudo service nginx restart'
}
