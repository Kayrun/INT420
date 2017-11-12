#!/usr/bin/perl -wT

#Using cgi.pm Module

#First you have to actually include the module via the use command. This goes after the #!/usr/bin/perl line and before any other code:
use CGI qw(:standard);
#CGI.pm is implied by the use command. the standard part of the line indicates we're importing "standard" set of fuctions from CGI.pm

print header; #header is a function used from the CGI module and so are the other functions below
print start_html("Hello World");
print "<h2>hello, world!</h2>\n";
print end_html;
