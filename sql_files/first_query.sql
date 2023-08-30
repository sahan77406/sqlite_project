SELECT albums.AlbumId, albums.Title, albums.ArtistId
FROM albums
JOIN artists ON albums.ArtistId = artists.ArtistId;
