import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    songs: List[Dict] = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            songs.append({
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness']),
            })
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute a score and explanation reasons for one song."""
    # Accept either the short keys used by main.py or the full UserProfile style keys.
    genre_key = user_prefs.get('favorite_genre', user_prefs.get('genre'))
    mood_key = user_prefs.get('favorite_mood', user_prefs.get('mood'))
    energy_key = user_prefs.get('target_energy', user_prefs.get('energy'))

    score = 0.0
    reasons: List[str] = []

    if genre_key is not None and song.get('genre') == genre_key:
        score += 2.0
        reasons.append('genre match (+2.0)')
    else:
        reasons.append('genre mismatch (+0.0)')

    if mood_key is not None and song.get('mood') == mood_key:
        score += 1.0
        reasons.append('mood match (+1.0)')
    else:
        reasons.append('mood mismatch (+0.0)')

    if energy_key is not None:
        energy_distance = abs(song.get('energy', 0.0) - float(energy_key))
        energy_score = max(0.0, 1.0 - energy_distance)
        score += energy_score
        reasons.append(f'energy similarity (+{energy_score:.2f})')
    else:
        reasons.append('energy preference missing (+0.0)')

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top K recommendations."""
    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked_songs[:k]
