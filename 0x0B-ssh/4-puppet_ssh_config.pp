# configuration file
file_line { 'Append a line to /etc/ssh/ssh_config':
ensure  => present,
path    => 'etc/ssh/ssh_config'
line    => '    PasswordAuthentication no',
}
file_line { 'Append a line to /etc/fuse.conf':
ensure  => present,
path    => 'etc/ssh/ssh_config'
line    => '    IdentityFile ~/.ssh/holberton',
}
