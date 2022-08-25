# Manifest to install Nginx web server.
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  content => 'Hello World',
}

file_line { 'redirection':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.mocionesdevida.com permanent;',
  after  => 'server_name _;',
}
