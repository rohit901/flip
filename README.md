# FLIP: Fine-Grained Object Classification using CLIP

Code repository for our AI701 team project titled "FLIP: Fine-Grained Object Classification using CLIP".

[![paper](https://img.shields.io/badge/-Paper-red)](https://drive.google.com/file/d/1Td0HP57i_JCHlwJC_I_-A4L83Ve1FDjH/view?usp=share_link)
## Abstract
In this paper, we show zero-shot, few-shot, and fully supervised performance of the Contrastive Language–Image Pre-training (CLIP) models on a fine-grained classification task with a bird dataset, CUB-200-2011. The baseline CLIP model gives an accuracy of 45.56\%, and using KNN; we achieved an accuracy of around 60\% on the pre-trained CLIP model. We also show that we can achieve an average of 3.5\% gain in zero-shot performance after fine-tuning CLIP's image encoder using captions only. Furthermore, a  hybrid model with fine-tuned CLIP's image and text encoders passed through a fully connected feedforward neural network has demonstrated the best performance of 75.18\% accuracy over the CUB-200-2011 dataset. We have also experimented with data augmentation with a fine-tuned Stable Diffusion model. However, it did not lead to an improvement which might be due to the limited number of unique examples that were generated as well as the suspected overlap with the dataset of around 400 million image/caption pairs used in the pre-trained CLIP model.

## Table of Contents
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Team](#team)
- [Acknowledgement](#acknowledgement)

## Dependencies
Install all the required dependencies for the project using [conda](https://conda.io/).

Create a new conda environment using the environment.yaml file and then activate it as follows:
```
conda env create -f environment.yaml
conda activate flip
```

## Usage
The pre-processed Dataset can be downloaded from this link: [birds.zip](https://mbzuaiac-my.sharepoint.com/:u:/g/personal/rohit_bharadwaj_mbzuai_ac_ae/EXq-t3obC6ZPrarkU8Bjoe0BRVvOIud1CAKRgH2-8G10zg?e=PUcP3n)

* Download and unzip the birds folder into `data/` directory.
* Zero-shot code can be run by running `CLIP_CUB_zeroshot_KNN.ipynb` notebook.
* `Few-shot` and `fully-supervised` code can be found in their respective folders.
* The augmented training dataset, which was generated using fine-tuned diffusion model, can be downloaded from: [augmented.zip](https://mbzuaiac-my.sharepoint.com/:u:/g/personal/rohit_bharadwaj_mbzuai_ac_ae/Ee8e4KIX3lxEpX_mtn-k14EBoKC5p0l4mwL9lPTLgtglzQ?e=fqdyyD)
* The fine-tuned diffusion model's weights are also provided and can be downloaded from: [diffusion_weights.ckpt](https://mbzuaiac-my.sharepoint.com/:u:/g/personal/rohit_bharadwaj_mbzuai_ac_ae/Ee-LcRcysyJLki2Qrayr-1QBhFeZzoGtJTBtjXiAmX_47w?e=h5oEc1). Save the weights in `diffusion-code/models/` folder, and to generate samples from the model, run `diffusion-code/inference/inference_512.py` modifying the paths accordingly.


## Team
- [Murtadha Aljubran](mailto:murtadha.aljubran@mbzuai.ac.ae)
- [Rohit K Bharadwaj](mailto:rohit.bharadwaj@mbzuai.ac.ae)
- [Santosh Sanjeev](mailto:Santosh.Sanjeev@mbzuai.ac.ae)

## Acknowledgement
Our code is based on:
- [CLIP](https://github.com/openai/CLIP)
- [Stable Diffusion](https://github.com/CompVis/stable-diffusion)

We thank the respective authors for open-sourcing their code. We also refer to this [Blog](https://lambdalabs.com/blog/how-to-fine-tune-stable-diffusion-how-we-made-the-text-to-pokemon-model-at-lambda) post for fine-tuning the diffusion model.
