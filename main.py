from features.Character import Character
from features.Comics import Comics
from features.Events import Events
from features.Series import Series
from features.Stories import Stories


def main():
    character = Character()
    comics = Comics()
    events = Events()
    series = Series()
    stories = Stories()

    while True:
        print("\n--- Menú de Marvel API ---")
        print("1. Obtener todos los personajes")
        print("2. Obtener un personaje por ID")
        print("3. Obtener todos los comics y todos los comics de un personaje")
        print("4. Obtener todos los eventos y todos los eventos de un personaje")
        print("5. Obtener todas las series y todas las series de un personaje")
        print("6. Obtener todas las historias y todas las historias de un personaje")
        print("7. Salir")

        choice = input("Elija una opción (1-7): ")

        if choice == '1':
            characters = character.get_characters()
            print(characters)
        elif choice == '2':
            character_by_id = character.getCharacterbyId(1011334)
            print(character_by_id)
        elif choice == '3':
            comics = comics.getComics()
            print(comics)
            print("\n")
            comics_by_character = comics.getComicsbyCharacter(1011334)
            print(comics_by_character)
        elif choice == '4':
            events = events.getEvents()
            print(events)
            print("\n")
            events_by_character = events.getEventsbyCharacter(1011334)
            print(events_by_character)
        elif choice == '5':
            series = series.getSeries()
            print(series)
            print("\n")
            series_by_character = series.getSeriesbyCharacter(1011334)
            print(series_by_character)
        elif choice == '6':
            stories = stories.getStories()
            print(stories)
            print("\n")
            stories_by_character = stories.getStoriesbyCharacter(1011334)
            print(stories_by_character)
        elif choice == '7':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor elige una opción entre 1 y 7.")

if __name__ == "__main__":
    main()