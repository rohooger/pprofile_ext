import collections


def update(d, u):
    """
    Perform a recursive update of dictionary `d` with the dictionary `u`

    :param d: dictionary
    :param u: dictionary

    :return: updated dictionary
    """
    for k, v in u.iteritems():
        if isinstance(v, collections.Mapping):
            r = update(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]

    return d
