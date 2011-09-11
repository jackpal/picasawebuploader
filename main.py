import argparse
import gdata.photos.service
import gdata.media
import gdata.geo

def parseArgs():
  parser = argparse.ArgumentParser(description='Upload pictures to picasa web albums / Google+.')
  parser.add_argument('--email', help='the google account email to use (example@gmail.com)', required=True)
  parser.add_argument('--password', help='the password', required=True)
  parser.add_argument('--source', help='the photo to upload', required=True)
  parser.add_argument('--album', help='the album to upload to', required=True)

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
    album = gd_client.InsertAlbum(title=title, summary='test album', access='private')
  return album

def postPhoto(gd_client, email, album, filename):
  album_url = '/data/feed/api/user/%s/albumid/%s' % (email, album.gphoto_id.text)
  photo = gd_client.InsertPhotoSimple(album_url, 'New Photo', 
      'Uploaded using the API', filename, content_type='image/jpeg')
  return photo

def main():
  args = parseArgs()
  gd_client = login(args.email, args.password)
  # listAlbums(gd_client)
  album = findOrCreateAlbum(gd_client, args.album)
  postPhoto(gd_client, args.email, album, args.source)
main()