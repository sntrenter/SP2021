## C. Phases

**In each phase you are exepected to submit:**

1. An HTML version of the notebook
   - If you are using Google Colab, please convert the notebook to `.html` files and submit the `.html` files, for example using [htmltopdf](https://htmtopdf.herokuapp.com/ipynbviewer/).
1. A PDF report describing your findings (downloaded from your Overleaf project). The reports for the first three phases can be as long as you make them but the final report has limit on the number of pages.
1. A link to view your Overleaf project.

## Tip for preparing notebooks

1. Read the [Ten Simple Rules for Reproducible Research in Jupyter Notebooks](https://arxiv.org/pdf/1810.08055.pdf)

Below is the list of all phases and the outline of what you will be working on in each phase.

### Phase I. Data preparation

1. Watch the lectures in [Module 5](https://github.com/badriadhikari/Deep-Learning/blob/main/LECTURES.md#5-preparing-images-for-deep-learning-sections-362-524-and-525).
1. In this phase the first task is to decide a dataset for your project. If you don't have any other project in mind, please choose to work on a "mood classification" project. For the mood classification project, you will need to decide a few moods you want to detect (smiling, laughing, crying, neutral, etc.) and take a few hundred pictures for each mood. For example, you will need to take around 200 pictures of you smiling in various lighting conditions, various clothings, and in various places. It may run into your mind to create a video instead and extract frames as images but previous students have achived almost 100% accuracy with such approach so I don't encourage that.
1. The next step is to organize the dataset and visualize the images. A clean way to organize the images is to put them in folders by their categories. For example, put all 'smiling' pictures in one folder. The next step is to visualize sample images (a few images from your ~1000 images) in a Jupyter Notebook.
1. In your report you should discuss distribution of output labels, i.e., a bar diagram (or a table) showing how many images belong to which categories.
1. In your report you should also discuss how you plan to normalize your input images.
