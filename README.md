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
Different aspects have different levels of specificity required to answer them. Some aspects like "Visa" have very technical questions, whereas other aspects like "Destinations" would have recommendations and opinions. Doing an aspect coverage check would help us gather thoughts and make observations on which aspects are covered the most by these platforms. 

#### Technique
We take collection of queries from all the aforementioned platforms and generate a set of uni,bi,tri-grams from them. We pool in all these n-grams into a universal pool. We perform a bayesian non-parametric clustering called distance dependent chinese restaurant process (DDCRP) over this universal pool of ngrams. This clustering method is specifically chosen as there is no need to specify the number of clusters desired - it is automatically inferred from the collection of ngranms. The distance required by the algorithm is modelled over the cosine similarity between the average word2vec embeddings formed by the individual words in an ngram. It should be noted that this algoithm being a derivative of the Dirichlet Process, is non-deterministic in nature. The algorithm returns a set of clusters containing ngrams. These clusters are mapped back to the original ngram collection to check the purity. The amount of purity in these clusters determine the different aspects of tasks which these platforms aid in solving.

#### Results
The results we obtain from these platforms shows the division of platforms among several different aspects of travel. We also use the TaskHierarchy138K to label the clusters which were formed to make a sense of the observations.

| Aspect Clusters | Wikihow | Reddit | Quora | StackExchange | Aspect Labels |
|---|---|---|---|---|---|
| [('wander', 'new', 'york'), ('las', 'vegas'), ('miami', 'new', 'york'), ('new', 'york', 'city'), ('washington', 'dc'), ('san', 'francisco'), ('la', 'new', 'york'), ('bus', 'new', 'york')]| [x] | [] | [] | [] | United States Travel |
| [('schengen', 'visa'), ('tourist', 'visa'), ('multipleentry', 'schengen', 'visa'), ('visitor', 'visa'), ('apply', 'schengen', 'visa'), ('visa', 'application'), ('schengen', 'visa', 'waiver')]| [] | [x] | [] | [] | Official Travel Documentation |
|[('unmarried', 'couples')]| [] | [] | [x] | [] | Traveling with Companions |
| [('sri', 'lanka'),('grand', 'canyon')]| [] | [] | [] | [x] | Around the World Travel |


### Quantitative Analysis with TREC Tasks

#### Why?
TREC Tasks are well curated set of subtasks being done to cover a particular task. Different subtasks have different levels of technicality associated with it. For example, a task like "Planning a Wedding" will have subtasks like "Buying a wedding cake" which is an opinion task based on the cost, shape, size, design etc. and other subtasks like "Wedding Registration with the government" which would be highly technical having very specific steps of fulfilling it. Hence, there exists a need to compare these subtasks with the questions being asked on the mentioned platforms.

#### Technique

We use TREC Tasks dataset from last 3 years for this purpose. Each dataset contains 150 tasks and their suggestive subtasks. These list of subtasks ideally represent the entirety of solving that particular task. We compare the formed aspects and their subtasks with these standard task-subtask relationship. In our case, we limit our analysis to a specific domain - Travel and hence, gather tasks which represent travel.

We perform 3 separate analysis to gather insights on which platform can help in solving our needs:
* Likelihood of a subtask being covered by a specific platform (The no. of questions which lie above a certain semantic similarity threshold) {This needs to be more precise, also has the classifier been validated? How much is the error?}
* Most accurate subtask being covered by a specific platform (The highest semantic similarity obtained for a subtask)
* Quality of a subtask being solved by a platform (The average semantic similarity of the top-10 questions)  {I am not sure this can be called quality, it sounds more like quantity}

{These measurements may not be measuring what you claim to measure. These need to be or 1) validated by doing a manual assessment of a sample, or if possible 2) completely avoided by doing manual assessment of everything. I believe the first may be sufficient.}


#### Results



From the evaluation of the aspects against tasks from the TREC Task dataset, it can be observed that StackExchange tends to solve technical aspects of solving a task and have only one right answer for eg. getting a visa, checking for weather. Quora and Reddit help extensively with recommendations which are effectively opinions from general public - Its intention can be seen from there being answers which are upvoted/downvoted based on their popularity and there is no one right answer as compared to StackExchange. Wikihow fares low on all the scores because.

### Unanswered Questions

#### Why?
We make a hypothesis that different platforms have induced a bias in the way people ask questions on each of them. However, rather than it being a natural bias, there might be moderation on each platform which remove/close questions which are not relevant to the platform. We need to check the unanswered questions to make sense of such data and this will help in supporting the argument for "natural" bias rather than a "moderated" bias.

#### Technique

#### Results
