moves = {
    'bulbasaur': {
        'vine whip': {
            'power': 30, 'type': 'grass'
        },
        'mud shot': {
            'power': 15, 'type': 'ground'
        },
        'poison dart': {
            'power': 20, 'type': 'poison'
        },
        'x-scissor': {
            'power': 40, 'type': 'bug'
        },
    },

    'charmander': {
        'ember': {
            'power': 30, 'type': 'fire'
        },
        'brick break': {
            'power': 15, 'type': 'fighting'
        },
        'thunder punch': {
            'power': 20, 'type': 'electric'
        },
        'rock throw': {
            'power': 40, 'type': 'rock'
        },
    },

    'squirtle': {
        'water gun': {
            'power': 30, 'type': 'water'
        },
        'ice beam': {
            'power': 15, 'type': 'ice'
        },
        'night slash': {
            'power': 20, 'type': 'ghost'
        },
        'bite': {
            'power': 40, 'type': 'dark'
        },
    },

    'all': {
        'tackle': {
            'power': 30, 'type': 'normal'
        },
        'pound': {
            'power': 30, 'type': 'normal'
        },
        'body slam': {
            'power': 30, 'type': 'normal'
        },
    }
}

pokemon = {
    'bulbasaur': {
        'type': 'Grass',
        'HP': 150
    },
    'charmander': {
        'type': 'Fire',
        'HP': 150
    },
    'squirtle': {
        'type': 'Water',
        'HP': 150
    }
}


def move_choices(choice):
    print('Your move choices are:')
    for move, power in moves.get(choice).items():
        print('{} which is a {} type move and has a base power of {}'.format(move, power.get('type'), power.get('power')))


def pokemon_choice(choice):
    if choice in pokemon:
        print('You have selected %s' % choice)
        print('Your selected pokemon is %s' % pokemon[choice])
    else:
        print('This pokemon is not available.')


def pokemon_stats(pkmn):
    for key, value in pokemon.get(pkmn).items():
        print('Pokemon {} is {}'.format(key,value))


def pokemon_hp(pkmn):
    if pkmn in pokemon:
        return (pokemon[pkmn]['HP'])


def pokemon_type(pkmn):
    if pkmn in pokemon:
        return (pokemon[pkmn]['type'])



p1name = input(
    'Welcome to the world of pokemon, if you could, can you tell me your name?: ').lower()

p1choice = input(
    'Well, % s, If you\'d be so kind as to select a pokemon, your choices are Charmander, Squirtle or Bulbasaur: ' % p1name).lower()

p1_pkmn_hp = pokemon_hp(p1choice)
p1_pkmn_type = pokemon_type(p1choice)

p2name = input(
    'and you there, could you also tell me your name?: ').lower()

p2choice = input(
    '% s! If you\'d also like to pick a Pokemon, again, your choices are Charmander, Squirtle or Bulbasaur: ' % p2name).lower()


battle_initiate = input(
    'Well {}, {}. I feel you should have a battle and test your abilities! Go at it!'.format(p1name, p2name))



