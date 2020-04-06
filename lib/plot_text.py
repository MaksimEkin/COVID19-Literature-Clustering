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
description2 = Div(text="""<h3>Approach:</h3>
<ul>
  <li>Parse the text from the body of each document using Natural Language Processing (NLP). </li>
  <li>Turn each document instance di into a feature vector Xi using Term Frequency–inverse Document Frequency (TF-IDF).</li>
  <li>Apply Dimensionality Reduction to each feature vector Xi using t-Distributed Stochastic Neighbor Embedding (t-SNE) to cluster similar research articles in the two dimensional plane X embedding Y1.</li>
  <li>Use Principal Component Analysis (PCA) to project down the dimensions of X to a number of dimensions that will keep .95 variance while removing noise and outliers in embedding Y2.</li>
  <li>Apply k-means clustering on Y2, where k is 20, to label each cluster on Y1.</li>
  <li>Apply Topic Modeling on X using Latent Dirichlet Allocation (LDA) to discover keywords from each cluster.</li>
  <li>Investigate the clusters visually on the plot, zooming down to specific articles as needed, and via classification using Stochastic Gradient Descent (SGD).</li>  
</ul> 
<p>Total of <b>29,240 samples</b> analysed. Articles that are not English dropped.</p1>""")

# citation
cite = Div(text="""<p1><h3>Citation:</h3><a href="https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge">COVID-19 Open Research Dataset Challenge (CORD-19) | Kaggle</a></p1>
<br><br>
<p1><a href="https://www.whitehouse.gov/briefings-statements/call-action-tech-community-new-machine-readable-covid-19-dataset/">Call to Action to the Tech Community on New Machine Readable COVID-19 Dataset | White House</a></p1>
<br><br>
<p1>Inspired by Dr. Charles Nicholas's "Mr. Shakespeare, Meet Mr. Tucker", High Performance Computing and Data Analytics Workshop, September 10-11, 2019.  Linthicum Heights, MD, USA</p1>
<br><br>
<p1>Raff, Edward and Nicholas, Charles and McLean, Mark. The Thirty-Fourth AAAI Conference on Artificial Intelligence. A New Burrows Wheeler Transform Markov Distance. 2020.</p1>""")

description_search = Div(text="""<h3>Filter by Text:</h3><p1>Search keyword to filter out the plot. It will search abstracts, 
titles, journals, and authors. Please keep in mind that only 150 words of abstracts, and first 2 authors are kept in the plot to reduce the size. Press enter when ready. 
Clear and press enter to reset the plot.</p1>""")

description_slider = Div(text="""<h3>Filter by the Clusters:</h3><p1>The slider below can be used to filter the target cluster. 
Simply slide the slider to the desired cluster number to display the plots that belong to that cluster. 
Slide back to 20 to show all.</p1>""")

description_keyword = Div(text="""<h3>Keywords:</h3>""")

description_current = Div(text="""<h3>Selected:</h3>""")

notes = Div(text="""<h3>Contact:</h3><p1>Malware Research Group, University of Maryland Baltimore County (UMBC). <br>
                                <b>Project Author: </b>Maksim Ekin Eren (meren1@umbc.edu), Nick Solovyev (sonic1@umbc.edu)<br>
                                <b>PI: </b>Dr. Charles Nicholas<br>
                                <b>GitHub: </b><a href="https://github.com/MaksimEkin/COVID19-Literature-Clustering">https://github.com/MaksimEkin/COVID19-Literature-Clustering</a>
                                <br><br><b>Many thanks to</b> Charles Varga, Felix Dogbe, Karsten Suhre, and Mark Mohades
<b>for their contributions and ideas.</b> </p1>
<br>                               
<h3>Latest Update:</h3><p1>Now using <a href="https://github.com/allenai/scispacy/blob/master/README.md">en_core_sci_lg</a> for tokenization. Using the new dataset with more articles. Click on a plot to show the link to the article.</p1>
<h4><a href="https://maksimekin.github.io/COVID19-Literature-Clustering/plots/t-sne_covid-19_interactive_old.html">Old version of the plot</a></h4>""")

dataset_description = Div(text="""<h3>Dataset Description:</h3><p1><i>'In response to the COVID-19 pandemic, the White House and a coalition of leading research groups have prepared the COVID-19 Open Research Dataset (CORD-19). CORD-19 is a resource of over 47,000 scholarly articles, including over 36,000 with full text, about COVID-19, SARS-CoV-2, and related coronaviruses. This freely available dataset is provided to the global research community to apply recent advances in natural language processing and other AI techniques to generate new insights in support of the ongoing fight against this infectious disease. There is a growing urgency for these approaches because of the rapid acceleration in new coronavirus literature, making it difficult for the medical research community to keep up.'</i> - Kaggle</p1>""")



