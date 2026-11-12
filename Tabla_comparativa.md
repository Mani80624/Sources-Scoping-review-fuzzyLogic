# Comparative table: fuzzy models in mammography

Complete map of the **65 studies** (2010–2026) that apply fuzzy logic or neuro-fuzzy models to mammography, organised by the role of the fuzzy component, model, dataset, metrics and use of BI-RADS. The last four columns contain the coding used for the figures and sections of the article (see *Coding criteria* and *Summary* below).

| Author (year) | Role | Fuzzy model | Dataset | Main metric | Uses BI-RADS? | Model category (Fig. 4) | Dataset category (Fig. 3) | Validation (Sec. 3.7) | Compared with other methods? |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| Fernandes et al. (2010) | Classification only | ANFIS (Adaptive Network-based Fuzzy Inference System) | Mini-MIAS (322 mammograms in total) | Accuracy rate: 99.75% (maximum, with PSIGMF membership function); also 96.95% with GBELLMF, 97.22% with TRAPMF and 99.49% with PIMF | No | ANFIS | MIAS/Mini-MIAS | Hold-out | Yes |
| Sahba & Venetsanopoulos (2010) | Segmentation + classification | Fuzzy contrast adaptation and type-II fuzzy sets | Real mammograms, unspecified database | Using SVM as classifier, a true positive rate of up to 90.5% | No | Type-2 fuzzy | Not specified | Cross-validation | Yes |
| Mohanalin et al. (2010) | Image preprocessing | Type-II fuzzy index (Tizhoosh) to find the optimal thresholding parameter | MIAS (50 images) and UCSF (197 images) | True positive rate: MIAS (93.75%), UCSF (97.18%) and combined (96.55%)<br>False positive rate: MIAS (0.52), UCSF (0.37), combined (0.4) | No | Type-2 fuzzy | MIAS/Mini-MIAS; Other public (UCSF) | No formal validation | Yes |
| Chumklin et al. (2010) | Classification only | Interval type-2 fuzzy logic system with membership functions generated using Possibilistic C-Means | In-house mammograms from Maharaj Hospital, Chiang Mai University | 89.47% correct classification (best system, interval type-2 with PCM), with 6 false positives per image | No | Fuzzy C-Means and variants; Type-2 fuzzy | In-house/private | Hold-out | Yes |
| Das & Bhattacharya (2011) | Segmentation + classification | Hybrid: fuzzy c-means (mass segmentation) and ANFIS (classification) | MIAS and other databases; 200 mammograms | 86% correct classification | No | Fuzzy C-Means and variants; ANFIS | MIAS/Mini-MIAS | Hold-out | No |
| Keleş et al. (2011) | Classification only | Neuro-fuzzy | UCI Mammographic Mass Dataset with 516 benign and 445 malignant cases | Sensitivity: 0.76<br>Specificity: 0.97<br>Positive predictive value: 0.96<br>Negative predictive value: 0.81 | Yes | Neuro-fuzzy (generic) | UCI Mammographic Mass | Not reported | No |
| Y. Wang et al. (2011) | Segmentation only | Extended Fuzzy C-Means (EFCM) clustering | Qiqihaer Medical College Hospital, Qiqihaer, China | Accuracy: 98.50%<br>Sensitivity: 99.72%<br>Specificity: 97.42%<br>Positive predictive value: 97.21%<br>Negative predictive value: 97.68% | No | Fuzzy C-Means and variants | In-house/private | Hold-out | Yes |
| Huang et al. (2010) | Classification only | ANFIS (neuro-fuzzy inference system, Sugeno model) | UCI Mammographic Mass Dataset with 516 benign and 445 malignant cases | AROC = 92.80% | Yes | ANFIS; Sugeno / Takagi–Sugeno | UCI Mammographic Mass | Hold-out | Yes |
| Keller et al. (2012) | Segmentation + classification | Multiclass adaptive Fuzzy C-Means (FCM) | Full-field digital mammography (FFDM) | n/a | Yes | Fuzzy C-Means and variants | Not specified | Cross-validation | No |
| Mencattini & Salmeri (2011) | Segmentation + classification | Fuzzy C-Means (segmentation) and fuzzy inference system | DDSM: D1 (388 images), D2 (674 images) | Sensitivity: 0.9 in both D1 and D2. Highest FPpI (false positives per image): 0.85 in D1 and D2 | Yes | Fuzzy C-Means and variants; Fuzzy inference system (unspecified) | DDSM/CBIS-DDSM | Cross-validation | Yes |
| Gorgel et al. (2012) | Classification only | ANFIS with subtractive clustering (Sugeno model) | Mammograms from the Faculty Hospital | Epoch 50: up to 92% accuracy, 100% sensitivity, 86% specificity, 92% F-measure | No | ANFIS; Sugeno / Takagi–Sugeno | In-house/private | Hold-out | Yes |
| Kabbadj et al. (2012) | Segmentation + classification | Fuzzy inference system (If-And-Then rules) and SVM for classification | MIAS (16 mammograms: 8 positive and 8 negative cases) | Correct classification rate: 99.60% (linear kernel)<br>Sensitivity: 99.11%<br>Specificity: 100% | No | Fuzzy inference system (unspecified) | MIAS/Mini-MIAS | Not reported | Yes |
| Keles & Keles (2013) | Classification only | Neuro-fuzzy (NEFCLASS) | UCI Mammographic Mass Dataset | Positive predictive value: 75%<br>Negative predictive value: 95% | Yes | Neuro-fuzzy (generic) | UCI Mammographic Mass | Cross-validation (+ hold-out) | Yes |
| Vadivel & Surendiran (2013) | Classification only | Mamdani-type fuzzy inference system with generated rules | DDSM (224 masses) | Classification using fuzzy rules:<br>87.76% (4 classes); 100% (oval vs round); 95.45% (lobular vs round); 97.22% (irregular vs oval) | Yes | Mamdani | DDSM/CBIS-DDSM | Cross-validation | Yes |
| Xiao-dong Wang et al. (2013) | Classification only | ANFC-LH (adaptive neuro-fuzzy classifier with linguistic hedges) | DDSM (740 images: 380 with lesions, 360 normal) | Accuracy: 89.14% (ANFC-LH with feature selection, 7 features)<br>Accuracy: 87.54% (improved ANFC-LH without feature selection) | No | Neuro-fuzzy (generic) | DDSM/CBIS-DDSM | Cross-validation | Yes |
| Rathi & Aggarwal (2014) | Classification only | Fuzzy neural network (FNN) | UCI 'Mammographic Mass' Data Set | Accuracy 90.00%, sensitivity 92.66%, specificity 87.78% (FRBF, best model);<br>Accuracy 87.50%, sensitivity 88.57%, specificity 86.66% (FMLP);<br>Accuracy 87.08%, sensitivity 84.07%, specificity 89.76% (RBF);<br>Accuracy 85.83%, sensitivity 85.98%, specificity 85.71% (MLP) | Yes | Neuro-fuzzy (generic) | UCI Mammographic Mass | Cross-validation | Yes |
| Ma et al. (2015) | Image preprocessing | Representation of spatial relations based on fuzzy sets | 95 pairs of real temporal mammograms | 0.8524 (combined single and temporal scheme) and 0.8458 (single scheme, without fuzzy registration) | No | Other fuzzy operators | Not specified | No formal validation | Yes |
| Miranda & Felipe (2015) | Classification only | Fuzzy Omega algorithm | DDSM (Digital Database for Screening Mammography) | 76.67% (nodules), 83.34% (calcifications) | Yes | Fuzzy rule-based | DDSM/CBIS-DDSM | Hold-out | No |
| Subramanian et al. (2015) | Classification only | Fuzzy cognitive maps (FCM) | MIAS (Mammographic Image Analysis Society) | Accuracy: 94.3% (normal 100%, benign 89.3%, malignant 91.7%) | No | Fuzzy cognitive maps | MIAS/Mini-MIAS | Cross-validation | Yes |
| Göreke et al. (2015) | Classification only | Mamdani fuzzy inference system | MIAS (Mammographic Image Analysis Society) | Sensitivity: 98%<br>Specificity: 99% | No | Mamdani | MIAS/Mini-MIAS | No formal validation | Yes |
| Cordeiro et al. (2016) | Segmentation + classification | Fuzzy GrowCut: GrowCut algorithm modified with Gaussian fuzzy membership functions | IRMA database (685 images in total, using fatty and fibrous tissue) | Classification accuracy with segmentation: 91.28%<br>Classification accuracy without segmentation: 85.53% | Yes | Fuzzy GrowCut | Other public (IRMA) | Cross-validation | Yes |
| Cordeiro et al. (2015) | Segmentation only | Fuzzy GrowCut: semi-supervised cellular automaton with Gaussian fuzzy membership function | Mini-MIAS (Mammographic Image Analysis Society) | Balanced accuracy (BAC) = 0.83 ± 0.13<br>Specificity: 0.84 ± 0.18<br>Sensitivity: 0.82 ± 0.22 | No | Fuzzy GrowCut | MIAS/Mini-MIAS | No formal validation | Yes |
| Boulehmi et al. (2016) | Classification only | ANFIS (Adaptive Network-based Fuzzy Inference System) | MIAS database (322 MLO mammograms and 56 mammograms for testing) | Classification rate: 97% | No | ANFIS | MIAS/Mini-MIAS | Cross-validation | Yes |
| Mahersia et al. (2016) | Classification only | ANFIS (Adaptive Network-based Fuzzy Inference System) | MIAS database (322 mammograms) | Recognition rate: ANFIS 95.42%; Bayesian neural network 97.08% | No | ANFIS | MIAS/Mini-MIAS | Cross-validation | Yes |
| Pawar & Talbar (2016) | Classification only | Genetic fuzzy system (GFS) | Mini-MIAS database; 142 images | Maximum accuracy with 16 features: 89.47% | No | Genetic-fuzzy | MIAS/Mini-MIAS | Not reported | Yes |
| Ben-Ari et al. (2016) | Segmentation only | Fuzzy logic system | 1,243 full-field digital mammograms (from several hospitals in Israel) | Breast density classification accuracy: 75% with adaptive threshold and 67.4% with constant threshold | Yes | Fuzzy inference system (unspecified) | In-house/private | Cross-validation | Yes |
| Touil & Kalti (2016) | Segmentation only | Iterative Fuzzy Breast Segmentation (IFBS) based on Fuzzy C-Means | Mini-MIAS database (322 digitised mammograms) | Mean accuracy = 0.937<br>Mean completeness (CM) = 0.989<br>Mean correctness (CR) = 0.947 | No | Fuzzy C-Means and variants | MIAS/Mini-MIAS | No formal validation | Yes |
| Baharuddin et al. (2016) | Classification only | Type-2 fuzzy logic, Mamdani model, with rules generated from expert knowledge | Reports and mammograms from the Radiology Department, Universiti Kebangsaan Malaysia Medical Centre | Accuracy, sensitivity and specificity with triangular membership function: 78%, 98.24%, 73.33%<br>With Gaussian membership function: 64%, 97.92%, 50%<br>With trapezoidal membership function: 58%, 12.55%, 37.5% | Yes | Type-2 fuzzy; Mamdani | In-house/private | Cross-validation | Yes |
| Nilashi et al. (2017) | Classification only | Fuzzy rule-based reasoning system | Mammographic Mass dataset | AUC: 0.941 | Yes | Fuzzy rule-based | UCI Mammographic Mass | Cross-validation | Yes |
| Pavan et al. (2017) | Segmentation only | Fuzzy C-Means tuned with variable compactness (FCMVC) | In-house dataset (Botucatu Medical School) | 67.8% correct classification compared with the radiologist's BI-RADS assessment | Yes | Fuzzy C-Means and variants | In-house/private | No formal validation | Yes |
| H. Wang et al. (2017) | Classification only | Grouped fuzzy SVM | DDSM (Digital Database for Screening Mammography) | Accuracy: 0.82<br>True positive rate: 0.78<br>False positive rate: 0.14<br>EVL: 0.72 | No | Fuzzy SVM | DDSM/CBIS-DDSM | Cross-validation | Yes |
| Salih & Kamil (2018) | Segmentation only | Fuzzy mathematical morphology | Mini-MIAS (322 images) | Reports CDR, DSI, recall and precision (for each image analysed) | No | Other fuzzy operators | MIAS/Mini-MIAS | No formal validation | Yes |
| Li et al. (2018) | Classification only | Feature ranking-guided fuzzy rule interpolation (T-FRI) for mass shape | CBIS-DDSM (Curated Breast Imaging Subset of DDSM) | Mean guided accuracy: 61.5% | Yes | Fuzzy rule interpolation | DDSM/CBIS-DDSM | Hold-out | Yes |
| Fan et al. (2018) | Segmentation only | Maximum fuzzy entropy thresholding tuned with differential evolution (DE) | Private (First Hospital of Quanzhou; 8 images, 4 tissue types) | Accuracy reported per image | No | Fuzzy entropy | In-house/private | No formal validation | Yes |
| Goudarzi & Maghooli (2018) | Classification only | Fuzzy rule extraction using the look-up table method | Mini-MIAS | Accuracy: 89.37% ± 6.62% | No | Fuzzy rule-based | MIAS/Mini-MIAS | Cross-validation | Yes |
| Hmida et al. (2018) | Segmentation only | Fuzzy contours incorporated into the Chan–Vese model | Mini-MIAS (57 mass ROIs) | Accuracy: 93.96%<br>Sensitivity: 91.12%<br>Precision: 88.08% | No | Other fuzzy operators | MIAS/Mini-MIAS | No formal validation | Yes |
| Sadad et al. (2018) | Segmentation + classification | Fuzzy C-Means (FCM) combined with region growing for segmentation | MIAS (109 images) and DDSM (72 images) | Decision tree accuracy: 98.2% (MIAS) | No | Fuzzy C-Means and variants | MIAS/Mini-MIAS; DDSM/CBIS-DDSM | Cross-validation | Yes |
| Sapate et al. (2018) | Segmentation + classification | Adaptive fuzzy region growing for lesion detection | Private (Tata Memorial Centre, FFDM) and DDSM | Accuracy: 88.61% (SVM)<br>Specificity: 91.67%<br>Sensitivity: 85.56% | No | Other fuzzy operators | DDSM/CBIS-DDSM; In-house/private | Cross-validation | Yes |
| P. Das & Das (2019) | Segmentation + classification | Folded kernel FCM (folded KFCM) | MIAS, DDSM and BIRADS (categories II and IV) | Relative error of shape features; convergence time | No | Fuzzy C-Means and variants | MIAS/Mini-MIAS; DDSM/CBIS-DDSM | Cross-validation | Yes |
| Kumar et al. (2018) | Segmentation only | Superpixel FCM with spatial information, tuned with Crow Search (SPOFCM) | MIAS | Mammograms (SPOFCM) accuracy: Case 1 = 80.07%, Case 2 = 84.28%, Case 3 = 58.38%, Case 4 = 84.32% | No | Fuzzy C-Means and variants | MIAS/Mini-MIAS | No formal validation | Yes |
| Punitha & Perumal (2019) | Segmentation only | Fuzzy-rough sets: FRIS (noise), FRNN (segmentation), fuzzy-rough set theory FRST (features) | Mini-MIAS | Accuracy: 99.02%<br>Sensitivity: 72.53%<br>Specificity: 78.45% | No | Fuzzy-rough | MIAS/Mini-MIAS | Not reported | Yes |
| Qu et al. (2019) | Segmentation + classification | Fuzzy C-Means (feature extraction)<br>Multi-label fuzzy-rough feature selection (MLFRFS) | MIAS | Accuracy depends on the criterion | Yes | Fuzzy C-Means and variants; Fuzzy-rough | MIAS/Mini-MIAS | Cross-validation | Yes |
| Parvathavarthini et al. (2019) | Segmentation only | Intuitionistic FCM with neighbourhood attraction, initialised with Crow Search (CrSA-IFCM-NA) | Mini-MIAS (322 images) | Cluster validity indices (Silhouette, DB), Jaccard and Dice | No | Fuzzy C-Means and variants | MIAS/Mini-MIAS | No formal validation | Yes |
| Li et al. (2020) | Classification only | Feature weight-guided fuzzy rule interpolation (W-T-FRI) | Breast Cancer Digital Repository (BCDR) | Accuracy: 91.65% on BCDR-D01 and 84.28% on BCDR-F01<br>Sensitivity: 88.93% on BCDR-D01 and 82.14% on BCDR-F01<br>AUC: 0.9614 on BCDR-D01 and 0.9023 on BCDR-F01 | No | Fuzzy rule interpolation | BCDR | Cross-validation | Yes |
| Patil & Biradar (2020) | Classification only | Fuzzy logic classifier tuned with IAP-CSA | MIAS | Accuracy: 91.67%<br>Sensitivity: 88.75%<br>Specificity: 93.13%<br>Precision: 86.59% | No | Fuzzy inference system (unspecified) | MIAS/Mini-MIAS | Not reported | Yes |
| Qu et al. (2020a) | Image preprocessing | Fuzzy-rough refinement of image processing (FRIP): local ROI contrast improvement guided by the fuzzy positive region | MIAS | Accuracy, BI-RADS criterion: 94.04%<br>Boyd criterion: 84.25%<br>Tabár criterion: 86.21%<br>Wolfe criterion: 90.34% | Yes | Fuzzy-rough | MIAS/Mini-MIAS | Not reported | Yes |
| Shen et al. (2020) | Classification only | Hierarchical Fuzzy Classifier (HFC): fusion of interval type-II possibilistic fuzzy C-Means and a fuzzy neural network | INbreast and a private database | Benign/malignant classification accuracy with HFC: 83.90% (INbreast), 82.11% (private); 5-class BI-RADS classification with HFC: 58.92% (INbreast), 50.41% (private) | Yes | Type-2 fuzzy; Fuzzy C-Means and variants; Neuro-fuzzy (generic) | INbreast; In-house/private | Cross-validation | Yes |
| Thawkar & Ingolikar (2020a) | Classification only | ANFIS | DDSM | Accuracy: 98.92%<br>True positive rate: 99.10%<br>True negative rate: 98.72% | No | ANFIS | DDSM/CBIS-DDSM | Not reported | Yes |
| Chaira (2021) | Segmentation only | Intuitionistic fuzzy clustering | 25 mammography images downloaded from the internet | Accuracy: 98.74% (exponential distance function) and 98.42% (divergence).<br>Mean classification/segmentation error with respect to the ground truth is also reported | No | Fuzzy C-Means and variants | Not specified | No formal validation | Yes |
| Ghosh et al. (2020) | Segmentation only | Intuitionistic fuzzy soft sets (IFSS) and multigranulation rough sets | MIAS and MedPix | Mean segmentation accuracy (SA): 88.46% (MIAS) and 86.32% (MedPix), outperforming all comparison methods | No | Other fuzzy operators | MIAS/Mini-MIAS; Other public (MedPix) | No formal validation | Yes |
| Jebathangam et al. (2021) | Segmentation only | Fuzzy logic segmentation | MIAS | Accuracy: 95%<br>Sensitivity: 86%<br>Specificity: 96% | No | Fuzzy inference system (unspecified) | MIAS/Mini-MIAS | No formal validation | No |
| Valencia-Hernandez et al. (2021) | Classification only | Takagi–Sugeno fuzzy classifier | BCDR and INbreast | Accuracy: 84.2% (BCDR) and 81.3% (INbreast) | Yes | Sugeno / Takagi–Sugeno | INbreast; BCDR | No formal validation | Yes |
| Altameem et al. (2022a) | Segmentation + classification | Fuzzy rank fusion based on the Gompertz function | Combination of DDSM, INbreast, Mini-MIAS and BCDR | Accuracy: 99.32% (Inception V4 with Gompertz function-based fuzzy rank ensemble) | No | Fuzzy–deep learning fusion | MIAS/Mini-MIAS; DDSM/CBIS-DDSM; INbreast; BCDR | Hold-out | Yes |
| Ghorbani et al. (2023) | Classification only | Hybrid fuzzy inference system with PSO (Fuzzy-PSO) | MIAS | Performance: 94.58% | No | Fuzzy inference system (unspecified) | MIAS/Mini-MIAS | Cross-validation | Yes |
| Ion et al. (2023) | Segmentation only | Fuzzy cellular automaton | Mini-MIAS | Accuracy: 98.66% (segmentation with fuzzy cellular automaton) and 92.46% (cellular automaton without fuzzy) | No | Fuzzy cellular automaton | MIAS/Mini-MIAS | No formal validation | Yes |
| Vidivelli & Sathiya Devi (2022) | Segmentation + classification | Fuzzy entropy segmentation | DDSM and MIAS | Dice: 0.822 (MIAS), 0.887 (DDSM)<br>Jaccard: 0.867 (MIAS), 0.876 (DDSM) | No | Fuzzy entropy | MIAS/Mini-MIAS; DDSM/CBIS-DDSM | Hold-out | Yes |
| Jamil et al. (2024) | Segmentation only | Unsupervised FCM on the difference image | MIAS (real mammography image) | Percentage of correct classification: 0.9737 to 0.9738 | No | Fuzzy C-Means and variants | MIAS/Mini-MIAS | No formal validation | Yes |
| Sannasi Chakravarthy et al. (2024) | Classification only | Fuzzy ranking with a modified Gompertz function to ensemble CNNs (VGG-11, Inception-v3, ResNet50) | BCDR, MIAS, INbreast and CBIS-DDSM | Accuracy: 98.986% (ResNet50), 98.086% (Inception v3), 97.072% (VGG-11) | No | Fuzzy–deep learning fusion | MIAS/Mini-MIAS; DDSM/CBIS-DDSM; INbreast; BCDR | Hold-out | Yes |
| Zeng et al. (2024) | Segmentation only | Fuzzy entropy | Private (First Hospital of Quanzhou) | Mean accuracy over the 18 images | Yes | Fuzzy entropy | In-house/private | No formal validation | Yes |
| Valencia-Hernández et al. (2025) | Segmentation + classification | Genetic programming guided by a fuzzy fitness function with medical criteria | INbreast and BCDR | Jaccard: 0.82 (INbreast), 0.78 (BCDR)<br>AUC: 0.91 (INbreast), 0.89 (BCDR) | Yes | Genetic-fuzzy | INbreast; BCDR | Cross-validation | Yes |
| Ion et al. (2025) | Segmentation only | Fuzzy cellular automaton | Mini-MIAS | Accuracy: 0.9953 (FCA with CA preprocessing) | No | Fuzzy cellular automaton | MIAS/Mini-MIAS | No formal validation | Yes |
| Lin et al. (2025) | Classification only | Density-based dynamic fuzzy rule interpolation | INbreast | The 'Promoted' rule base reaches up to 0.732 in later iterations, compared with 0.27 for the original sparse rule base (SRB); rule-space coverage of up to 98.84% | No | Fuzzy rule interpolation | INbreast | Hold-out | Yes |
| Zhou et al. (2025) | Classification only | Adaptive fuzzy transformation: FRI with Mahalanobis distance (MT-FRI) | INbreast, CBIS-DDSM, BCDR-D01, BCDR-F01 | MT-FRI: INbreast accuracy 0.8336, precision 0.9008, F1-score 0.8724<br>CBIS-DDSM recall 0.9825, F1-score 0.6402<br>BCDR-D01 accuracy 0.8930, precision 0.8987, recall 0.8246, F1-score 0.8600<br>BCDR-F01 accuracy 0.8277, precision 0.8771, F1-score 0.8223, recall 0.7739 | No | Fuzzy rule interpolation | DDSM/CBIS-DDSM; INbreast; BCDR | Cross-validation (+ hold-out) | Yes |
| Jelli & Pagadala (2026) | Classification only | Fuzzy Residual-ShuffleNet (Fuzzy RS-Net) after wavelet filtering and O-SegNet segmentation | DDSM, MIAS, CBIS-DDSM | Accuracy: 94.999%<br>Sensitivity: 95.899%<br>Specificity: 93.889% | No | Fuzzy–deep learning fusion | MIAS/Mini-MIAS; DDSM/CBIS-DDSM | Hold-out | Yes |
| Tran et al. (2026) | Classification only | Gaussian fuzzy inference module over an ensemble of 7 CNNs (GOOWE), FGOOPNet | VinDr-Mammo and a private database | Accuracy: 98.4%<br>F1-score: 98.29 (B), 98.5 (M)<br>Recall: 97.88% (B), 98.87% (M)<br>Precision: 98.72% (B), 98.13% (M) | No | Fuzzy–deep learning fusion | VinDr-Mammo; In-house/private | Hold-out | Yes |

