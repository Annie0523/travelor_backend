import os
import json



# ================== SAMPLE DATA ==================
cities_data = [
    {
        "name": "Tokyo",
        "value": "tokyo",
        "position": [35.6895, 139.6917],
        "category": "cultural",
        "interest": "technology",
    },
    {
        "name": "Mumbai",
        "value": "mumbai",
        "position": [19.0760, 72.8777],
        "category": "cultural",
        "interest": "bollywood",
    },
    {
        "name": "Cairo",
        "value": "cairo",
        "position": [30.0444, 31.2357],
        "category": "historical",
        "interest": "pyramids",
    },
    {
        "name": "Lagos",
        "value": "lagos",
        "position": [6.5244, 3.3792],
        "category": "cultural",
        "interest": "afrobeat",
    },
    {
        "name": "London",
        "value": "london",
        "position": [51.5074, -0.1278],
        "category": "historical",
        "interest": "theatre",
    },
    {
        "name": "Paris",
        "value": "paris",
        "position": [48.8566, 2.3522],
        "category": "cultural",
        "interest": "fashion",
    },
    {
        "name": "New York City",
        "value": "new_york_city",
        "position": [40.7128, -74.0060],
        "category": "cultural",
        "interest": "broadway",
    },
    {
        "name": "Mexico City",
        "value": "mexico_city",
        "position": [19.4326, -99.1332],
        "category": "historical",
        "interest": "art",
    },
    {
        "name": "São Paulo",
        "value": "sao_paulo",
        "position": [-23.5505, -46.6333],
        "category": "cultural",
        "interest": "nightlife",
    },
    {
        "name": "Buenos Aires",
        "value": "buenos_aires",
        "position": [-34.6037, -58.3816],
        "category": "historical",
        "interest": "tango",
    },
]