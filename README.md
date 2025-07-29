# API-HOCKEY MCP Server

## Overview

API-HOCKEY is a comprehensive API designed to provide a wide array of data related to hockey leagues and cups. This freemium service offers real-time livescores, odds, bookmakers insights, detailed statistics, standings, historical data, and more across over 245 hockey leagues and cups worldwide.

## Features

- **Livescore and Standings**: Access real-time scores and standings for over 250 hockey leagues and cups. View rankings for regular seasons, pre-seasons, and more.
- **Odds and Bookmakers**: Retrieve pre-match odds and bookmaker information. Access historical odds data up to 7 days before the game.
- **Team and League Data**: Get detailed information about teams, leagues, and their respective statistics.
- **Country and Season Information**: Explore data by country or season, with 4-digit season keys for easy filtration.
- **Widgets**: Utilize available widgets for enhanced integration and display.

## Tool List

### Timezone
- **Function**: Get the list of available timezones to be used in the games endpoint.

### Seasons
- **Function**: Access all available seasons. Useful as filters in other endpoints.

### Standings
- **Function**: Retrieve standings for leagues. Includes various rankings and stages throughout the year.

### Teams
- **Teams Statistics**: Get statistics for teams within a specific league and season.
- **Teams Details**: Obtain data about teams, including unique team IDs across leagues/cups.

### Leagues
- **Function**: Access the list of available leagues and cups. Unique league IDs are consistent across all seasons.

### Countries
- **Function**: Retrieve a list of available countries. Use name and code fields as filters.

### Odds
- **Bets**: Access all available bets for use in odds filtering.
- **Bookmakers**: Get information about available bookmakers.
- **Odds**: Retrieve odds from games or leagues, updated daily.

### Search
- **Search Countries**: Search available countries.
- **Search Leagues**: Search leagues.
- **Search Bets**: Search available bets.
- **Search Bookmakers**: Search available bookmakers.
- **Search Teams**: Search teams within the API.

## Authentication

API-HOCKEY uses API keys to manage access. Ensure your API key is included in all requests to authenticate and access the API's resources.

## Request Headers

- Only **GET** requests are supported.
- Allowed headers:
  - `x-rapidapi-host`
  - `x-rapidapi-key`

Ensure that no extra headers are added, as this may result in errors.

## Architecture

API-HOCKEY is built to deliver high availability and low latency, ensuring seamless access to data. The server architecture supports efficient data retrieval and processing to meet user demands.

## Usage Analytics

While using API-HOCKEY, you can monitor API request metrics, error rates, and latency to optimize usage and performance.

## Response Headers

Upon consuming the API, expect to receive the following headers in the response:

- `server`: Current version of the API proxy.
- `x-ratelimit-requests-limit`: Maximum number of requests allowed based on your subscription plan.
- `x-ratelimit-requests-remaining`: Number of remaining requests before reaching your plan's limit.

API-HOCKEY offers a robust set of tools and data to support a wide range of hockey-related applications, from live score tracking to detailed statistical analysis.