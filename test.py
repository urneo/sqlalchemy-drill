import sqlalchemy as sqla
from sqlalchemy.dialects import registry
from sqlalchemy import create_engine

registry.register("drill.pydrill", "sqlalchemy_drill.pydrill", "DrillDialect_pydrill")

try:
    # engine = create_engine('drill+pydrill://localhost:8047/INFORMATION_SCHEMA')
    engine = create_engine('drill+pydrill://192.168.0.3:18047/hive.log')

    conn = engine.connect()
    # inspector = sqla.inspect(engine)
    # print inspector.get_schema_names()
    print engine.table_names()
except Exception as e:
    print e
