#!/usr/bin/perl -w

#print HTTP header
print  "Content-Type: text/html;charset=ISO-8859-1\n\n";

# print starting XHTML tags
print qq~
  <?xml version="1.0" encoding="utf-8"?>
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML XHTML 1.1/EN" "http://w3.org/TR/xhtml11/DTD/xhtml11.dtd">

  <html xmlns="http://www.w3.org/1999/xhtml">

  <head><title>Hello CGI!</title></head>
  <body>

  ~;

  # Print page body
  print "<p>\n";
  print "Youare using the following browser: $ENV{HTTP_USER_AGENT} <br />\n";
  print "Your IP address is $ENV{REMOTE_ADDR} <br />\n";
  print "This server is using $ENV{SERVER_SOFTWARE} and runnin on port $ENV{SERVER_PORT} <br />\n";
  print "The server's document root is $ENV{DOCUMENT_ROOT} <br />\n";
  print "</p>\n";

  #print ending HTML tags
  print "</body></html>\n";