## Coding criteria

- **Role of the fuzzy component (Fig. 5, Sec. 3.5):** *Segmentation only*: fuzzy c-means, fuzzy clustering, etc. used to delineate the lesion without classifying malignancy; *Classification only*: ANFIS or a fuzzy inference system used for diagnosis, without explicit segmentation; *Segmentation and classification*: fuzzy segmentation plus classification (fuzzy or not) in the same study; *Image preprocessing*: fuzzy logic used for contrast adjustment, noise reduction, etc.
- **Model category (Fig. 4, Sec. 3.4):** coded from the *Fuzzy model* column. A study may count in several categories when several techniques are explicitly mentioned; Sugeno and Mamdani are counted only when explicitly named; non-fuzzy components (SVM, CNN, PSO) are not counted.
- **Dataset category (Fig. 3, Sec. 3.3):** a study counts once for each dataset it uses (mentions). *In-house/private*: non-public institutional or hospital collections; *Other public*: IRMA, UCSF or MedPix; *Not specified*: the study does not identify its data source.
- **Validation (Sec. 3.7):** *Cross-validation*: k-fold or leave-one-out (including two studies that combine it with a hold-out split); *Hold-out*: simple training and test split; *No formal validation*: evaluation only by direct comparison with ground truth or by statistical tests; *Not reported*: the study does not describe its validation scheme.
- **Uses BI-RADS (Table 1, Sec. 3.6):** *Yes* when the study uses or predicts formal BI-RADS categories (assessment, density or shape).

