
def csv_from_page(s: str, *props):
    import re
    res = re.search(r'var raw_str = "(.*)";', s)
    if not res:
        raise Exception("CSV data not found.")
    raw_csv = res.group(1)

    name_row, *rows = raw_csv.split('\\n')
    all_field = name_row.split(',')
    indexs = [all_field.index(n) for n in props]
    for row in rows:
        values = row.split(',')
        yield tuple(values[i] for i in indexs)


class ServantProp:
    id = 'id'
    star = 'star'
    name_cn = 'name_cn'
    name_jp = 'name_jp'
    name_en = 'name_en'
    name_link = 'name_link'
    name_other = 'name_other'
    cost = 'cost'
    faction = 'faction'
    get = 'get'
    hp = 'hp'
    atk = 'atk'
    class_link = 'class_link'
    avatar = 'avatar'
    card1 = 'card1'
    card2 = 'card2'
    card3 = 'card3'
    card4 = 'card4'
    card5 = 'card5'
    np_card = 'np_card'
    np_type = 'np_type'
    class_icon = 'class_icon'
    stars_marker = 'stars_marker'
    class_marker = 'class_marker'
    get_marker = 'get_marker'
    cards_marker = 'cards_marker'
    npc_marker = 'npc_marker'
    npt_marker = 'npt_marker'
    fac_marker = 'fac_marker'
    sex_marker = 'sex_marker'
    prop1_marker = 'prop1_marker'
    prop2_marker = 'prop2_marker'
    traits_marker = 'traits_marker'
    sort_atk = 'sort_atk'
    sort_hp = 'sort_hp'
