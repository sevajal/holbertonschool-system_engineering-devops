# manifest that kills a process named killmenow.
exec { 'run the command':
  command => 'pkill -f killmenow',
  path    => [ '/bin', '/sbin' ],
}
