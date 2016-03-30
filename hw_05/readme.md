# Ad Hoc Information Retrieval
Katy Herrick | 3/30/16

### Overview
In this project, I was given two text files:
1. `cran.qry`, which contains 225 search queries
2. `cran.all.1400` which contains 1400 research paper abstracts and associated information, such as author, bibliographic info, etc.

The goal was calculate the similarity of each search query to each abstract, and then rank the most relevant abstracts for each query. To run, simply run
``` shell
python main.py
```
from the root directory. This will generate a file called `output_file.txt` with 3 columns:
| Query ID | Abstract ID | Cosine Similarity Score  |
|:--|:--|:--|
|001 | 878 | 0.547009993528 |
|001 | 486 | 0.527114275295 |
|001 | 12 | 0.507882017581 |
| ... | ... | ... |
|365 | 1362 | 0.276715974355 |

##### File Parsing
Parsing the original files was more difficult than expected. Each abstract is separated by a new line with ".I" followed by the abstract number, but the twist is that although there are 1400 abstracts, they aren't numbered consecutively. So, I couldn't put the abstract text into a list and index into it that way. To maintain the integrity of the abstract/query IDs, I created a dictionary of the form
``` python
{'abstract/query_id': ['token_1': token_1_freq, 'token_2': token_2_freq,... 'token_n': token_n_freq}
```
where each token is a word of abstract/query (excluding numbers, and common English words such as 'the', 'of', 'what', etc.)

Adding to the parsing issues, each abstract text was filled with newline characters so that the text wouldn't stretch past the 80-character line limit, so I had to stitch the abstract and query texts back together as I parsed the file.

##### Making Feature Vectors
After I had my query and abstract texts organized into dictionaries, I then had to represent each query's search intent mathematically. Luckily, linguists before me came up with a method for that called a feature vector. A feature vector is a list of each relevant word in the text, along with each word's term-frequency-inverse-document-frequency. 

Without going too much into it, a high TF-IDF means that the word is important and should be weighted higher than other words in the text when determining search intent. A word will have a high TF (term-frequency) if it shows up many times in the text, and it will have a high IDF if it only shows up in a few other texts. To calculate these numbers, I had to count the number of times each word was repeated in each text, as well as the number of texts each word was used in. 

After creating all 225 query feature vectors, I created TF-IDF feature vectors for each abstract in relation to each query. One might think that each abstract only needs to have one feature vector to represent its intent, but since I needed to compare each _pair_ of abstracts and queries, it's helpful to have the vectors I'm comparing to be the same length and only across the same words. 

##### Calculating Cosine Similarities
Once I had all of the query-abstract feature vector pairs, I calculated the cosine similarity between them. One can think of each feature vector as a line pointing out in some direction in space, and calculating cosine similarity gives a value between 0 and 1 that represents how similar those two directions are. Values closer to 1 signify greater correlation, while 0 means that the two vectors have nothing in common.

##### Results
I return a list of abstract IDs for each query in order of decreasing cosine similarity (i.e. in order of decreasing relevance to the query), excluding any results with cosine similarity scores of 0.

---
##### Future Improvements
The main limitation of this program is that it is specifically designed to read in these strangely formatted input files, and therefore would have to be entirely refactored to create the necessary feature vectors out of another type of file.

The program also takes about 3 minutes to run, which can certainly be improved. I attribute most of the inefficiency to to the way in which I am sorting the results. For each of the 225 queries, I create a new list which simulates a sorted dictionary of length 1400. That eats up a lot of processing time, when I could most likely have created the list to be ordered in the first place.