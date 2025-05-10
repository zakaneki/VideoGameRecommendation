import requests

# Replace these with your actual Client ID and Client Secret
CLIENT_ID = '99o9s3clx1qlil5bfxht4au3mtpesb'
CLIENT_SECRET = 'j2z3b57u2pm0k1umoci0z4vzzsgkw1'

def get_access_token(client_id, client_secret):
    # Endpoint for Twitch OAuth token
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    
    response = requests.post(url, params=params)
    response.raise_for_status()
    data = response.json()
    print("Time to get access token:", data['expires_in'], "seconds")
    return data['access_token']

def query_igdb(access_token, endpoint, body):
    # IGDB API URL
    url = f'https://api.igdb.com/v4/{endpoint}'
    
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {access_token}'
    }
    
    response = requests.post(url, headers=headers, data=body)
    response.raise_for_status()
    return response.json()

def main():
    # Step 1: Get access token
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    print("Access Token:", access_token)
    
    # Step 2: Use the token to query IGDB
    # Example: Get the first 5 games with their name and release date
    igdb_body = '''
        fields *; 
        limit 10;
    '''

    # Replace 'games' with your desired IGDB endpoint
    response_data = query_igdb(access_token, 'games', igdb_body)
    print("IGDB Response:", response_data)

if __name__ == '__main__':
    main()