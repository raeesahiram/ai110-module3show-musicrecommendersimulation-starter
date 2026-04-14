from src.recommender import load_songs, recommend_songs

songs = load_songs("data/songs.csv")
profiles = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.85,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.92,
        "likes_acoustic": False,
    },
    "Conflicting Energy + Mood": {
        "favorite_genre": "pop",
        "favorite_mood": "relaxed",
        "target_energy": 0.90,
        "likes_acoustic": False,
    },
    "Genre vs Acoustic Mismatch": {
        "favorite_genre": "electronic",
        "favorite_mood": "peaceful",
        "target_energy": 0.30,
        "likes_acoustic": True,
    },
}

print("Loaded songs:", len(songs))
for name, profile in profiles.items():
    print(f"\nPROFILE: {name}")
    recs = recommend_songs(profile, songs, k=5)
    for i, (song, score, explanation) in enumerate(recs, start=1):
        print(f"{i}. {song['title']} by {song['artist']} - {score:.2f}")
        print(f"   {explanation}")
