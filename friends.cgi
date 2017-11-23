#!/usr/bin/perl -w

use strict;

my %friends;
my $name;
my $phone;

#Path to the log file may need to be adjusted
open FILE, "//home/int420_173a30/apacheserver/htdocs/sample.txt" or die ("Cannot open file!\n");
while(<FILE>)
  {
    chomp
    ($name,$phone)=split(" ",$_);
    $friends{$name}=$phone;
  }

foreach (keys %friends)
{
  print "Name: ", $_,"\n";
  print "Phone: ", $friends{$_},"\n\n";
}
