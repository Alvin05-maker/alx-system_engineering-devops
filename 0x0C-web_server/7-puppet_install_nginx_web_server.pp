# Install and configure nginx on web server

# update package list
exec { 'update package-list':
  command  => 'apt-get update',
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
}

# Install nginx
package { 'nginx':
  ensure   => installed,
  provider => 'apt',
}

# Change file ownership of /var/www/html to current user
exec { 'change owner':
  command  => 'chown -R $USER:$USER /var/www/html'
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
}

# Update html doc
file { '/var/www/index.nginx-debian.html':
  ensure    => present,
  content   => 'Hello World!'
}

# Custom error html page
file { '/var/www/html/404.html':
  ensure  => present,
  content => 'Ceci n\'est pas une page'
}

# Update configuration file and redirection
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => 

"
# Default server configuration
#
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files \$uri \$uri/ =404;
	}

	#

	# deny access to .htaccess files, if Apache's document root
	# concurs with nginx's one
	#
	#location ~ /\.ht {
	#	deny all;
	#}

	location /redirect_me {
		return 301 http://new-destination.com;
	}

	error_page 404 /404.html;
	location /404.html {
		root /var/www/html/;
		internal;
	}

}

"
}

# Check the configuration for errors
exec { 'check config':
  command   => 'nginx -t'
  path      => 'usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin',
  logoutput => true
}

# Reload nginx
exec { ' reload nginx':
  command   => 'service nginx reload'
  path      => /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
}

# Ensure nginx is running
service { 'nginx':
  ensure   => running
}
