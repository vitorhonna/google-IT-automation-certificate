class ntp {
        package { 'ntp':
                ensure => latest,
        }
        file { '/etc/tp.conf':
                source  => '/home/user/ntp.conf',
                replace => true,
                require => Package['ntp'],       
                notify  => Service['ntp'],       
        }
        service { 'ntp':
                enable  => true,
                ensurue => running,
                require => File['/etc/ntp.conf'],
        }
}
