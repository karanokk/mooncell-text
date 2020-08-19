from typing import List, Optional


class SqliteType:
    text = 'TEXT'
    integer = 'INTEGER'
    boolean = 'BOOLEAN'
    real = 'REAL'


def sqlite_type(obj: object) -> str:
    obj_type = type(obj)
    if obj_type in (str, list, dict):
        return SqliteType.text
    elif obj_type == bool:
        return SqliteType.boolean
    elif obj_type == int:
        return SqliteType.integer
    elif obj_type == float:
        return SqliteType.real
    elif obj is None:
        raise TypeError('Cannot infer type from `None`.')
    else:
        raise TypeError('Unsupported type.')


def creation_sql(table_name: str, rows: List[dict], *, primary_key=None):
    definitions = []
    row = rows[0]
    for key, value in row.items():
        try:
            s_type = sqlite_type(value)
        except TypeError:
            s_type = None
            for row in rows:
                if row[key] is not None:
                    s_type = sqlite_type(value)
            if s_type is None:
                s_type = SqliteType.text

        words = [key, s_type]
        if primary_key == key:
            words.append('PRIMARY KEY')
        column_definition = ' '.join(words)
        definitions.append(column_definition)
    sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({",".join(definitions)})'
    return sql


def possible_primary_keys(rows: List[dict]) -> Optional[List[str]]:
    temp = {key: set()
            for key, value in rows[0].items() if isinstance(value, int)}
    for row in rows:
        out_keys = []
        for key, value in temp.items():
            new_value = row[key]
            if new_value in value:
                out_keys.append(key)
            else:
                value.add(new_value)
        for out_key in out_keys:
            del temp[out_key]
        if not temp:
            return None
    return list(temp.keys())
