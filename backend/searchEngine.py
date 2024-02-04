from databaseWrapper import filter_by_keywords


def compute_score(up_score, down_score):
    return (up_score - down_score) / 2


# RETURN: list of info dictionary
def split_by_count(links_to_info):
    split_list = [{}]
    print(links_to_info)
    fst_key = next(iter(links_to_info))

    prev_count = links_to_info[fst_key]['count']

    for link in links_to_info:
        if links_to_info[link]["count"] == prev_count:
            split_list[-1].update({link: links_to_info[link]})
        else:
            split_list.append({link: links_to_info[link]})

    return split_list


def map_score(links):
    for link in links:
        link_value = links[link]
        up_score = link_value["up_score"]
        down_score = link_value["down_score"]

        links.update({link:
            {
                "count": link_value["count"],
                "description": link_value["description"],
                "score": compute_score(up_score, down_score)
            }})

    return links


def search(keywords):
    link_to_info = filter_by_keywords(keywords)
    link_to_info = map_score(link_to_info)

    link_to_info = dict(sorted(link_to_info.items(), key=lambda item: item[1]["count"], reverse=True))

    split_dict = split_by_count(link_to_info)
    print(f"split_dic: {split_dict}")

    sorted_search = {}

    for link in split_dict:
        print(f"link: {link}")
        sorted_slice = dict(sorted(link.items(), key=lambda item: item[1]["score"], reverse=True))

        for key in sorted_slice:
            sorted_search.update({key: sorted_slice[key]})

    return sorted_search


if __name__ == '__main__':
    print(search(["mouse", "fingers", "maltesers", "red", "bull"]))
