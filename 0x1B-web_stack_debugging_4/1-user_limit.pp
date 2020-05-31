
# puppet file
exec { 'limit':
  command  => '/usr/bin/env sed -i s/holberton.*//g /etc/security/limits.conf'
}
