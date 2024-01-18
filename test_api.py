import model
from repository import FakeRepository

batch1 = model.Batch(ref="batch1", sku="SMALL-TABLE", qty=100, eta=None)
batch2 = model.Batch(ref="batch2", sku="UNICORN-CHAIR", qty=15, eta=None)

# This illustrates using a fake repository to test the API
fake_repo = FakeRepository([batch1, batch2])
