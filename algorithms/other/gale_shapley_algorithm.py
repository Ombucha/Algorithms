class Person:

    def __init__(self, identifier: str | int, preferences: list[str | int]) -> None:
        self.identifier = identifier
        self.preferences = preferences
        self.partner = None

    def __str__(self) -> str:
        return str(self.identifier)

def fetch_person(people: list[Person], identifier: str | int) -> Person | None:
    for person in people:
        if person.identifier == identifier:
            return person
    return None

def gale_shapley_algorithm(males: list[Person], females: list[Person]) -> list[tuple[Person, Person]]:
    unmatched_males = males
    rejected_pairs = []
    matching = []
    while len(unmatched_males) > 0:
        male = unmatched_males[0]
        for identifier in male.preferences:
            if (male.identifier, identifier) not in rejected_pairs:
                female = fetch_person(females, identifier)
                break
        if female.partner is None or female.preferences.index(female.partner.identifier) < female.preferences.index(male.identifier):
            if female.partner is not None:
                matching.remove((female.partner, female))
                unmatched_males.append(female.partner)
            matching.append((male, female))
            male.partner, female.partner = female, male
            unmatched_males.remove(male)
        else:
            rejected_pairs.append((male.identifier, female.identifier))
    return matching
