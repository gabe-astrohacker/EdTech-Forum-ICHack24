from databaseWrapper import filter_by_keywords


def get_resource_score(up_score, down_score):
    return (up_score - down_score) / 2


def search(keywords):
    _link_to_info = filter_by_keywords(keywords)
    # TODO
