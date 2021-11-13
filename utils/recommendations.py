import collections
import math

from typing import List

from api.models import Program, Composition

MAX_DIFFICULTY_DELTA = 2


def can_add(comp, avg):
    return abs(comp.difficulty - avg) < MAX_DIFFICULTY_DELTA


def delete_from_frequency(frequency, composition):
    for freq in frequency:
        comps = frequency[freq]
        for comp in comps:
            if comp.id == composition.id:
                frequency[freq].remove(comp)
                return frequency
    raise Exception("No composition in frequency")


def new_avg(music_list, count, avg):
    sum_diff = avg * (count - len(music_list) + 1)
    sum_diff -= music_list[-1].difficulty
    try:
        new = sum_diff / (count - len(music_list))
    except:
        return None
    return new


def find_best(music_list, count, avg, frequency):
    buffer = list()
    for freq in frequency:
        comps = frequency[freq]
        buffer.extend(comps)
        if len(buffer) != 0:
            best = buffer[0]
            best_val = buffer[0].difficulty
            for comp in buffer:
                delta = abs(comp.difficulty - avg)
                if delta < best_val:
                    best_val = delta
                    best = comp
            if can_add(best, avg):
                music_list.append(best)
                avg = new_avg(music_list, count, avg)
                return music_list, avg
    raise Exception("Can't find best composition")


def get_frequency_list(programs: List[Program]):
    frequency = dict()
    for composition in Composition.objects.all():
        frequency[composition] = 0
    for program in programs:
        for comp in program.compositions.all():
            if frequency[comp]:
                frequency[comp] += 1
            else:
                frequency[comp] = 1
    reversed = dict()
    for key in frequency:
        if frequency[key] in reversed:
            reversed[frequency[key]].append(key)
        else:
            reversed[frequency[key]] = [key]
    reversed = collections.OrderedDict(sorted(reversed.items()))

    return reversed


def get_recommendations(program: Program, MAX_DIFFICULTY_DELTA=MAX_DIFFICULTY_DELTA):
    concert = program.concert
    other_programs = Program.objects.filter(concert_id=concert.id).all()
    composition_count = program.semester.composition_count
    max_difficulty = program.semester.max_difficulty
    min_difficulty = program.semester.min_difficulty

    avg_difficulty = (max_difficulty + min_difficulty) / 2 / composition_count
    frequency = get_frequency_list(other_programs)
    music_list = []

    while len(music_list) != composition_count:
        try:
            music_list, avg_difficulty = find_best(music_list, composition_count, avg_difficulty, frequency)
            frequency = delete_from_frequency(frequency, music_list[-1])
        except:
            MAX_DIFFICULTY_DELTA += 1

    return music_list