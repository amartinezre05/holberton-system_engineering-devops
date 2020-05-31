# puppet file
exec { 'limit':
  command  => '/bin/sed -i "s/15/3000/g" /etc/default/nginx && /usr/sbin/service nginx restart'
}
