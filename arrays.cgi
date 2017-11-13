#!/usr/bin/perl -wT
my @people = ();
push(@people, "Howard"); #this makes  Howard the first member in the array
push(@people, ("Sara","Ken","Josh")); #This pushes the list of values into the array
my $who = shift(@people); #This sets $who to Howard and also removes Howard from the @people array
my $who = pop(@people); #This pops Josh off the array. $Who now has Josh.

#FINDING LENGTH

my $linelen = scalar(@people); #scalar is a function used to find the length of the array
print "There are $linelen people in line.\n";
print "The last person in the line is $people[$linelen-1].\n";
print "The last person in the line is $people[$#people].\n";

my @colors = ("cyan", "magenta", "yellow", "black");
foreach my $i (0..$#colors) {
  print "color $i is $colors[$i]\n";
}

my @slice = @colors[1..2]; #this sets @slice to ("magenta","yellow")

#FINDING AN ITEM AN ARRAY

my @results = grep(/pattern/,@listname);

#HASHES

   my %colors = (   red   => "#ff0000",
                    green => "#00ff00",
                    blue  => "#0000ff",
                    black => "#000000",
                    white => "#ffffff" );
    my %colors = (  "red",   "#ff0000",
                    "green", "#00ff00",
                    "blue",  "#0000ff",
                    "black", "#000000",
                    "white", "#ffffff" );
                    

                    
                    
