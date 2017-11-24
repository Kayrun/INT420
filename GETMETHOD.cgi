#!/usr/bin/perl -w

#print a standard 200-level HTTp header
print "Content-Type:text/html\n\n";

#the following code - in blue - will get the data from the form and store it in a hash name %form

#get data from environment variable
$qstring = $ENV{'QUERY_STRING'};

#break data up on ampersands and store in array
@pairs = split(/&/, $qstring);

#start a loop to process form data
foreach (@pairs) {
#split field name and value on '=', store in two scalar variables
($key, $value) = split(/=/);
#translate '+' signs back to spaces
$value =~ tr/+/ /;
#translate special characters
$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("c", hex($1))/eg;
#store data in hash
$form{$key} = $value;
}

#now the data is stored in the has %form

#send output to browser as HTML

print "<html><head><title>Student Survey</title></head>\n";
print "<body>\n";

#display form data

&displayInfo();

print "</body></html>\n";

#This subroutine will display information received from a form

sub displayInfo {

print "Full Name:",             $form{"person"}, "<br>";
print "Favourite Sport:",       $form{"sport"}, "<br>";
print "Favourite Seneca Course:",       $form{"course"}, "<br>";
print "GPA:",   $form{"gpa"}, "<br>";
}
