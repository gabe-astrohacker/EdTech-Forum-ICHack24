from databaseAPI import get_all_table

def filter_by_keywords(keywords):
    table = get_all_table(["keywords"])

    link_to_keywords_count = {}

    for rid in table:
        count = 0
        resource_keywords = table[rid].values()

        for keywords in keywords:
            if keywords in resource_keywords:
                count += 1

        if count > 0:
            link_to_keywords_count.update({
                rid_to_link(rid),
                count
            })

    return link_to_keywords_count

def rid_to_link(rid):
    table = get_all_table(["resources"])

    return table[rid]["link"]

def filter_with_keywords(keywords):


def main():
    pass


if __name__ == '__main__':
    main()