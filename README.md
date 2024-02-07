# Cataract-1K


Dataset release for "Cataract-1K: Cataract Surgery Dataset for Scene Segmentation, Phase Recognition, and Irregularity Detection"
=================================================================================================================================

The Cataract-1K dataset consists of 1000 videos of cataract surgeries performed in the eye clinic of Klinikum Klagenfurt from 2021 to 2023. From these videos, we provide surgical phase annotations for 56 regular videos and relevant anatomical plus instrument pixel-level annotations for 2256 frames out of 30 cataract surgery videos. Furthermore, we provide a small subset of surgeries with two major irregularities including "pupil reaction" and "IOL rotation" to support further research on irregularity detection in cataract surgery. Except for the annotated videos and images, the remaining videos in Cataract-1K dataset are encoded with a temporal resolution of 25 fps and the spatial resolution of (512,324). Besides, we assess the surgeons' skills by considering the cumulative count of their completed surgeries, which spans from 1000 to over 40000 procedures in the Cataract-1K dataset. We delineate the annotation procedures for each subset within the dataset in the following paragraphs.

Phase recognition dataset
-------------------------

As shown in **Figure 1**, a regular cataract surgery can include twelve action phases, including incision, viscoelastic, capsulorhexis, hydrodissection, phacoemulsification, irrigation-aspiration, capsule polishing, lens implantation, lens positioning, viscoelastic-suction, anterior-chamber flushing, and tonifying/antibiotics. Besides, the idle phases refer to the time spans in the middle of a phase or between two phases when the surgeons mainly change the instruments and no instrument is visible inside the frames.

  

Your browser does not support the video tag.

Incision

Your browser does not support the video tag.

Viscoelastic

Your browser does not support the video tag.

capsulorhexis

Your browser does not support the video tag.

Hydrodissection

Your browser does not support the video tag.

phacoemulsification

Your browser does not support the video tag.

Irrigation-Aspiration

Your browser does not support the video tag.

Capsule Polishing

Your browser does not support the video tag.

Lens Implantation

Your browser does not support the video tag.

Lens Positioning

Your browser does not support the video tag.

Viscoelastic-Suction

Your browser does not support the video tag.

Anterior-Chamber Flushing

Your browser does not support the video tag.

Tonifying/Antibiotics

Your browser does not support the video tag.

Idle

**Figure 1.** Different phases in a regular cataract surgery

  

We provide a large annotated dataset to enable comprehensive studies on deep-learning-based phase recognition in cataract surgery videos. **Table 1** visualizes the phase annotations corresponding to 56 normal cataract surgery videos, with a spatial resolution of (1024,768), a temporal resolution of 30 fps, an average duration of 6.45 minutes, and a standard deviation of 2.04. This dataset comprises patients with an average age of 75 years, ranging from 51 to 93 years, and a standard deviation of 8.69 years. The videos present in the phase recognition dataset correspond to surgeries executed by surgeons with an average experience of 8929 surgeries and a standard deviation of 6350 surgeries. Frame-level annotations for phase recognition are provided in CSV files, determining the first and the last frames for all action phases per video. The preprocessing codes to extract all action and idle phases from a video using the CSV files are provided in the GitHub repository of the paper. Furthermore, **Figure 2** demonstrates the total duration of the annotations corresponding to each phase from 56 videos.

  

![](imgs/Table1.png)

**Table 1.** Total duration of the annotated phases in the 56 annotated cataract surgery videos (in seconds).

  

![](imgs/pie_chart.png)

**Figure 2.** Total duration of the annotated phases in the 56 annotated cataract surgery videos (in seconds).

Semantic segmentation dataset
-----------------------------

**Figure 3** visualizes pixel-level annotations for relevant anatomical objects and instruments.

  

![](imgs/Figure3.png)

**Figure 3.** Visualization of pixel-based annotations corresponding to relevant anatomical structures and instruments in cataract surgery and the challenges associated with different object.

