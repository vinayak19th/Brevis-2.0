# MDD_Project
* **BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension**: https://arxiv.org/abs/1910.13461

# Usage

## BART Serving:
### Step 1: Clone this repo

```bash
git clone https://github.com/vinayak19th/MDD_Project
```

### Step 2: pull the docker container

> For information on installing docker, check [here](https://docs.docker.com/engine/install/)

```bash
docker pull vinayak1998th/bart_serve:1.0
```
### Step 3: Launch the container

```bash
docker run -d -p 8501:8501 -p 8500:8500 --name bart vinayak1998th/bart_serve:1.0
```
### Step 4 : Test

The code for testing after the server is running is in the [Serving_Test](./Serving_Test.ipynb) notebook