## Summary (figures reported in the article)

**Role of the fuzzy component (Fig. 5)**

| Category | n | % of 65 |
|:--|--:|--:|
| Classification only | 31 | 47.7% |
| Segmentation only | 18 | 27.7% |
| Segmentation + classification | 13 | 20.0% |
| Image preprocessing | 3 | 4.6% |

**Linkage with BI-RADS (Sec. 3.6)**

| Category | n | % of 65 |
|:--|--:|--:|
| No | 45 | 69.2% |
| Yes | 20 | 30.8% |

**Validation (Sec. 3.7)**

| Category | n | % of 65 |
|:--|--:|--:|
| Cross-validation | 25 | 38.5% |
| No formal validation | 19 | 29.2% |
| Hold-out | 14 | 21.5% |
| Not reported | 7 | 10.8% |

**Comparison with other methods (Sec. 3.7)**

| Category | n | % of 65 |
|:--|--:|--:|
| Yes | 60 | 92.3% |
| No | 5 | 7.7% |

**Datasets (Fig. 3): mentions**

| Category | n | % of 65 |
|:--|--:|--:|
| MIAS/Mini-MIAS | 32 | 49.2% |
| DDSM/CBIS-DDSM | 15 | 23.1% |
| In-house/private | 11 | 16.9% |
| INbreast | 7 | 10.8% |
| BCDR | 6 | 9.2% |
| UCI Mammographic Mass | 5 | 7.7% |
| Not specified | 4 | 6.2% |
| Other public | 3 | 4.6% |
| VinDr-Mammo | 1 | 1.5% |
| *Total mentions* | 84 | n/a |

