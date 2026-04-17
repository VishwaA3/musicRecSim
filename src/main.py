"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9
        },

        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.3
        },

        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95
        }
    }

    for name, user_prefs in profiles.items():
        print("\n" + "="*50)
        print(f"PROFILE: {name}")
        print("="*50)

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\nTop recommendations:\n")
        for song, score, explanation in recommendations:
            # You decide the structure of each returned item.
            # A common pattern is: (song, score, explanation)
            print(f"{song['title']} — {song['artist']}")
            print(f"Score: {score:.2f}")
            print(f"Reasons: {explanation}")
            print("-" * 40)


if __name__ == "__main__":
    main()
