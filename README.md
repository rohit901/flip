# FLIP: Fine-Grained Object Classification using CLIP

Code repository for our AI701 team project titled "FLIP: Fine-Grained Object Classification using CLIP". 

## Abstract
In this paper, we show zero-shot, few-shot, and fully supervised performance of the Contrastive Language–Image Pre-training (CLIP) models on a fine-grained classification task with a bird dataset, CUB-200-2011. We show that we can achieve an average of 3.5% gain in zero-shot performance after fine-tuning CLIP's image encoder using captions only. Furthermore, a  hybrid model with fine-tuned CLIP's image and text encoders passed through a fully connected feedforward neural network has demonstrated the best performance of 75.18% accuracy over the CUB-200-2011 dataset. We have also experimented with data augmentation with a fine-tuned Stable Diffusion model. However, it did not lead to an improvement which might be due to the limited number of unique examples that were generated as well as the suspected overlap with the dataset of around 400 million image/caption pairs used in the pre-trained CLIP model.

## Table of Contents
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Team](#team)
- [Acknowledgement](#acknowledgement)

## Dependencies
TODO

## Usage
TODO

## Team
- [Murtadha Aljubran](mailto:murtadha.aljubran@mbzuai.ac.ae)
- [Rohit K Bharadwaj](mailto:rohit.bharadwaj@mbzuai.ac.ae)
- [Santosh Sanjeev](mailto:Santosh.Sanjeev@mbzuai.ac.ae)

## Acknowledgement
Our code is based on:
- [CLIP](https://github.com/openai/CLIP)
- [Stable Diffusion](https://github.com/CompVis/stable-diffusion)

We thank the respective authors for open-sourcing their code. We also refer to this [Blog](https://lambdalabs.com/blog/how-to-fine-tune-stable-diffusion-how-we-made-the-text-to-pokemon-model-at-lambda) post for fine-tuning the diffusion model.