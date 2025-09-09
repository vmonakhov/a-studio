"""Application entrypoint"""

from main import app
from time import sleep

import torch
from torch.multiprocessing import get_start_method, set_start_method

print(f">>>>> {torch.cuda.is_initialized()=}")
print(f">>>>> {torch._C._cuda_isInBadFork()=}")
print(f">>>>> {set_start_method('spawn', force=True)=}")
print(f">>>>> {get_start_method()=}")
print(f">>>>> {torch.cuda.init()=}")
print(f">>>>> {torch.zeros(1).cuda()=}")
#sleep(15)

if __name__ == "__main__":
    app.run()
