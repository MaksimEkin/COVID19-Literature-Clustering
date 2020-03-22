from bokeh.models import Div

#header
header = Div(text="""<h1>COVID-19 LITERATURE CLUSTERING</h1>""")

# title for the toolbox
toolbox_header = Div(text="""<h1>Toolbox:</h1>""")

# project description
description = Div(text="""<p1>Given a large amount of literature regarding the rapidly spreading <b>COVID-19</b>, 
it is difficult for a scientist to keep up with the research community promptly. <u>Can we cluster similar research articles 
together to make it easier for health professionals to find relevant research articles?</u> Clustering can be used to create 
a tool to identify similar articles, given a target article. It can also reduce the number of articles one has to go through as 
one can focus on a cluster of articles rather than many different kinds. On this plot, we demonstrate how clustering can 
be used to achieve this. 
This project is done for <b>Kaggle</b>'s <a href="https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge">COVID-19 Open Research Dataset Challenge (CORD-19)</a>.</p1>""")

# steps description
description2 = Div(text="""<h3>Approach:</h3><p1>This scatter plot is generated using <b>plain text</b> from the body of 
each article as a feature. Then each instance is turned into features vector using Sklearn's <b>TfidfVectorizer</b>. 
Then, Dimensionality Reduction is applied to the feature vectors using Sklearn's <b>t-SNE</b>. Finally, labels are 
generated with the means of clustering using Sklearn's <b>k-Means</b> where k=20. <b>Topic Modeling</b> is done on each cluster
to get the keywords per cluster. <b>spaCy</b> is used to tokenize each instance first. Then, Sklearn's <b>CountVectorizer</b> is used to vectorize the features. Finally, Sklearn's <b>LatentDirichletAllocation</b> trained to get the keywords. Total of <b>26,043 samples</b> analysed.</p1>""")

# citation
cite = Div(text="""<p1><h3>Citation:</h3><a href="https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge">COVID-19 Open Research Dataset Challenge (CORD-19) | Kaggle</a></p1>
<br><br>
<p1><a href="https://www.whitehouse.gov/briefings-statements/call-action-tech-community-new-machine-readable-covid-19-dataset/">Call to Action to the Tech Community on New Machine Readable COVID-19 Dataset | White House</a></p1>
<br><br>
<p1>Inspired by Dr. Charles Nicholas's "Mr. Shakespeare, Meet Mr. Tucker", High Performance Computing and Data Analytics Workshop, September 10-11, 2019.  Linthicum Heights, MD, USA</p1>""")

description_search = Div(text="""<h3>Filter by Text:</h3><p1>Search keyword to filter out the plot. It will search abstracts, 
titles, journals, and authors. Please keep in mind that only 150 words of abstracts are kept in the plot. Press enter when ready. 
Clear and press enter to reset the plot.</p1>""")

description_slider = Div(text="""<h3>Filter by the Clusters:</h3><p1>The slider below can be used to filter the target cluster. 
Simply slide the slider to the desired cluster number to display the plots that belong to that cluster. 
Slide back to 20 to show all.</p1>""")

notes = Div(text="""<h3>Notes:</h3><p1>I hope you enjoyed this plot, and I hope it will be helpful for someone. 
Please feel free to make any recommendations to improve the project. Please feel free to reach out to me on 
                                <a href="https://www.linkedin.com/in/maksimeren/">LinkedIn (MaksimEren)</a> for any questions.
                                <br><br><b>Project Author: </b>Maksim Ekin Eren<br>
                                <b>GitHub: </b><a href="https://github.com/MaksimEkin/COVID19-Literature-Clustering">https://github.com/MaksimEkin/COVID19-Literature-Clustering</a>
                                <br><b>Many thanks to</b> Nick Solovyev, Charles Varga, and Felix Dogbe <b>for their contributions.<b/> </p1>""")

dataset_description = Div(text="""<h3>Dataset Description:</h3><p1><i>'In response to the COVID-19 pandemic, 
the White House and a coalition of leading research groups have prepared the COVID-19 Open Research Dataset 
(CORD-19). CORD-19 is a resource of over 44,000 scholarly articles, including over 29,000 with full text, 
about COVID-19, SARS-CoV-2, and related coronaviruses. This freely available dataset is provided to the global 
research community to apply recent advances in natural language processing and other AI techniques to generate 
new insights in support of the ongoing fight against this infectious disease. There is a growing urgency for these 
approaches because of the rapid acceleration in new coronavirus literature, making it difficult for the medical 
research community to keep up.'</i> - Kaggle</p1>""")

