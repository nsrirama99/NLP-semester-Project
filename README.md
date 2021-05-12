# NLP-semester-Project

This project includes several python scripts that can be utilized in order to create the results showcased in our presentation and technical report.

## PDF to Text Conversion
This project utilizes text files as input data. If new test datasets are desired, and they exist in pdf form, you can run the "convert pdf to text.py" file in order to convert the pdf. The final version of this project did not require us to utilize this conversion, so the python script is not fully modular, and may require some editing depending on where the desired pdf file exists on your local machine.

## Protein Name Recognition
The initial part of the project exists in the "NLP final Part1.ipynb" file. This notebook contains scripts taht were used to parse a medical text in .json form. This is the main data that was utilized in the project. The first part of the program is a copy of the readJson.py file. It transfer the json text into a list. The output save as "paper"
The secound part of program consist of many regular expressions. Each of them filter out some possible protein names. The added up all the output of the regular expressions is a list called "protein_words". The final output of the protein name before match with protein database is "protein_words_final”.
The last part of the program is to match the "protein_words_final” with our protein name database. The output of it save into "list2". Then, the next step is to match the words with sentense with "paper" variable. 
The final output of the progarm saved as a pickle file. 


## Cluster Analysis
In order to analyze the extracted sentences from the Protein Name Recognition section, we created a "tagger-and-edit-dist.py" script. 
This python script expects an input argument. The argument should be the path and name of a pickle file which contains the list of extracted sentences. 
These sentences are then converted into simple character strings utilizing the parts of speech of each word. Python’s NLTK package defines a total of thirty-one parts of speech (POS). These parts of speech were then grouped into thirteen groups of similar POS. Each group was then assigned a single character that would be used in place of any POS within that group. The goal is to utilize a string of the characters defined for each group in order to measure distance. The initial data at this step is a list of sentences that were identified utilizing the Protein Name Recognition python notebook. Each sentence is then run through NLTK’s word tokenizer and POS tagger, to get a list of words and their associated POS. Then, for each word the POS is checked against the POS groups we’ve defined, and a character is appended to a string depending on what group the word falls under.
This is all handled automatically by the program once the input argument has been supplied. Editing distance is then used to create an NxN matrix (N = number of sentences in dataset) of distances between all sentences. This matrix is fed into a scipy Hierarchical clustering function that creates a single-link clustering. This cluster is then visualized using a Dendrogram with pyplot, and output to the console.

## filename.pkl
This is the pickle file that was generated by the protein name recognition script and is utilized in the Cluster analysis section. It is based off of the data supplied by the "test-json.json" file.
