#!/usr/bin/perl -wT                     

#The above line tells where the perl interpreter is. -w is a flag for warnings and -T is a flag for special user input taint checking.

print "Content-type: text/html \n\n";

#This is a content-type header that tells the receiving web browser what sort of data it is about to receive - in this case, an HTML document
#If you forget to include it, or if you print something else before printing this header, you'll get an "Internal Server Error" 

print "Hello, world!\n";
