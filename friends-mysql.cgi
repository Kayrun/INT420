#!/usr/bin/perl -w

#Use the DBI (database interface) module
use DBI;

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
    print "<html><head><title>Student Survey</title></head>\n";
    print "<body>\n";
    print "Last Name:",             $form{"lname"}, "<br>";
    print "First Name:",       $form{"fname"}, "<br>";
    print "Phone Number:",       $form{"phone"}, "<br>";
    print "Email:",   $form{"email"}, "<br>";
    print "</body></html>\n";
    &verifyform();
    &insertfriend();
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

sub insertfriend
  {
    #Form SQL insert statement
    $insert = qq~insert friends(lname, fname, phone, email) values('$form{lname}','$form{fname}','$form{phone}','$form{email}')~;
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
            <title>My Friends</title>
            </head>
            <body>
            <h2>Record Added</h2>
            </body>
            </html>
            ~;
    }

  sub displayfail
    {
      print qq~<html>
               <head>
               <title>My Friends</title>
               </head>
               <body>
               <h2>Record NOT Added</h2>
               </body>
               </html>
               ~;
    }

    sub displayform
      {
        print qq~
              <html>
              <head>
	      <meta charset ="utf-8">
	      <meta name="viewport" content="width=device-width, initial-scale=1">
              <title>My Friends</title>
              </head>
              <body>
              <form action="friends-mysql.cgi" method="POST">
              <h2>My Friends</h2>
              <p>Last Name: <input type="text" name="lname" value="$form{lname}">$errors{lname}</p>
              <p>First Name: <input type="text" name="fname" value="$form{fname}">$errors{fname}<p>
              <p>Phone Number: <input type="text" name="phone" value="$form{phone}">$errors{phone}(10 digits only please)</p>
              <p>E-mail: <input type="text" name="email" value="$form{email}">$errors{email}</p>
              <input type="submit" value="Insert" name="Insert"/>
              <input type="reset" value="Reset" name="reset"/>
              </form>
              </body>
              </html>
              ~;
      }

      sub verifyform
        {
          $missing = 0;         #assuming there is nothing missing and hence initializing it to 0
          foreach (keys %form)
            {
              if($form{$_} eq "")
                {
                  $errormsg="Please enter data for required field";
                  $missing = 1; #If there is a missing field, setting the flag to 1
                }
              else
                {
                  $errormsg="";
                }
              $errors{$_}=$errormsg;   #Load the % errors hash with error message
            }
          if($missing == 1)
            {
              &displayform;
              exit;
            }
        }
