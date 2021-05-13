

########## Aux ##########
types = {
    "BOOK":  0,
    "SHOW":  1,
    "ANIME": 2,
}
ids = {
    0: "BOOK",
    1: "SHOW",
    2: "ANIME",
}
def get_type(type):
    if type not in types:
        return None
    return types[type]
def get_id(id):
    if id not in ids:
        return None
    return ids[id]
#########################

def getViewsOf(type,itemId):
    type = get_type(type)
    if not type: return 'false', 400

    # TODO
    return 0

def getLikesOf(type,itemId):
    type = get_type(type)
    if not type: return 'false', 400

    # TODO
    return 0