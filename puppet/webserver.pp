package { 'php5=5.3.10-1ubuntu3.6': ensure => installed; }
package { 'python2.7': ensure => installed; }
package { 'python-dev': ensure => installed; }
package { 'python-setuptools': ensure => installed; }
package { 'python-pip': ensure => installed; }
package {
    'django': ensure => '1.5.1', provider => 'pip';
 	"django-celery":
 	    provider => pip;
 	    }
package { 'phpmyadmin': ensure => installed; }
package { 'libmysqlclient-dev' : ensure => installed; }
package { 'MySQL-python': ensure => "1.2.3", require => Package['libmysqlclient-dev'], provider => pip; }
package { 'php5-curl': ensure =>installed; }

include mysql
class { 'mysql::server' :
	config_hash => { 'root_password' => 'test',
			'etc_root_password' => 'True' },
}

mysql::db  {'puppettest':
	user => 'testuser',
	password => 'test',
	host =>'localhost',
	grant => ['all'],
}

class { 'apache':
    default_vhost => false,
}

apache::vhost { 'django_server':
       port    => '80',
       vhost_name => '*',
       logroot => '/var/log/apache2/django',
       setenv => 'DJANGO_SETTINGS_MODULE django_server.settings',
       docroot => '/var/www/random_num_web_app/django_server/django_server',
       custom_fragment => 'WSGIScriptAlias / /var/www/random_num_web_app/django_server/django_server/django_server.wsgi'
}

class {'apache::mod::python': }
class {'apache::mod::wsgi': }

class { 'rabbitmq::server':
  port              => '5672',
  delete_guest_user => true,
}