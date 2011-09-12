A script that uploads photos to Picasa Web Albums

+ Resizes large images to be less than the free limit (2048 x 2048)
+ Uploads all directories under a given directory
+ restartable
+ Creates the albums as "private" aka "limited"
+ Automatically retries when Google data service errors out.

To Do:

+ Allow password to be entered from stdin (rather than passed on command line.)
+ Use multiple threads for uploading.
+ Add Progress UI
+ Deal with duplicate picture and folder names, both on local and web collections.
  + Currently we just throw an exception when we detect duplicate names.
+ Deal with 'Error: 17 REJECTED_USER_LIMIT' errors.

Installation

+ Prerequesites:
  + Python 2.7
  + Google Data APIs http://code.google.com/apis/gdata/
    + gdata-2.0.14 for Python
  + The BSD "sips" image processing program.
     + This comes pre-installed on OSX.

