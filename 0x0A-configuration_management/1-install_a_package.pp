#!/usr/bin/puppet
# install flask 2.1.0

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  path    => ['/usr/bin'],
  unless  => '/usr/local/bin/flask --version | grep "2.1.0"',
  require => Package['python3-pip'],
}
