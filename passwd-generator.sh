#Use Kernel's urandom device to generate password
#do NOT use on a multiuser system (multiple people using it)

l=$1
	[ "$l" == "" ] && l=16
      	tr -dc A-Za-z0-9_ < /dev/urandom | head -c ${l} | xargs
 
