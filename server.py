import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/api-sports/api/api-hockey'

mcp = FastMCP('api-hockey')

@mcp.tool()
def timezone() -> dict: 
    '''Get the list of available timezone to be used in the games endpoint. > This endpoint does not require any parameters.'''
    url = 'https://api-hockey.p.rapidapi.com/timezone'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def seasons() -> dict: 
    '''All seasons are only 4-digit keys, so for a league whose season is 2018-2019 the season in the API will be 2018. All seasons can be used in other endpoints as filters. > This endpoint does not require any parameters.'''
    url = 'https://api-hockey.p.rapidapi.com/seasons/'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def standings(league: Annotated[Union[int, float], Field(description='The id of the league Default: 3')],
              season: Annotated[Union[int, float], Field(description='The season of the league Default: 2019')],
              team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
              stage: Annotated[Union[str, None], Field(description='A valid stage ')] = None,
              group: Annotated[Union[str, None], Field(description='A valid group ')] = None) -> dict: 
    '''Get the standings for a league. Return a table of one or more rankings according to the league / cup. Some competitions have several rankings in a year, regular season, pre season etc… To know the list of available stages or grou^ you have to use the endpoint standings/stages or standings/groups > Standings are updated every hours'''
    url = 'https://api-hockey.p.rapidapi.com/standings/'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'team': team,
        'stage': stage,
        'group': group,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stages(league: Annotated[Union[int, float], Field(description='The id of the league Default: 3')],
           season: Annotated[Union[int, float], Field(description='The season of the league Default: 2019')]) -> dict: 
    '''Get the list of available stages for a league to be used in the standings endpoint.'''
    url = 'https://api-hockey.p.rapidapi.com/standings/stages'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def groups(league: Annotated[Union[int, float], Field(description='The id of the league Default: 3')],
           season: Annotated[Union[int, float], Field(description='The season of the league Default: 2019')]) -> dict: 
    '''Get the list of available groups for a league to be used in the standings endpoint.'''
    url = 'https://api-hockey.p.rapidapi.com/standings/groups'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_statistics(league: Annotated[Union[int, float], Field(description='The id of the league Default: 3')],
                     season: Annotated[Union[int, float], Field(description='The season of the league Default: 2019')],
                     team: Annotated[Union[int, float], Field(description='The id of the team Default: 17')],
                     date: Annotated[Union[str, datetime, None], Field(description='A date limit ')] = None) -> dict: 
    '''Get Teams statistics for a league and a season'''
    url = 'https://api-hockey.p.rapidapi.com/teams/statistics/'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'team': team,
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_details(id: Annotated[Union[int, float, None], Field(description='The id of the team Default: 135')] = None,
                  name: Annotated[Union[str, None], Field(description='The name of the team ')] = None,
                  country_id: Annotated[Union[int, float, None], Field(description='The id of the country Default: 0')] = None,
                  country: Annotated[Union[str, None], Field(description='The name of the country ')] = None,
                  league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                  season: Annotated[Union[int, float, None], Field(description='The season of the league Default: 0')] = None,
                  search: Annotated[Union[str, None], Field(description='External Docs')] = None) -> dict: 
    '''Get data about teams. The team id are unique in the API and teams keep it among all the leagues/cups in which they participate. > This endpoint requires at least one parameter.'''
    url = 'https://api-hockey.p.rapidapi.com/teams/'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'country_id': country_id,
        'country': country,
        'league': league,
        'season': season,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def leagues(id: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
            name: Annotated[Union[str, None], Field(description='The name of the league ')] = None,
            country_id: Annotated[Union[int, float, None], Field(description='The id of the country Default: 0')] = None,
            country: Annotated[Union[str, None], Field(description='The name of the country ')] = None,
            type: Annotated[Union[str, None], Field(description='The type of the league : league or cup ')] = None,
            season: Annotated[Union[int, float, None], Field(description='The season of the league Default: 0')] = None,
            search: Annotated[Union[str, None], Field(description='External Docs')] = None) -> dict: 
    '''Get the list of available leagues and cups. The league id are unique in the API and leagues keep it across all seasons > Most of the parameters of this endpoint can be used together.'''
    url = 'https://api-hockey.p.rapidapi.com/leagues/'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'country_id': country_id,
        'country': country,
        'type': type,
        'season': season,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def countries(id: Annotated[Union[int, float, None], Field(description='The id of the country Default: 0')] = None,
              name: Annotated[Union[str, None], Field(description='The name of the country ')] = None,
              code: Annotated[Union[str, None], Field(description='The code of the country ')] = None,
              search: Annotated[Union[str, None], Field(description='External Docs')] = None) -> dict: 
    '''Get the list of available countries. The name and code fields can be used in other endpoints as filters. > All the parameters of this endpoint can be used together.'''
    url = 'https://api-hockey.p.rapidapi.com/countries/'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'code': code,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bets(id: Annotated[Union[int, float, None], Field(description='The id of the bet Default: 0')] = None,
         search: Annotated[Union[str, None], Field(description='External Docs')] = None) -> dict: 
    '''Get all available bets. All bets id can be used in endpoint odds as filters'''
    url = 'https://api-hockey.p.rapidapi.com/odds/bets'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bookmakers(id: Annotated[Union[int, float, None], Field(description='The id of the bookmaker Default: 0')] = None,
               search: Annotated[Union[str, None], Field(description='External Docs')] = None) -> dict: 
    '''Get all available bookmakers. All bookmakers id can be used in endpoint odds as filters.'''
    url = 'https://api-hockey.p.rapidapi.com/odds/bookmakers'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def odds(league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
         season: Annotated[Union[int, float, None], Field(description='The season of the league Default: 0')] = None,
         game: Annotated[Union[int, float, None], Field(description='The id of the game Default: 11590')] = None,
         bookmaker: Annotated[Union[int, float, None], Field(description='The id of the bookmaker Default: 0')] = None,
         bet: Annotated[Union[int, float, None], Field(description='The id of the bet Default: 0')] = None) -> dict: 
    '''Get odds from games or leagues. We provide pre-match odds between 1 and 7 days before the game. We keep a 7-day history (The availability of odds may vary according to the leagues, seasons, games and bookmakers) > Odds are updated once a day'''
    url = 'https://api-hockey.p.rapidapi.com/odds/'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'game': game,
        'bookmaker': bookmaker,
        'bet': bet,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_countries(search: Annotated[str, Field(description='External Docs')]) -> dict: 
    '''search countries'''
    url = 'https://api-hockey.p.rapidapi.com/countries/'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_leagues(search: Annotated[str, Field(description='External Docs')]) -> dict: 
    '''Search Leagues'''
    url = 'https://api-hockey.p.rapidapi.com/leagues/'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_bets(search: Annotated[str, Field(description='External Docs')]) -> dict: 
    '''Search Bets'''
    url = 'https://api-hockey.p.rapidapi.com/odds/bets/'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_bookmakers(search: Annotated[str, Field(description='External Docs')]) -> dict: 
    '''Search Bookmakers'''
    url = 'https://api-hockey.p.rapidapi.com/odds/bookmakers/'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_teams(search: Annotated[str, Field(description='External Docs')]) -> dict: 
    '''Search Teams'''
    url = 'https://api-hockey.p.rapidapi.com/teams/'
    headers = {'x-rapidapi-host': 'api-hockey.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
