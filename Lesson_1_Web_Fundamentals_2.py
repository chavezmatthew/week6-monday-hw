import requests
import json


def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_data = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet["name"]
            mass = planet["mass"]["massValue"]
            mass_exponent = planet["mass"]["massExponent"]
            orbit_period = planet["sideralOrbit"]
            planet_data.append({
                "name": name,
                "mass": mass,
                "mass_exponent": mass_exponent,
                "orbit_period": orbit_period
            })
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    return planet_data

# fetch_planet_data()

def find_heaviest_planet(planets):
    heaviest_mass = 0
    planet_name = None
    mass_exponent = None
    for planet in planets:
        if planet["mass"] > heaviest_mass:
            heaviest_mass = planet["mass"]
            planet_name = planet["name"]
            mass_exponent = planet["mass_exponent"]
    
    return planet_name, heaviest_mass, mass_exponent

planets = fetch_planet_data()
name, mass, mass_exponent = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {name} with a mass of {mass}*10^{mass_exponent} kg.")


