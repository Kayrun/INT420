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
    &displayform();
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
    &verifyform();
    &insertuser();
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

sub insertuser
{
  #my $salt = "Major Minus 8991076543&123"
$cryptpasswd = sha1_base64($form{password});

#Form SQL insert statement
$insert = qq~insert users(name, password) values('$form{name}','$cryptpasswd')~;
$dbh=DBI->connect($connectionInfo,$user,$passwd);

#Prepare MySQL statement and create Statement Handler $sth
$sth=$dbh->prepare($insert);

#Execute Statement Handler and test for success
if($sth->execute())
  {
      &displaysuccess;
  }
else
  {
      &displayfail;
  }

#Disconnect the database connection
$dbh->disconnect();
}

sub displaysuccess
{
print qq~<html>
        <head>
        <title>Account Creation</title>
        </head>
        <body>
  <center>
        <h2>Acount Created Successfully!</h2>
        <img src="http://www.clker.com/cliparts/2/k/n/l/C/Q/transparent-green-checkmark-hi.png" alt="Accepted" width="460" height="345">
  </body>
        </html>
        ~;
}

sub displayfail
{
  print qq~<html>
           <head>
           <title>Account Creation</title>
           </head>
           <body>
           <h2>Uh oh, account creation failed</h2>
           </body>
           </html>
           ~;
}


sub displayform
  {
      print qq~
              <html>
              <head>
              <title>Register User</title>
              </head>
              <body>
              <form action="register.cgi" method=post>
              <center>
              <h2>Register a User and Password</h2>
              User Name: <input type=text name=name value="$form{name}">$errors{name}
              <br>
              <i>Username should be all lowercase and 8 chars or less</i>
              <br>
              <br>
              Password: <input type=password name=password>$errors{password}
              <br>
              Retype Password: <input type=password name=password2>$errors{password2}
              <br>
              <input type=submit value="Insert" name=Insert>
              <input type=reset value=Reset name=reset>
              </form>
              </body>
              </html>
              ~;
  }

  sub verifyform
    {
      $missing = 0;

      #Test for username between 2 and 8 alphanumerics
      if($form{'name'}!~/^[a-z0-9]{2,8}$/)
          {
            $errors{'name'}="Please enter up to 8 character username";
            $missing = 1
          }
      else
          {
            #Test for eisting username in table
            $select = qq~select name from users where name = '$form{name}'~;
            $dbh=DBI->connect($connectionInfo,$user,$passwd);
            $sth=$dbh->prepare($select);
            $sth->execute();

            if(@row=$sth->fetchrow_array())
              {
                $errors{'name'} = "name already registered";
                $missing = 1;
              }
            else
              {
                $errors{'name'}="";
              }
          }

        #Test for password between 6 and 10 alphanumerics
        if($form{'password'} !~ /^[a-z0-9A-Z]{6,10}$/)
            {
              $errors{'password'}="Please enter 6 to 10 character password";
              $missing = 1
            }
        else  {
              $errors{'password'} = "";
        }

        #Test for password entered twice
        if($form{'password'} ne $form{'password2'})
            {
              $errors{'password2'} = "Passwords do not match";
              $missing = 1;
            }

        else  {
              $errors{'password2'} = "";
        }

        if($missing==1)
          {
            &displayform;
            exit;
          }
    }
