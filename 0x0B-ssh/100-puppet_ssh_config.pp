# Manifest to connect to a server without typing a password.
exec { 'SSH client configuration':
  command => [ 'eval "$(ssh-agent)"', 'ssh-add' ],
  path    => [ '/bin', '/sbin' ],
}
