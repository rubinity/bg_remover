# bg_remover
Smart Image Background Remover (API-based tool)

Demo - https://clearback.netlify.app/

Prometheus - http://rubinity.duckdns.org:9090

Grafana - http://rubinity.duckdns.org:3000

http://rubinity.duckdns.org:3000/dashboards

## Current state
Current version removes background using U2Net library and rough thresholding.
Still to do:

- Improve thresholding with advanced algorithms

- Add background customization

- Add user-friendly input for CLI version

- Create a proper UI in a seperate repo

- Experiment with alternative models


---

Note: The first Docker build may take several minutes as it downloads and installs large dependencies (e.g., PyTorch). Subsequent builds will be much faster.

---
## Table of Contents
  - [Current state](#current-state)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Reference](#reference)



---

## About

---
## Installation



## Reference

Based on the original **U²-Net** implementation: [xuebinqin/U-2-Net](https://github.com/xuebinqin/U-2-Net)

