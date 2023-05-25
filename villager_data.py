"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()
    data_file = open(filename)
    for data in data_file:
        line_species = data.rstrip().split("|")[1]
        species.add(line_species)

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    data_file = open(filename)
    for data in data_file:
        line_names, species = data.rstrip().split("|")[:2] 
                                                
        if search_string in ("All", species):
            villagers.append(line_names)

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

    education = []
    fitness = []
    fashion = []
    nature = []
    music = []
    play = []

    data_file = open(filename)
    for data in data_file:
        name, species, personality, hobby, motto = data.rstrip().split("|")

        if hobby == "Education":
            education.append(name)
        elif hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)
        elif hobby == "Music":
            music.append(name)

    return [sorted(fitness), sorted(nature), sorted(education),
            sorted(music), sorted(fashion), sorted(play)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    data_file = open(filename)

    for data in data_file:
        all_data.append(tuple(data.rstrip().split("|")))

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    for name, species, personality, hobby, motto in all_data(filename):
        if name == villager_name:
            return motto or None


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
    
    likeminded = set()

    target_personality = None
    for villager_data in all_data(filename):
        name, _, personality = villager_data[:3]

        if name == villager_name:
            target_personality = personality
            break
    
    if target_personality:
        for villager_data in all_data(filename):
            name, _, personality = villager_data[:3]
            if personality == target_personality:
                likeminded.add(name)

    

    return likeminded