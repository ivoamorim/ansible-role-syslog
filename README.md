syslog
=========

Installs rsyslog and setting default rules

Requirements
------------

None

Role Variables
--------------
```
syslog_udp_enable: false
syslog_udp_address: 127.0.0.1
syslog_udp_port: 514
syslog_tcp_enable: false
syslog_tcp_port: 514
```

Dependencies
------------

- ivoamorim.logrotate

Example Playbook
----------------
```
- hosts: all
  vars:
    syslog_udp_enable: false
    syslog_udp_address: 127.0.0.1
    syslog_udp_port: 514
    syslog_tcp_enable: false
    syslog_tcp_port: 514

  roles:
    - role: ivoamorim.selinux
```

License
-------

BSD
