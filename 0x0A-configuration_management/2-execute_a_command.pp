# kills a process using Pkill

exec {'killmenow' :
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
}