**Fuzzy models (Fig. 4): mentions**

| Category | n | % of 65 |
|:--|--:|--:|
| Fuzzy C-Means and variants | 15 | 23.1% |
| ANFIS | 7 | 10.8% |
| Fuzzy inference system (unspecified) | 6 | 9.2% |
| Neuro-fuzzy (generic) | 5 | 7.7% |
| Other fuzzy operators | 5 | 7.7% |
| Type-2 fuzzy | 5 | 7.7% |
| Fuzzy rule interpolation | 4 | 6.2% |
| Fuzzy–deep learning fusion | 4 | 6.2% |
| Fuzzy entropy | 3 | 4.6% |
| Fuzzy rule-based | 3 | 4.6% |
| Fuzzy-rough | 3 | 4.6% |
| Mamdani | 3 | 4.6% |
| Sugeno / Takagi–Sugeno | 3 | 4.6% |
| Fuzzy GrowCut | 2 | 3.1% |
| Fuzzy cellular automaton | 2 | 3.1% |
| Genetic-fuzzy | 2 | 3.1% |
| Fuzzy SVM | 1 | 1.5% |
| Fuzzy cognitive maps | 1 | 1.5% |
| *Total mentions* | 74 | n/a |

**Distribution by year (Fig. 2)**

| Year | n |
|:--|--:|
| 2010 | 5 |
| 2011 | 4 |
| 2012 | 3 |
| 2013 | 3 |
| 2014 | 1 |
| 2015 | 5 |
| 2016 | 7 |
| 2017 | 3 |
| 2018 | 8 |
| 2019 | 4 |
| 2020 | 6 |
| 2021 | 3 |
| 2022 | 2 |
| 2023 | 2 |
| 2024 | 3 |
| 2025 | 4 |
| 2026 | 2 |

