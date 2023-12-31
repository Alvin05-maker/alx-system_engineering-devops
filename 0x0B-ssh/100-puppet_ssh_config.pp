#!/usr/bin/env bash
# using puppet for configuration

file { '~/.ssh/config':
  ensure  => 'present',
}
file_line { 'Turn off password authentication':
  path    => '~/.ssh/config',
  line    => 'PasswordAuthentication no',
  match   => '^#PasswordAuthentication',
}
file_line { 'Declare Identity File':
  path    => '~/.ssh/school',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#IdentityFile',
}
