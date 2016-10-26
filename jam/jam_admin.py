from datetime import datetime

from django.shortcuts import get_object_or_404, render
from django.http import  Http404, HttpResponse

from jam.models import Artists, Album
from jam.spotify_api import *

###################
#   ADMIN FUNCTIONS
###################

def add_artist(request, artist_query):
    artist_query = url_argument_parse(artist_query)
    json_Search_response_artist, json_Search_response_album = spotify_gen_search(artist_query)

    spotify_Artist_ID = json_Search_response_artist['artists']['items'][0]['id']
    spotify_Artist_Name = json_Search_response_artist['artists']['items'][0]['name']

    if (json_Search_response_artist['artists']['items'][0]['genres'] != [ ]):
            spotify_Primary_Genre = json_Search_response_artist['artists']['items'][0]['genres'][0]
            try: 
                spotify_Secondary_Genre = json_Search_response_artist['artists']['items'][0]['genres'][1]
            except IndexError:
                spotify_Secondary_Genre = 'undefined'
    else:
        spotify_Primary_Genre = 'undefined'
        spotify_Secondary_Genre = 'undefined'

    new_artist = Artists.objects.create(ArtistName=spotify_Artist_Name, SpotifyID=spotify_Artist_ID, PrimaryGenre=spotify_Primary_Genre, SecondaryGenre=spotify_Secondary_Genre)
    new_artist.save()

    # temp success page redirect
    now = datetime.strftime("%Y-%m-%d %H:%M:%S", gmtime())
    page_title = "Evan"
    pic_url = urllib2.urlopen("https://farm2.staticflickr.com/1627/24943678040_d9637bdeee_c.jpg")
    return render(request, 'time.html', {'current_time': now, 'page_title': page_title})


def add_album(request, album_query):
    album_query = url_argument_parse(album_query)
    json_Search_response_artist, json_Search_response_album = spotify_gen_search(album_query)

    spotify_Album_ID = json_Search_response_album['albums']['items'][0]['id']
    spotify_Album_Name = json_Search_response_album['albums']['items'][0]['name']

    json_Search_response_album = spotify_album_search(spotify_Album_ID)
    spotify_Artist_ID = json_Search_response_album["artists"][0]["id"]
    spotify_Artist_Name = json_Search_response_album["artists"][0]["name"]

    artist = Artists.objects.filter(SpotifyID=spotify_Artist_ID)
    artist = list(artist[:1])

    new_album = Album.objects.create(AlbumTitle=spotify_Album_Name, SpotifyAlbumID=spotify_Album_ID, ArtistID=artist[0])
    new_album.save()


    now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    page_title = "Successfully added " + spotify_Album_Name
    return render(request, 'time.html', {'current_time': now, 'page_title': page_title})

def add_review(request):
    return render(request, 'add_review.html')

