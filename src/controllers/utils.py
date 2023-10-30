from urllib.parse import urlencode

def get_page_link(new_skip, limit, endpoint):
    next_link_params = {"skip": new_skip, "limit": limit}
    return f"/{endpoint}/?{urlencode(next_link_params)}"
