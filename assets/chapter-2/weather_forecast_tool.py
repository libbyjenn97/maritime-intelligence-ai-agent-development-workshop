"""
Weather Forecast Tool for watsonx Orchestrate
Retrieves weather data using the Open-Meteo API
"""

import requests
from typing import Dict, Any, Optional
import json


def get_weather_forecast(
    latitude: float,
    longitude: float,
    forecast_days: int = 7
) -> Dict[str, Any]:
    """
    Retrieve weather forecast data from Open-Meteo API.
    
    This function fetches current weather conditions and daily forecasts for a specified
    location using latitude and longitude coordinates. The data is retrieved from the
    Open-Meteo API which requires no API key.
    
    Args:
        latitude (float): Latitude coordinate of the location (-90 to 90)
        longitude (float): Longitude coordinate of the location (-180 to 180)
        forecast_days (int, optional): Number of forecast days to retrieve (1-16). 
                                       Defaults to 7.
    
    Returns:
        Dict[str, Any]: A dictionary containing:
            - status (str): "success" or "error"
            - data (dict): Weather data including current conditions and daily forecast
            - error (str): Error message if status is "error"
            
    Raises:
        None: All exceptions are caught and returned in the response dictionary
        
    Example:
        >>> result = get_weather_forecast(-41.2865, 174.7762, forecast_days=5)
        >>> if result["status"] == "success":
        ...     print(result["data"]["current"]["temperature_2m"])
    """
    
    # Validate input coordinates
    if not isinstance(latitude, (int, float)) or not isinstance(longitude, (int, float)):
        return {
            "status": "error",
            "error": "Invalid coordinate types. Latitude and longitude must be numeric values.",
            "data": None
        }
    
    if not -90 <= latitude <= 90:
        return {
            "status": "error",
            "error": f"Invalid latitude: {latitude}. Must be between -90 and 90.",
            "data": None
        }
    
    if not -180 <= longitude <= 180:
        return {
            "status": "error",
            "error": f"Invalid longitude: {longitude}. Must be between -180 and 180.",
            "data": None
        }
    
    # Validate forecast_days parameter
    if not isinstance(forecast_days, int) or not 1 <= forecast_days <= 16:
        return {
            "status": "error",
            "error": f"Invalid forecast_days: {forecast_days}. Must be an integer between 1 and 16.",
            "data": None
        }
    
    # Construct API URL with parameters
    base_url = "https://api.open-meteo.com/v1/forecast"
    
    # Define current weather parameters
    current_params = [
        "temperature_2m",
        "relative_humidity_2m",
        "wind_speed_10m",
        "wind_direction_10m",
        "weather_code"
    ]
    
    # Define daily forecast parameters
    daily_params = [
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "wind_speed_10m_max",
        "weather_code"
    ]
    
    # Build query parameters
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ",".join(current_params),
        "daily": ",".join(daily_params),
        "timezone": "Pacific/Auckland",
        "forecast_days": forecast_days
    }
    
    try:
        # Make API request with timeout
        response = requests.get(
            base_url,
            params=params,
            timeout=10  # 10 second timeout
        )
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse JSON response
        weather_data = response.json()
        
        # Structure the output
        result = {
            "status": "success",
            "data": {
                "location": {
                    "latitude": weather_data.get("latitude"),
                    "longitude": weather_data.get("longitude"),
                    "timezone": weather_data.get("timezone"),
                    "elevation": weather_data.get("elevation")
                },
                "current": {
                    "time": weather_data.get("current", {}).get("time"),
                    "temperature_2m": weather_data.get("current", {}).get("temperature_2m"),
                    "relative_humidity_2m": weather_data.get("current", {}).get("relative_humidity_2m"),
                    "wind_speed_10m": weather_data.get("current", {}).get("wind_speed_10m"),
                    "wind_direction_10m": weather_data.get("current", {}).get("wind_direction_10m"),
                    "weather_code": weather_data.get("current", {}).get("weather_code")
                },
                "daily": {
                    "time": weather_data.get("daily", {}).get("time", []),
                    "temperature_2m_max": weather_data.get("daily", {}).get("temperature_2m_max", []),
                    "temperature_2m_min": weather_data.get("daily", {}).get("temperature_2m_min", []),
                    "precipitation_sum": weather_data.get("daily", {}).get("precipitation_sum", []),
                    "wind_speed_10m_max": weather_data.get("daily", {}).get("wind_speed_10m_max", []),
                    "weather_code": weather_data.get("daily", {}).get("weather_code", [])
                },
                "units": {
                    "current": weather_data.get("current_units", {}),
                    "daily": weather_data.get("daily_units", {})
                }
            },
            "error": None
        }
        
        return result
        
    except requests.exceptions.Timeout:
        # Handle timeout errors
        return {
            "status": "error",
            "error": "Request timeout: The API did not respond within 10 seconds. Please try again.",
            "data": None
        }
    
    except requests.exceptions.ConnectionError:
        # Handle connection errors
        return {
            "status": "error",
            "error": "Connection error: Unable to connect to the Open-Meteo API. Please check your internet connection.",
            "data": None
        }
    
    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors (4xx, 5xx status codes)
        return {
            "status": "error",
            "error": f"HTTP error: {e.response.status_code} - {e.response.reason}",
            "data": None
        }
    
    except requests.exceptions.RequestException as e:
        # Handle any other requests-related errors
        return {
            "status": "error",
            "error": f"Request error: {str(e)}",
            "data": None
        }
    
    except json.JSONDecodeError:
        # Handle JSON parsing errors
        return {
            "status": "error",
            "error": "Failed to parse API response. The server returned invalid JSON.",
            "data": None
        }
    
    except Exception as e:
        # Handle any unexpected errors
        return {
            "status": "error",
            "error": f"Unexpected error: {str(e)}",
            "data": None
        }


# Example usage and testing
if __name__ == "__main__":
    # Test with Wellington, New Zealand coordinates
    print("Testing weather forecast tool...")
    print("-" * 50)
    
    # Test 1: Valid coordinates (Wellington, NZ)
    print("\nTest 1: Wellington, New Zealand")
    result = get_weather_forecast(-41.2865, 174.7762, forecast_days=5)
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        print(f"Current Temperature: {result['data']['current']['temperature_2m']}°C")
        print(f"Current Humidity: {result['data']['current']['relative_humidity_2m']}%")
        print(f"Forecast Days: {len(result['data']['daily']['time'])}")
    else:
        print(f"Error: {result['error']}")
    
    # Test 2: Invalid latitude
    print("\nTest 2: Invalid latitude")
    result = get_weather_forecast(95.0, 174.7762)
    print(f"Status: {result['status']}")
    print(f"Error: {result['error']}")
    
    # Test 3: Invalid longitude
    print("\nTest 3: Invalid longitude")
    result = get_weather_forecast(-41.2865, 200.0)
    print(f"Status: {result['status']}")
    print(f"Error: {result['error']}")
    
    # Test 4: Invalid forecast_days
    print("\nTest 4: Invalid forecast_days")
    result = get_weather_forecast(-41.2865, 174.7762, forecast_days=20)
    print(f"Status: {result['status']}")
    print(f"Error: {result['error']}")
    
    print("\n" + "-" * 50)
    print("Testing complete!")

# Made with Bob
