from playlist_service import PlaylistService
from confirmation import Confirmation
self.playlist_service = PlaylistService()
    def choose_playlist(self):
        print("\nБажаєте додати опцію 'Ідеальний Плейлист'? (yes/no)")
        choice = input("> ").lower()

        if choice != "yes":
            return None, None

        print("\nОберіть настрій або жанр:")
        for mood in self.playlist_service.playlists.keys():
            print(f"- {mood}")

        selected = input("\nВаш вибір: ")

        link = self.playlist_service.get_playlist_link(selected)

        if link:
            print("Плейлист додано!")
            return selected, link
        else:
            print("Такого плейлиста нема.")
            return None, None
if car.available:
    car.available = True

    playlist_name, playlist_link = self.choose_playlist()

    self.update_csv()
    print(f"Автомобіль {car.brand} {car.model} успішно заброньовано.")

    return Confirmation(car, playlist_name, playlist_link)

