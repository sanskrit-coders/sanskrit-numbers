CARDINALS = {1: "eka", 2: "dvi", 3: "tri", 4: "catuH", 5: "paJca", 6: "SaT",
             7: "sapta", 8: "aSTa", 9: "nava", 10: "daza", 11: "ekAdaza",
             12: "dvAdaza", 13: "trayodaza", 14: "caturdaza", 15: "paJcadaza",
             16: "SoDaza", 17: "saptadaza", 18: "aSTAdaza", 20: "viMza",
             21: "ekaviMza", 22: "dvAviMza", 23: "trayoviMza", 28: "aSTAviMza",
             30: "triMza", 31: "ekatriMza", 32: "dvAtriMza",
             33: "trayastriMza", 38: "aSTAtriMza", 40: "catvAriMza",
             50: "paJcAza", 60: "SaSTi", 70: "saptati", 80: "azIti",
             90: "navati", 100: "zata", 1000: "sahasra", 10000: "ayuta",
             100000: "lakSa", 1000000: "prayuta", 10000000: "koTi",
             100000000: "arbuda", 1000000000: "abja", 10000000000: "kharva",
             100000000000: "nikharva", 1000000000000: "mahApadma",
             10000000000000: "zaGku", 100000000000000: "jaladhi",
             1000000000000000: "antya", 10000000000000000: "madhya",
             100000000000000000: "parArdha"}

ORDINALS = {1: "prathama", 2: "dvitIya", 3: "tRtIya", 4: "caturtha",
            5: "paJcama", 6: "SaSTha", 7: "saptama", 8: "aSTama", 9: "navama",
            10: "dazama"}


def ordinal_number(n):
    """Return the ordinal number for a given number n in Sanskrit
    """
    if n == 0:
        return ''
    elif n in ORDINALS:
        return ORDINALS[n]
    else:
        ord = cardinal_number(n)
        if n >= 59:
            ord += 'tama'
        return ord


def cardinal_number(n):
    """Return the ordinal number for a given number n in Sanskrit
    """
    PLUS = 'uttara'
    # PLUS = 'adhika'

    if n == 0:
        return ''

    if n in CARDINALS:
        return CARDINALS[n]

    if (n % 10) == 9 and (n % 100) != 9:
        return compose(('ekona', cardinal_number(n + 1)))

    if n < 1000:
        if n <= 100:
            t = n // 10
            return compose((cardinal_number(n % 10), CARDINALS[t * 10]))
        else:
            h = n // 100
            if h == 1:
                return compose((cardinal_number(n % 100), PLUS, 'zata'))
            else:
                return compose((cardinal_number(n % 100), PLUS, CARDINALS[h], 'zata'))
    else:
        # More work needed
        raise ValueError('Number too big!')


def compose(pieces):
    """Fix sandhis etc. and return the correct text
    """
    while pieces[0] == '':
        pieces = pieces[1:]

    SANDHIS = {('a', 'a'): 'A', ('a', 'u'): 'o', ('H', 'a'): 'ra',
               ('H', 'c'): 'zc', ('H', 'n'): 'rn', ('H', 'S'): 'SS',
               ('H', 't'): 'st', ('H', 'u'): 'ru', ('H', 'v'): 'rv',
               ('i', 'a'): 'ya', ('i', 'u'): 'yu', ('T', 'a'): 'Da',
               ('T', 'n'): 'NN', ('T', 'u'): 'Du', ('T', 'v'): 'Dv'}

    result = pieces[0]

    for i in range(1, len(pieces)):
        suff = result[-1]
        pref = pieces[i][0]
        if (suff, pref) in SANDHIS:
            result = result[:-1] + SANDHIS[(suff, pref)] + pieces[i][1:]
        else:
            result = result + pieces[i]

    return result


if __name__ == '__main__':
    for i in range(1, 1001):
        print(i, ':', ordinal_number(i))
