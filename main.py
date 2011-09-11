import argparse
import filecmp
import gdata.photos.service
import gdata.media
import gdata.geo
import os

def parseArgs():
  parser = argparse.ArgumentParser(description='Upload pictures to picasa web albums / Google+.')
  parser.add_argument('--email', help='the google account email to use (example@gmail.com)', required=True)
  parser.add_argument('--password', help='the password', required=True)
  parser.add_argument('--source', help='the directory to upload', required=True)

  args = parser.parse_args()
  return args

def login(email, password):
  gd_client = gdata.photos.service.PhotosService()
  gd_client.email = email
  gd_client.password = password
  gd_client.source = 'palevich-photouploader'
  gd_client.ProgrammaticLogin()
  return gd_client

def listAlbums(gd_client):
  albums = gd_client.GetUserFeed()
  for album in albums.entry:
    print 'title: %s, number of photos: %s, id: %s' % (album.title.text,
        album.numphotos.text, album.gphoto_id.text)
    print vars(album)

def findAlbum(gd_client, title):
  albums = gd_client.GetUserFeed()
  for album in albums.entry:
    if album.title.text == title:
      return album
  return None

def findOrCreateAlbum(gd_client, title):
  album = findAlbum(gd_client, title)
  if not album:
    print "Creating album " + title
    # public, private, protected. private == "anyone with link"
    album = gd_client.InsertAlbum(title=title, summary='test album', access='private')
  return album

def postPhoto(gd_client, album, filename):
  album_url = '/data/feed/api/user/%s/albumid/%s' % (gd_client.email, album.gphoto_id.text)
  photo = gd_client.InsertPhotoSimple(album_url, 'New Photo', 
      'Uploaded using the API', filename, content_type='image/jpeg')
  return photo

def postPhotoToAlbum(gd_client, photo, album):
  album = findOrCreateAlbum(gd_client, args.album)
  photo = postPhoto(gd_client, album, args.source)
  return photo

allExtensions = {}

# key: extension, value: type
knownExtensions = {
  '.png': 'image/png',
  '.jpeg': 'image/jpeg',
  '.jpg': 'image/jpeg',
  '.avi': 'video/avi',
  '.wmv': 'video/wmv',
  '.3gp': 'video/3gp',
  '.m4v': 'video/m4v',
  '.mp4': 'video/mp4',
  '.mov': 'video/mov'
  }

def getMimeType(filename):
  ext = os.path.splitext(filename)[1].lower()
  if ext in knownExtensions:
    return knownExtensions[ext]
  else:
    return None

def accumulateSeenExtensions(filename):
  ext = os.path.splitext(filename)[1].lower()
  if ext in allExtensions:
    allExtensions[ext] = allExtensions[ext] + 1
  else:
    allExtensions[ext] = 1

def isMediaFilename(filename):
  accumulateSeenExtensions(filename)
  return getMimeType(filename) != None

def visit(arg, dirname, names):
  basedirname = os.path.basename(dirname)
  if basedirname.startswith('.'):
    return
  mediaFiles = [name for name in names if not name.startswith('.') and isMediaFilename(name) and
    os.path.isfile(os.path.join(dirname, name))]
  count = len(mediaFiles)
  if count > 0:
    arg[dirname] = {'files': mediaFiles}

def findMedia(source):
  hash = {}
  os.path.walk(source, visit, hash)
  return hash

def findDupDirs(photos):
  d = {}
  for i in photos:
    base = os.path.basename(i)
    if base in d:
      print "duplicate " + base + ":\n" + i + ":\n" + d[base]
      dc = filecmp.dircmp(i, d[base])
      print dc.diff_files
    d[base] = i
  # print [len(photos[i]['files']) for i in photos]
  
def main():
  args = parseArgs()
  # gd_client = login(args.email, args.password)
  # listAlbums(gd_client)
  # postPhotoToAlbum(gd_client, album, args.source)
  photos = findMedia(args.source)
  # findDupDirs(photos)
  print photos
  
main()