#!/usr/bin/perl -wT
use CGI qw(:standard);
#A good first step in debugging is to use the CGI:Carp module in your program. This causes all warnings and fatal error messages to be echoed in your browser window. You'll want to remove this line after you're finished developing and debugging your programs. The info here is the same as "tail /var/log/apache2/error_log
use CGI:Carp qw(warningsToBrowser fatalsToBrowser);
#also use: perl -cwT scriptname.cgi
use strict;
#use strict is a standard Perl module that requires you to declare all variables.

my $email = "yoda\@starwars.com";
my $url = "starwars.com";

print header;
print start_html("Scalars");
print <<EndHTML;
<h2>Hello</h2>
<p>
My e-mail address is $email, and my web url is 
<a href=$url">$url</a>
</p>
EndHTML

print end_html;

