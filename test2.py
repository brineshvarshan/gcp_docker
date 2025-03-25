import requests
from tabulate import tabulate

def fetch_multiple_cricket_matches():
    url = 'https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent'  # For recent matches
    # url = 'https://cricbuzz-cricket.p.rapidapi.com/matches/v1/upcoming'  # For upcoming matches
    headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "4309cbe9e5msh69d6d9f465b9939p10ca40jsn47eb7087c12b"  # Replace with your key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        matches = data.get('typeMatches', [])
        
        if not matches:
            print("No matches found in the API response.")
            return

        for match_type in matches:
            print(f"\n--- {match_type.get('matchType', 'N/A')} ---")
            series_list = match_type.get('seriesMatches', [])
            
            for series in series_list:
                series_wrapper = series.get('seriesAdWrapper', {})
                if not series_wrapper:
                    continue
                
                series_name = series_wrapper.get('series', {}).get('seriesName', 'N/A')
                print(f"\nSeries: {series_name}")
                
                matches_list = series_wrapper.get('matches', [])
                for match in matches_list:
                    match_info = match.get('matchInfo', {})
                    match_score = match.get('matchScore', {})
                    
                    # Prepare match details
                    table = []
                    table.append(["Teams", f"{match_info.get('team1', {}).get('teamName', 'N/A')} vs {match_info.get('team2', {}).get('teamName', 'N/A')}"])
                    table.append(["Match Desc", match_info.get('matchDesc', 'N/A')])
                    table.append(["Format", match_info.get('matchFormat', 'N/A')])
                    table.append(["Status", match_info.get('status', 'N/A')])
                    
                    # Add scores if available
                    if match_score.get('team1Score'):
                        team1_score = match_score['team1Score'].get('inngs1', {})
                        table.append([
                            match_info['team1']['teamName'],
                            f"{team1_score.get('runs', 'N/A')}/{team1_score.get('wickets', 'N/A')} in {team1_score.get('overs', 'N/A')} overs"
                        ])
                    
                    if match_score.get('team2Score'):
                        team2_score = match_score['team2Score'].get('inngs1', {})
                        table.append([
                            match_info['team2']['teamName'],
                            f"{team2_score.get('runs', 'N/A')}/{team2_score.get('wickets', 'N/A')} in {team2_score.get('overs', 'N/A')} overs"
                        ])
                    
                    # Print match details
                    print(tabulate(table, headers=["Key", "Value"], tablefmt="grid"))
                    print("\n" + "-"*50 + "\n")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

fetch_multiple_cricket_matches()