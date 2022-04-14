import requests
def get_pokemon_info(name):
    """
    Gets a dictionary of information from the PokeaAPi from a pokemon
    :param name : Pokemons name 
    """
    print("Getting pokemon information...", end="")
    if name is None:
        return

    name = name.lower().strip()
    if name == '':
        return
    
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(name))

    if response.status_code == 200:
        print("Success")
        return  response.json()
    else:
        print('Failed. Response code:',response.status_code)
        return