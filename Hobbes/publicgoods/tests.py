from django.test import TestCase
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from publicgoods.models import Game_Instance, Game_Response

from gametheory import pseudonym_generator

def fullOnlineTest():
    g = Game_Instance(instance_name="PHILO 100",
            time_opened=timezone.now(),
            instructor_password= make_password("pass"),
            user_keyword="key",
            endowment=5,
            max_contribution=5)

    g.save()

    addTestUser(g, 0, 'Connor Cottenmyre', 'connor37', pseudonym_generator.random_pseudonym())

    addTestUser(g, 0, 'Luke Fringer', 'lukefringer7', pseudonym_generator.random_pseudonym())

    addTestUser(g, 0, 'Kelsey Gibbs', 'kjgibbs', pseudonym_generator.random_pseudonym())
    addTestUser(g, 0, 'Kirk Iseli', 'kiseli', pseudonym_generator.random_pseudonym())
    addTestUser(g, 0, 'Kyler Thompson', 'kyler8911', pseudonym_generator.random_pseudonym())

    addTestUser(g, 0, 'Walter Neil', 'walnutdb4', pseudonym_generator.random_pseudonym())
    addTestUser(g, 0, 'Nathan Rosario', 'nmrosario', pseudonym_generator.random_pseudonym())
    addTestUser(g, 0, 'Hawa Dembele', 'hpdembele', pseudonym_generator.random_pseudonym())

    addTestUser(g, 2, 'Alex Galey', 'alexjgaley', pseudonym_generator.random_pseudonym())

    addTestUser(g, 0, 'Caitlin Garcia', 'cggarcia', pseudonym_generator.random_pseudonym())

    addTestUser(g, 1, 'Anya Gleichmann', 'anyag', pseudonym_generator.random_pseudonym())

    addTestUser(g, 5, 'Emily Heinking', 'eeheinki', pseudonym_generator.random_pseudonym())

    addTestUser(g, 5, 'Kyra Lampe', 'ktlampe', pseudonym_generator.random_pseudonym())

    addTestUser(g, 0, 'Sarah Millard', 'semillard', pseudonym_generator.random_pseudonym())

    addTestUser(g, 4.25, 'Madison Rios', 'mkate7', pseudonym_generator.random_pseudonym())

    addTestUser(g, 2, 'Alexias Rose', 'amrose', pseudonym_generator.random_pseudonym())

    addTestUser(g, 0, 'Isabel Schmidt', 'icschmid', pseudonym_generator.random_pseudonym())

    addTestUser(g, .11, 'Austin Slobodzian', 'austinslobo', pseudonym_generator.random_pseudonym())

    addTestUser(g, 2, 'Sara Sullivan', 'scsulliv', pseudonym_generator.random_pseudonym())

    addTestUser(g, 4, 'Lake Winter', 'lrwinter', pseudonym_generator.random_pseudonym())

    addTestUser(g, 2, 'Samantha Stoss', 'sstoss1570', pseudonym_generator.random_pseudonym())

    addTestUser(g, 0, 'Ethan Rice', 'ethancole99', pseudonym_generator.random_pseudonym())

    addTestUser(g, 3.33, 'Jennah Ohlde', 'jnohlde', pseudonym_generator.random_pseudonym())

def addTestUser(instance, contribution, name, eid, pseudonym):
    r = Game_Response(game=instance,
            contribution=contribution,
            name=name,
            eid=eid,
            pseudonym=pseudonym)
    r.save()

