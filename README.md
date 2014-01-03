A script that uploads photos to Picasa Web Albums

+ Resizes large images to be less than the free limit (2048 x 2048)
+ Uploads all directories under a given directory
+ restartable
+ Creates the albums as "private" aka "limited"
+ Automatically retries when Google data service errors out.

Attention: This script is obsolete for Windows and Mac
------------------------------------------------------

It looks like Google Picassa for Windows and Mac now comes with a back up tool that performs the same functionality as
this script. If you are using a Windows or Macintosh system, you probably should look into using the official Google
tool instead. See [Picasa](http://picasa.google.com/).

For more details, read this unofficial blog post describing the
[Google+ Auto Backup for Desktop](http://googlesystem.blogspot.com/2013/12/google-auto-backup-for-desktop.html) tool.


To Do
-----

+ Use multiple threads for uploading.
+ Add Progress UI
+ Deal with duplicate picture and folder names, both on local and web collections.
  + Currently we just throw an exception when we detect duplicate names.
+ Deal with 'Error: 17 REJECTED_USER_LIMIT' errors.

Installation
------------

+ Prerequesites:
  + Python 2.7
  + Google Data APIs http://code.google.com/apis/gdata/
    + gdata-2.0.16for Python
  + The BSD "sips" image processing program.
     + This comes pre-installed on OSX.

Known Problems
--------------

Picasa Web Albums appears to have an undocumented upload quota system that
limits uploads to a certain number of bytes per month.

Do a web search for REJECTED_USER_LIMIT to see the various discussions about
this. From reading the web forums it appears that the upload quota is reset
occasionally (possibly monthly). If you start getting REJECTED_USER_LIMIT
errors when you run this script you may have to wait a month to upload new
pictures.

Some people have reported that paying for yearly web storage will remove the
upload quota.

