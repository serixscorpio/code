import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from orm import mapper_registry, start_mappers


@pytest.fixture
def session():
    engine = create_engine("sqlite://")
    mapper_registry.metadata.create_all(engine)
    start_mappers()
    with Session(engine) as session:
        yield session
