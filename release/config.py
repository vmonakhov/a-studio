"""Release backend config"""
'''
import torch
from torch.multiprocessing import get_start_method, set_start_method

print(f">>>>> {torch.cuda.is_initialized()=}")
print(f">>>>> {torch._C._cuda_isInBadFork()=}")
print(f">>>>> {set_start_method('spawn', force=True)=}")
print(f">>>>> {get_start_method()=}")
print(f">>>>> {torch.cuda.init()=}")
print(f">>>>> {torch.zeros(1).cuda()=}")
'''
MODEL = "sonar"
DEFAULT_TRESHOLD = 0.2
DEFAULT_BATCHSIZE = 200
DEFAULT_WINDOW = 50
TEST_RESTRICTION_MAX_BATCHES = 2000
PROCESSORS_COUNT = 1
EMBED_BATCH_SIZE = 5
NORMALIZE_EMBEDDINGS = True
VIS_REGRESSION = False
VIS_BATCH_INFO = True
API_PORT = 80
