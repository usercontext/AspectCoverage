# Platform Bias

## Introduction
People are ever curious and are always asking questions around. With the advent of internet, it has become several times easier to get one's queries cleared. People rely heavily on community question answering platforms where different users (probably experts in the question topic) contribute their knowledge by answering those questions. At present, there are several very commonly used community question answering platforms. These include Quora, StackExchange, Yahoo Answers, Reddit, Wikihow (in some way). Each of these platforms have a unique format of asking and answering questions. We intend to study whether these different formats have intentionally created a bias in the questions that are being asked on these platforms.

## Community Question Answering platforms
### Quora
Quora is a Single Inquirer Multiple Responder (SIMR) platform. Questions are asked by individuals and are answered by other users on the platform. There is no need to be an expert to answer these questions. The answerer can mention the credentials of why they are an apt person to answer that particular question. The answers are rated based on an upvote button. However, upvote numbers cannot be used to rank the answers among each other. This is due to the way the answers are pushed in the Quora feed. Upvotes are like "+1" which means that they agree with the content.

### StackExchange
StackExchange is also a SIMR platform. The unsaid rule of the platform is that the answerer has to have some level of expertise to answer the question. The user's credential are shown through the points they have collected and can give the OP a fair idea of how much to trust that answer. OP also has an option to choose one answer among several others which worked for them.

### Yahoo! Answers
Yahoo! Answers is also an SIMR platform and is very similar to structure with Quora.

### Reddit
Reddit is a MIMR platform.

### Wikihow
Wikihow is not exactly a CQA platform. However, the questions are asked and articles are written by crowd sourcing. Each of the articles are moderated for their content. Expertise of the author is shown by a verification mark on their profile along with their ratings. The articles can also be rated based on the helpfulness which is an apt measurement owing to this platform helping in solving tasks.

## Definitions

Aspects: 
Tasks:


## Analysis

### Aspect Coverage

#### Why?

#### Technique
We take collection of queries from all the aforementioned platforms and generate a set of uni,bi,tri-grams from them. We pool in all these n-grams into a universal pool. We perform a bayesian non-parametric clustring called distance dependent chinese restaurant process (DDCRP) over this universal pool of ngrams. This clustering method is specifically chosen as there is no need to specify the number of clusters desired - it is automatically inferred from the collection of ngranms. The distance required by the algorithm is modelled over the cosine similarity between the average word2vec embeddings formed by the individual words in an ngram. It should be noted that this algoithm being a derivative of the Dirichlet Process, is non-deterministic in nature. The algorithm returns a set of clusters containing ngrams. These clusters are mapped back to the original ngram collection to check the purity. The amount of purity in these clusters determine the different aspects of tasks which these platforms aid in solving.

#### Results
The results we obtain from these platforms shows the division of platforms among several different aspects.

### Quantitative Analysis with TREC Tasks

#### Why?

#### Technique

#### Results

### Unanswered Questions

#### Why?

#### Technique

#### Results
