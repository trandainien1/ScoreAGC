
# ScoreAGC - Evaluate the importance of CAM for every heads 

This is github implementation of ScoreAGC

## Description

Vision Transformer (ViT) is a widely used model in computer vision due to its unique architecture, which uses self-attention mechanisms to effectively extract features for accurate predictions. Given its high performance, it is crucial to understand the features the model relies on for decision-making. This study proposes a method for visualizing the features extracted by ViT by identifying Class Activation Maps (CAMs) at each head within the self-attention module. We then evaluate the importance of each CAM and aggregate them to derive the final CAM representation. Furthermore, we used evaluation metrics such as Localization metrics and Faithfulness metrics to assess whether our explanation method provides meaningful insights into the model’s decision-making process.

## Kaggle

All the experiments are conducted in Kaggle. 

To run Kaggle, you have to do the following steps:
1. Download "ILSVRC2012_img_val.tar" and "ILSVRC2012_devkit_t12.tar.gz" from [Imagenet](https://www.image-net.org).
2. Upload "ILSVRC2012_img_val.tar" and "ILSVRC2012_devkit_t12.tar.gz" to your personal Google Drive.

3. Enable sharing option and copy the id of two of them.

4. Paste id to our Kaggle and then you are good to go. 

**Localization evaluation**: [link](https://www.kaggle.com/code/nientrandai/localization-evaluation)

**Insertion Deletion evaluation**: [link](https://www.kaggle.com/code/nientrandai/insertion-deletion-evaluation)

**Falthfulness Evaluation**: [link](https://www.kaggle.com/code/nientrandai/faithfulness-evaluation)

**Display Saliency maps**: [link](https://www.kaggle.com/code/nientrandai/display-saliency-map)

📌 You can store saliency maps/heatmaps of XAI methods for later use by store them on Google Drive and use the id of them in our Kaggle.

# Github references

- Special thanks to the following githubs to support our evaluations and references. 

[Attention Guided CAM: Visual Explanations of Vision Transformer Guided by Self-Attention](https://github.com/LeemSaebom/Attention-Guided-CAM-Visual-Explanations-of-Vision-Transformer-Guided-by-Self-Attention)

[Explainability and Evaluation of Vision Transformers: An In-Depth Experimental Study](https://github.com/ValentinCord/TFE_XAI_ViT/tree/main)

[Explaining Information Flow Inside Vision Transformers Using Markov Chain](https://github.com/XianrenYty/Transition_Attention_Maps)

- Detail our usage in these githubs:

We clone these githubs and implement our methods inside them. Besides, we also use their implementation of evaluation to help us in conducting evaluation metrics.

- Refer to these github for ScoreAGC implementation (refer README for detail instruction):

    Localization Evaluation: [link](https://github.com/trandainien1/better_agc_ubuntu)

    Insertion/Deletion Evaluation: [link](https://github.com/trandainien1/tam)

    Faithfulness Evaluation: [link](https://github.com/trandainien1/quantus)