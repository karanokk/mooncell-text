import json
import sqlite3
from typing import List, Union
from . import convert


class JConnection(sqlite3.Connection):
    def insert(self, table_name, **kwargs):
        keys = kwargs.keys()
        insert_sql = f'INSERT INTO {table_name} ({",".join(keys)}) values ({",".join(["?"] * len(keys))})'
        self.execute(insert_sql, kwargs.values)

    def load_table_from_json(self, table_name: str, rows: List[dict]):
        if not (isinstance(rows, list) and len(rows)):
            return
        # create table
        primary_keys = convert.possible_primary_keys(rows)
        primary_key = primary_keys[0] if primary_keys else None
        creation_sql = convert.creation_sql(
            table_name, rows, primary_key=primary_key)
        self.execute(creation_sql)
        # insert rows
        keys = rows[0].keys()
        insert_sql = f'INSERT INTO {table_name} ({",".join(keys)}) values ({",".join(["?"] * len(keys))})'
        self.executemany(insert_sql, map(
            lambda x: tuple(x.values()), rows))
        self.commit()

    def load_tables_from_json(self, tables):
        self.execute("BEGIN")
        for table_name, rows in tables.items():
            self.load_table_from_json(table_name, rows)


def connect(database, **kwargs) -> JConnection:
    kwargs['detect_types'] = sqlite3.PARSE_COLNAMES
    kwargs['factory'] = JConnection
    return sqlite3.connect(database, **kwargs)


def register_adapters_and_converters():
    def adapt_list(val: Union[list, str]) -> str:
        if isinstance(val, list):
            return ','.join(map(adapt_list, val))
        return str(val)

    def convert_list(val: str, *, transform: callable = str) -> list:
        if val.startswith('['):
            val = val[1:]
        if val.endswith(']'):
            val = val[:-1]
        if val.startswith('['):
            result = val.split('],[')
            return [convert_list(x, transform=transform) for x in result]
        else:
            return [convert_list(s) for s in val.split(',') if val]

    def convert_int_list(val: str) -> List[int]:
        return convert_list(val, transform=int)

    def _pre_decode(transform: callable):
        return lambda b: transform(b.decode())

    sqlite3.register_adapter(list, adapt_list)
    sqlite3.register_adapter(dict, json.dumps)

    sqlite3.register_converter("strList", _pre_decode(convert_list))
    sqlite3.register_converter("intList", _pre_decode(convert_int_list))
    sqlite3.register_converter("dict", _pre_decode(json.loads))


register_adapters_and_converters()
