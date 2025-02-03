import requests
from bs4 import BeautifulSoup

def scrape_match_data(team_name):
    url = f"https://www.sofascore.com/team/football/{team_name.replace(' ', '-').lower()}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract relevant data like recent form, injuries, etc.
    
    return {
        "team": team_name,
        "recent_form": "WDLWW",  # Example format
        "injuries": ["Player A - Hamstring", "Player B - Knee"]
    }
