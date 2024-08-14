# errorr: Apache is returning a 500 error
# fix: typo error: '.phpp' instead of '.php'


exec { 'fix-typo-sed':
  command => 'sed -i s/\.phpp/.php/g /var/www/html/wp-settings.php',
  path    => '/usr/bin:/usr/sbin:/bin',
}

exec { 'restart-apache2':
  command => 'sudo service apache2 restart',
  path    => '/usr/bin:/usr/sbin:/bin'
}

