A script that uploads photos in bulk to Google Photos

+ Resizes large images to be less than the free limit (2048 x 2048)
+ Uploads all directories under a given directory
+ Restartable
+ Creates the albums as "private" aka "limited"
+ Automatically retries when Google data service errors out.

Attention: This script is becoming obsolete
-------------------------------------------

Changes to GData APIs have impacted what this script can do without the 
user's help. At this point no one has come forward to rewrite the script.

Google Photos was formerly a part of Google+, and before that Picasa Web 
Albums; all three largely different interfaces for the same storage technology.

At some point a Google Picasa application existed for Windows, Mac, and even
linux. Google Photos also exists as application for at least ChromeOS, Android 
and iOS. Google Photos are accessible through Google Drive. 

The unique selling point of this script was, and is now less, to allow bulk
upload of photos, without an overloading webpage, without user interaction, 
and at pretty much maximum upload speed.

Not Done
--------

+ Use multiple threads for uploading.
+ Add Progress UI
+ Deal with duplicate picture and folder names, both on local and web collections.
  + Currently we just throw an exception when we detect duplicate names.

Installation
------------

+ Prerequesites:
  + Python 2.7
  + Google Data APIs http://code.google.com/apis/gdata/
    + gdata-2.0.16for Python
  + The BSD "sips" image processing program.
     + This comes pre-installed on OSX.

Please fill in your credentials in the script.

On first usage, you will be redirected to an OAuth webpage and asked to copy the token, for
caching with the script.

Known Problems
--------------

Google Photos at some point appeared to have an undocumented upload quota system that
limits uploads to a certain number of bytes per month (REJECTED_USER_LIMIT).

Google Photos has a maximum file size, notably for video files, of about 100MB. The script
tries to upload these files but reports when the file size is too big. You are advised to
then prune these files.

Google Photos acts erratic if there are more than 1000 photos in one album (directory).
The script in this case will just keep uploading the same photos over and over on restarts.

Google Photos stopped accepted video files for upload via this API through what seems to be a technical 
issue. The video files will upload normally, but will appear as blank (or rather grey) in the 
recent photoslist in Google Photos.

Around Januari 2017, the API was changed such that creating albums (directories) is no longer
possible. As a result, the script will now no longer create the albums, but request the
user to do some manually beforehand.

Google Photos now has an option to chose whether photos should be resized, which obverrules the 
resizing capabilities of this script.

Sometimes a connection gets lost, and the script has been retrofitted with a back-off recovery
action that tries to just restart the script. The same mechanism is used against OAuth token
expiration.
