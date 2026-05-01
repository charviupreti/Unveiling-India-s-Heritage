import wikipedia

# Mapping from monument names to Wikipedia page titles
monument_to_wiki_id = {
    "Ajanta Caves": "Ajanta Caves",
    "alai_darwaza": "Alai Darwaza",
    "alai_minar": "Qutub Minar",
    "basilica_of_bom_jesus": "Basilica of Bom Jesus",
    "Charar-E-Sharif": "Charar-e-Sharief shrine",
    "charminar": "Charminar",
    "Chhota Imambara": "Chota Imambara",
    "Ellora Caves": "Ellora Caves",
    "Fatehpur Sikri": "Jama Mosque",
    "Gateway of India": "Gateway of India",
    "golden temple": "Golden Temple",
    "Hawa mahal": "Hawa Mahal",
    "Hymayun_s Tsomb": "Humayun's Tomb",
    "India_gate": "All India War Memorial",
    "iron_pillar": "Iron Pillar",
    "jamali_kamali_tomb": "Jamali Kamali Mosque and Tomb",
    "Khajuraho": "Lakshmana Temple, Khajuraho",
    "lotus_temple": "LotusTemple",
    "mysore_palace": "Amba Vilas Palace",
    "qutub_minar": "Qutub Minar",
    "Sun Temple Konark": "Konark Sun Temple",
    "tajmahal": "TajMahal",
    "tanjavur temple": "Brihadisvara Temple",
    "victoria memorial": "Victoria Memorial, Kolkata",
}


def get_monument_name(monument):
    return monument_to_wiki_id[monument]


def summarize(monument, lines=10):
    """
    Fetches and returns a summary of the given monument from Wikipedia.

    Parameters:
    monument (str): The name of the monument to summarize.

    Returns:
    str: A summary of the given monument.
    """

    # Using a dictionary to get wikipedia ID of the monument
    monument_id = get_monument_name(monument)

    # Using summary function of wikipedia
    summary = wikipedia.summary(monument_id, sentences=lines)

    return summary
