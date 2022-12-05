import subprocess
import json
import numpy as np
import os
import time

def generate_img(dir_name, prompt):
    run = f"python ../scripts/txt2img.py \
    --prompt '{prompt}' \
    --outdir '{dir_name}' \
    --H 512 \
    --W 512 \
    --n_samples 4 \
    --config '../configs/stable-diffusion/birds_512.yaml' \
    --ckpt '../models/model_512.ckpt'"

    result = subprocess.run(run, capture_output = True, text = True, shell = True)
    error = result.stderr
    if "CUDA out of memory." in error:
        print("="*40)
        print("CUDA out of memory.")
        print(f"directory: {dir_name}")
        print(f"prompt: {prompt}")
        with open(root_dir + "error.txt", "w") as file:
            file.write(f"directory: {dir_name}")
            file.write(f"prompt: {prompt}")
            file.write("="*40)
        print("="*40)
    else:
        print("Success!")
        time.sleep(4)
        with open(dir_name + "/prompt.txt", "w") as f:
            f.write(prompt)

        print("="*40)

with open("../data/birds/captions.json", "r") as f:
    captions = json.load(f)

root_dir = "output_512/"

#get list of all directories in root_dir
dirs = [x + ".jpg" for x in os.listdir(root_dir) if os.path.isdir(root_dir + x)]

tot_keys = set(captions.keys())
saved_keys = set(dirs)

print(f"Saved Keys: {len(saved_keys)}")

keys_to_save = tot_keys - saved_keys

keys = list(keys_to_save)[:2000-len(saved_keys)]

np.random.shuffle(keys)

captions_subset = {k: captions[k] for k in keys}

for k, v in captions_subset.items():
    print("key:", k)
    caption = np.random.choice(v)
    print("caption:", caption)
    dir_name = k[:-4]
    generate_img(root_dir + dir_name, caption)