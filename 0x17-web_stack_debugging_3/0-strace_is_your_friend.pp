# This Puppet script fixes a typo in the WordPress configuration file that was
# causing a 500 Internal Server Error. Specifically, it corrects ".phpp" to ".php"
# in the wp-settings.php file.

exec { 'Fix typo in wp-settings.php':
  command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin:/sbin',
}
