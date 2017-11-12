#A good first step in debugging is to use the CGI:Carp module in your program. This causes all warnings and fatal error messages to be echoed in your browser window. You'll want to remove this line after you're finished developing and debugging your programs. The info here is the same as "tail /var/log/apache2/error_log

use CGI:Carp qw(warningToBrowser fatalsToBrowser);

#also use: perl -cwT scriptname.cgi
