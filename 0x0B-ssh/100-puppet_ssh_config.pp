# Manifest to connect to a server without typing a password.
exec { 'SSH client configuration':
  command => 'ssh-copy-id -i ~/.ssh/school ubuntu@54.160.169.188',
  path    => [ '/bin', '/sbin' ],
}
