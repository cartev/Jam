# from jam.models import Artists, Album

class Singleton(type):
	
    instance = None
    def __call__(cls, *args, **kwargs):
        if cls.instance is None :
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance

# Singleton is the metaclass that manages the instance of class Cache
class Cache():#object, metaclass = Singleton):
    
    albumCache = set()
    artistCache = set()

    # search for artist
    def searchArtist(self, name):
        if name in self.artistCache:
            return artistCache[name]
        return readThrough(artistCache, name)

    def searchAlbum(self, name):
        if name in self.albumCache[name]:
            return albumCache[name]
        return readThrough(albumCache, name)
	
    # called if Cache miss, read DB and replace in Cache
    def readThrough(cacheSet, replacement):
       
        if type(cacheSet[0]) == Artists:
            newCacheItem = Artists.objects.get(ArtistName=replacement)
        else:
            newCacheItem = Album.objects.get(AlbumTitle=replacement)

        if len(cacheSet) < 101:
            cacheSet.add(newCacheItem) # load new item
        else:
            cacheSet.pop() # evict arbitrary element
            cacheSet.add(newCacheItem) # replace with new item
        return newCacheItem


##############
#        TESTS
##############

# print (hasattr(Cache, "albumCache")) # attributed
# print (hasattr(Cache, "artistCache"))
# print (Cache.albumCache)

# # a = Cache(5) # TypeError "object() takes no parameters" / no __init__() w/ parameters
# a = Cache() # Instance is created in memory
# b = Cache(5) # If 2nd __call__(), returns Single Cache instance, regardless of parameters provided 

# c = Cache().albumCache
# d = b.albumCache 

# print (a is b) # reference same singleton object in memory
# print (c is d) # reference same attribute object in memory
