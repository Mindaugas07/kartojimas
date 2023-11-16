from typing import Dict, List
 
 
person = {
    "name": "Vytautas",
    "surname": "Sluckas",
    "ip": "127.0.0.1",
    "programming_language": "python",
    "address": {"Street": "some street", "House Number": "some house number"},
    "languages": ["Lithuanian", "English", "Norwegian"]
}
 
person1 = {
    "name": "Tomas",
    "surname": "BLABLABA",
    "ip": "127.0.0.1",
    "programming_language": "python",
    "address": {"Street": "some street", "House Number": "some house number"},
    "languages": ["Latvian", "English", "Swedish"]
}
 
people = [person, person1]
 


def get_most_popular_language(people: List[Dict]) -> str:
    # create dictionary with language counts
    # for person in people:
        # get persons languages
        # for language in languages:
            # if language is new:
                # add key to dictionary with language counts
            # else if langauge is not new:
                # add count +1 to already existing language in dictionary with language counts
    languages_dictionary = {}
    for person in people:
        languages = person.get("languages")
        for language in languages:
            languages_dictionary[language] = languages_dictionary.get(language, 0) + 1


    max_key = None
    max_value = None
    for key, value in languages_dictionary.items():
        if max_value == None or max_value < value:
            max_key, max_value = key, value
    return max_key

   
    # return max(languages_dictionary, key=languages_dictionary.get)

print(get_most_popular_language(people))