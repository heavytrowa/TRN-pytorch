# Temporal Relation Networks

We release the code of the [Temporal Relation Networks](http://relation.csail.mit.edu/), built on top of the [TSN-pytorch codebase](https://github.com/yjxiong/temporal-segment-networks).

**NEW (July 29, 2018)**: This work is accepted to ECCV'18, check the [paper](https://arxiv.org/pdf/1711.08496.pdf) for the latest result. We also release the state of the art model trained on the Something-Something V2, see following instruction.

**Note**: always use `git clone --recursive https://github.com/metalbubble/TRN-pytorch` to clone this project
Otherwise you will not be able to use the inception series CNN architecture.

![framework](http://relation.csail.mit.edu/framework_trn.png)

### Data preparation
Download the [something-something dataset](https://www.twentybn.com/datasets/something-something/v1) or [jester dataset](https://www.twentybn.com/datasets/something-something) or [charades dataset](http://allenai.org/plato/charades/). Decompress them into some folder. Use [process_dataset.py](process_dataset.py) to generate the index files for train, val, and test split. Finally properly set up the train, validation, and category meta files in [datasets_video.py](datasets_video.py).

For [Something-Something-V2](https://www.twentybn.com/datasets/something-something), we provide a utilty script [extract_frames.py](https://github.com/metalbubble/TRN-pytorch/blob/master/extract_frames.py) for converting the downloaded `.webm` videos into directories containing extracted frames. Additionally, the corresponding optic flow images can be downloaded from [here](http://relation.csail.mit.edu/data/20bn-something-something-v2-flow.tar.gz).

### Code

Core code to implement the Temporal Relation Network module is [TRNmodule](TRNmodule.py). It is plug-and-play on top of the TSN.

### Training and Testing

* Train on moments in time dataset

```bash
python parse_moments.py
./train.sh
```

* Test on moments in time dataset
```bash
./test_moment.sh
```

* Test on video (ex. sample_data/test2.mp4)

```bash
./test_video.sh
```

* Prediction timeline on video (ex. sample_data/sample1.mp4)

```bash
./test_segment.sh
python plot.py
```

### Reference:
B. Zhou, A. Andonian, and A. Torralba. Temporal Relational Reasoning in Videos. European Conference on Computer Vision (ECCV), 2018. [PDF](https://arxiv.org/pdf/1711.08496.pdf)
```
@article{zhou2017temporalrelation,
    title = {Temporal Relational Reasoning in Videos},
    author = {Zhou, Bolei and Andonian, Alex and Oliva, Aude and Torralba, Antonio},
    journal={European Conference on Computer Vision},
    year={2018}
}
```

### Acknowledgement
Our temporal relation network is plug-and-play on top of the [TSN-Pytorch](https://github.com/yjxiong/temporal-segment-networks), but it could be extended to other network architectures easily. We thank Yuanjun Xiong for releasing TSN-Pytorch codebase. Something-something dataset and Jester dataset are from [TwentyBN](https://www.twentybn.com/), we really appreciate their effort to build such nice video datasets. Please refer to [their dataset website](https://www.twentybn.com/datasets/something-something) for the proper usage of the data.
