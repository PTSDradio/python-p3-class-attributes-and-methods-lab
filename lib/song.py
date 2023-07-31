class Song:
    count = 0
    genres = []
    genre_count={}
    artists = []
    artist_count={}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.increase_count()
        self.add_to_genres(genre)
        self.add_to_genre_count(genre)
        self.add_to_artists(artist)
        self.add_to_artist_count(artist)

    pass

    @classmethod
    def increase_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre]= 1
        elif genre in cls.genre_count:
            cls.genre_count[genre]+= 1
        pass

    def add_to_artists(cls, artist):
       if artist not in cls.artists:
           cls.artists.append(artist)

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist]= 1
        elif artist in cls.artist_count:
            cls.artist_count[artist]+= 1
        pass
