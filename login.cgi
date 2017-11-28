#!/usr/bin/perl -w

#Use the DBI (database interface) module
use DBI;

use Digest::SHA1 qw(sha1_hex sha1_base64);


#Declare variables with MySQL connection data
$db="int420_173a30";
$user="int420_173a30";

$passwd="ebTA9338";
$host="db-mysql.zenit";
$connectionInfo="dbi:mysql:$db;$host";

#Print HTTP header
print "Content-Type:text/html\n\n";

#If first time script run display form
if($ENV{"REQUEST_METHOD"} eq "GET")
  {
    &displaylogin();
    exit;
  }

#Else process for and insert into DB
else  {
	&parseform();
    #print "<html><head><title>Student Survey</title></head>\n";
    #print "<body>\n";
    #print "Login Name:",             $form{"lname"}, "<br>";
    #print "Full Name:",       $form{"fname"}, "<br>";
    #print "Phone Number:",       $form{"phone"}, "<br>";
    #print "Email:",   $form{"email"}, "<br>";
    #print "</body></html>\n"; */
    &verify();
    &sendmessage();
    exit;
}

#Standard form parsing using POST method
sub parseform
{
  read(STDIN,$qstring,$ENV{'CONTENT_LENGTH'}); #get data from environment variables
  @pairs = split(/&/, $qstring); #break data up on ampersands and store in array
  foreach (@pairs) {             #start a for loop to process form data
  ($key, $value) = split(/=/);   #split field name and value on '=', store in two scalar variables
    $value =~ tr/+/ /;                                           #translate + signs back to spaces
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("c", hex($1))/eg; # translate special characters
    $form{$key} = $value;
   }
}

sub displaylogin
  {
    print qq~
              <html>
              <head>
              <title>Login Page</title>
              </head>
              <body>
              <form action="login.cgi" method=post>
              <center>
              <h2>Enter Your Username and Password</h2>
              User Name: <input type=text name=name value="$form{name}">$errors{name}
              <br>
              Password: <input type=password name=password>
              $errors{password}
              <br>
              <input type=submit value="Insert" name = Insert>
              <input type=reset value=Reset name=reset>
              </form>
              </body>
              </html>~;
  }

  sub verify
      {
        #Form SQL select statement to select users record from table
        $select = qq~select id, name, password from users where name = '$form{name}'~;

        #Connect to MySQL and create Database Handler $dbh
        $dbh=DBI->connect($connectionInfo,$user,$passwd);
        $sth=$dbh->prepare($select);
        $sth->execute();

      if(@row=$sth->fetchrow_array())
        {
          #If row found compate encrypted passwords
          $cryptpasswd = sha1_base64($form{password});

          if($cryptpasswd ne $row[2])
            {
              $errors{password} = "Incorrect password";
              &displaylogin;
              exit;
            }
        }

      else
          {
            #If row not found display username not found
            $errors{name} = "User name not found";
            &displaylogin;
            exit;
          }
      }

    sub sendmessage
      {
        print qq~<html>
                <head>
                <title>Login Success</title>
                </head>
                <body>
          <center>
                <h2>Logged in Successfully!</h2>
                <img src="http://www.clker.com/cliparts/2/k/n/l/C/Q/transparent-green-checkmark-hi.png" alt="Accepted" width="460" height="345">
          </body>
                </html>
                ~;
      }
