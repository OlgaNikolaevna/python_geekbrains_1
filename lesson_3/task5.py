# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import choice


def get_jokes(n, is_notrepeatable):
    """Generates n jokes from random nouns, adverbs, adjectives

    :param n: number of jokes
    :param is_notrepeatable: prevent repeat of words
    :return: list of jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    for i in range(0, n):
        if len(nouns) and len(adverbs) and len(adjectives):
            noun = choice(nouns)
            adv = choice(adverbs)
            adj = choice(adjectives)
            if is_notrepeatable:
                nouns.remove(noun)
                adverbs.remove(adv)
                adjectives.remove(adj)
            joke = noun + " " + adv + " " + adj
        else:
            joke = 'jokes are finished'
        jokes.append(joke)
    return jokes


print(get_jokes(n=5, is_notrepeatable=False))
print(get_jokes(n=10, is_notrepeatable=True))