The semantic segmentation dataset includes frames from 30 regular videos of cataract surgery with a spatial resolution of (1024,768). Frame extraction is performed at the rate of one frame per five seconds. Subsequently, the frames featuring very harsh motion blur or out-of-scene iris are excluded from the dataset. We provide pixel-level annotations for three relevant anatomical structures, including iris, pupil, and intraocular lens, as well as nine instruments used in regular cataract surgeries including slit/incision knife, gauge, spatula, capsulorhexis cystome, phacoemulsifier tip, irrigation-aspiration, lens injector, capsulorhexis forceps, and katana forceps. All annotations are performed using polygons in the [Supervisely platform](https://supervisely.com/), and exported as JSON files. Within this dataset, the included individuals possess an average age of 74.5 years, spanning from 51 to 90 years, with a standard deviation of 8.43 years. Additionally, the videos contained in the phase recognition dataset depict surgeries conducted by surgeons whose collective experience averages 8033 surgeries, with a standard deviation of 3894 surgeries. The provided dataset enables a reliable study of segmentation performance for relevant anatomical structures, binary instruments, and multi-class instruments. Pixel-level annotations are provided in two formats: (1) Supervisely format, for which we provide Python codes for mask creation from JSON files, and (2) COCO format, which also provides bounding box annotations for all pixel-level annotated objects. The latter annotations can be used for object localization problems. The preprocessing codes to create training masks for "anatomy plus instrument segmentation", "binary instrument segmentation", and "multi-class instrument segmentation" are provided in the GitHub repository of the paper. We have formed five folds with patient-wise separation, meaning every fold consists of the frames corresponding to six distinct videos. **Table 2** compares the number of instances and their appearance percentage in the frames. Besides, **Table 3** lists the average number of pixels per frame corresponding to each label.

  

![](imgs/Table2.png)

**Table 2.** Number of instances and presence in the frames (% of total number of frames in each fold).

  

![](imgs/Table3.png)

**Table 3.** Average pixels corresponding to different labels per frame.

Irregularity detection dataset
------------------------------

This dataset contains two small subsets of major intra-operative irregularities in cataract surgery, including pupil reaction and lens rotation.

*   **Pupil Contraction:** During the phacoemulsification phase, where the occluded natural lens is corrupted and suctioned, the amount of light received by photoreceptors may suddenly increase. This increase in light reception affects the size of the pupil, usually resulting in slow (gradual) pupil contraction. In some cases, however, the pupil unexpectedly reacts to the lighting changes and becomes quickly contracted. These sudden reactions in pupil size can lead to serious intra-operative implications. Especially during the phacoemulsification phase where the instrument is deeply inserted inside the eye, sudden changes in pupil size may lead to injuries to the eye’s tender tissues. Besides, achieving precise IOL alignment or centration becomes challenging in cases where intraoperative pupil contraction (miosis) occurs. Particularly in multifocal IOLs, minor displacements or tilts, which might be negligible for conventional mono-focal IOLs, can significantly compromise visual performance. In the case of toric IOLs, precise alignment of the torus is crucial, as any deviation diminishes the IOL's effectiveness. Detection of unusual pupil reactions and severe pupil contractions during the surgery can highly contribute to the overall outcomes of cataract surgery and provide important insight for further post-operative investigations. Figure 4-top demonstrates an example of severe pupil contraction during cataract surgery.
*   **IOL rotation:** Although aligned and centered upon surgery's conclusion, the IOL may rotate or dislocate following the surgery. Even slight deviations, such as minor misalignments of the torus in toric IOLs or the slight displacement and tilting of multifocal IOLs, can result in significant distortions in vision and leave patients dissatisfied. The sole way to address this postoperative complication is follow-up surgery, entailing added costs, heightened surgical risks, and patient discomfort. Identification of intra-operative indicators for predicting and preventing post-surgical IOL dislocation is an unmet clinical need. It is argued that intra-operative rotation of IOLs during cataract surgery is the leading cause of post-operative misalignments. Hence, automatic detection and measurement of intra-operative lens rotations can effectively contribute to preventing post-operative IOL dislocation. Figure 4-bottom represents fast clockwise rotations of IOL during unfolding, which occur in less than seven seconds.

  

![](imgs/Figure4.png)

**Figure 4.** Intra-operative irregularities in cataract surgery.

* * *

Disclaimer
----------

The datasets are exclusively provided for **scientific research purposes** and as such cannot be used commercially or for any other purpose. If any other purpose is intended, you may directly contact the originator of the dataset, [Prof. Yosuf El-Shabrawi](mailto:Yosuf.El-Shabrawi@kabeg.at), or [Assoc. Prof. DI Dr. Klaus Schoeffmann](mailto:ks@itec.aau.at).  
  
Besides, a reference must be made to the following publication when this dataset is used in any academic and research reports:  
  
Ghamsarian, N., El-Shabrawi, Y., Nasirihaghighi, S. Putzgruber-Adamitsch, D., Zinkernagel, M., Wolf, S., Schoeffmann, K., Sznitman, R.: Cataract-1K: Cataract Surgery Dataset for Scene Segmentation, Phase Recognition, and Irregularity Detection (to appear)  
  

BibTeX:

@inproceedings{Cataract-1K,
    author    = {Negin Ghamsarian and
                Yosuf El-Shabrawi and
                Sahar Nasirihaghighi and
                Doris Putzgruber-Adamitsch and
                Martin Zinkernagel and
                Sebastian Wolf and
                Klaus Schoeffmann and
                Raphael Sznitman},
    title     = {Cataract-1K: Cataract Surgery Dataset for Scene Segmentation, Phase Recognition, and Irregularity Detection (to appear)},
    
}

The datasets are licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY, [![Creative Commons License](https://licensebuttons.net/l/by/4.0/80x15.png)]([https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by/4.0/))) and are created as well as maintained by Distributed Multimedia Systems Group of the Institute of Information Technology (ITEC) at Alpen-Adria Universität in Klagenfurt, Austria.

This license allows users of this dataset to copy, distribute, and transmit the work under the following conditions:

*   Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
*   Non-Commercial: You may not use the material for commercial purposes.

For further legal details, please read the complete [license terms](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

* * *

Download
--------

If you agree to above conditions, you are free to download:

*   [Catatact-1k](./downloads/Dataset_phase.zip) ( GB)
*   [Phase Recognition Set](./downloads/Dataset_phase.zip) ( GB)
*   [Semantic Segmentation Set](./downloads/Dataset_lens.zip) ( MB)
*   [Irregularity Detection Set](./downloads/Dataset_pupil.zip) ( MB).
*   [Dataset Preparation Codes](https://github.com/Negin-Ghamsarian/Cataract-1K) ( MB).

* * *

Copyright @ [ITEC Institute](https://itec.aau.at/), [AAU Klagenfurt](https://www.aau.at/).
