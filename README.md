# NLPCC-2024-Shared-Task-9
Chinese Metaphor Generation Task
# Task Introduction
This task is designed to generate Chinese metaphors using machine learning techniques by either effectively identifying the ground or vehicle in the metaphoric relation. It is divided into two subtasks:

SUBTASK 1. Metaphor Generation, which involves creating a metaphor from a provided tuple consisting of TENOR, GROUND, and VEHICLE. The goal here is to synthesize a metaphor that aptly connects the subject (TENOR) with the object (VEHICLE), guided by the concept of the GROUND.

SUBTASK 2. Metaphor Components Identification, aimed at extracting the TENORs, GROUNDs, and VEHICLEs from a metaphorical sentence. This component requires the identification of metaphor elements that correspond to the specified grounds.
## Data Description & Rules

### Train Data

In our training data we provide the format like:

```
    {
        "metaphor_id": 0,
        "context": "天空随意飘着几朵白云 棉花糖一样如你般的纯净 打开手机看到今天天气晴 如果有可能想带你去远行 某年某月某日几点零几",
        "tenor": "白云",
        "vehicle": "棉花糖",
        "ground": "白色的外形",
        "sub_id": 0
    },
```
**we allow you to use extra data apart from our provided training data**

### Validation & Test Data:

We will provide you with multiple-choice questions, each containing four options. Based on the descriptions of two tasks, task 1 and task 2, please select the option that most closely aligns with the given metaphor.

#### Subtask 1: Data Format and Files
Data format details and file links for Subtask 1 are provided below:

- **Validation File:** The validation data includes the following fields: `本体, 喻体, 共性, 正确选项, 选项A, 选项B, 选项C, 选项D`.  
  [View the Validation File](./data/data/test/track1_validation.csv)

- **Test File:** The test data includes these fields: `本体, 喻体, 共性, 选项A, 选项B, 选项C, 选项D`. You will need to determine the correct option among the four provided.  
  [View the Test File](./data/data/test/track1_test.csv)

#### Subtask 2: Data Format and Files
Data format details and file links for Subtask 2 are provided below:

- **Validation File:** The validation data includes the following fields: `比喻句, 正确答案, 答案A_本体, 答案A_喻体, 答案A_共性, 答案B_本体, 答案B_喻体, 答案B_共性, 答案C_本体, 答案C_喻体, 答案C_共性, 答案D_本体, 答案D_喻体, 答案D_共性`.  
  [View the Validation File](./data/data/test/track2_validation.csv)

- **Test File:** The test data includes these fields: `比喻句, 答案A_本体, 答案A_喻体, 答案A_共性, 答案B_本体, 答案B_喻体, 答案B_共性, 答案C_本体, 答案C_喻体, 答案C_共性, 答案D_本体, 答案D_喻体, 答案D_共性`. You will need to determine the correct option among the four provided.  
  [View the Test File](./data/data/test/track2_test.csv)


### Evaluation
For each task we provide two tracks to evaluation:

- Track1 : LLM Track

We encourage the use of large models to directly generate the options. You may use your own prompt, but please use a common prompt during the answer phase: "The answer is {}."

- Track2: Rule based Track

You can also use traditional linguistic rules or machine learning-based methods to directly compare and derive conclusions for options A, B, C, and D.


For more information related to this dataset, please refer to our paper: [CMDAG: A Chinese Metaphor Dataset with Annotated Grounds as CoT for Boosting Metaphor Generation](https://arxiv.org/abs/2402.13145). If there are any differences between the paper and this page, the content of this page should prevail.

## Submission & Evaluation

For submission, the following materials should be packaged as one `zip` file, the final result must be a json file named with format `yourteamid_task{1or2}_track{1or2}.json` and sent to quxingwei25@gmail.com:

- Submission File: 
For the Large Language Model Track, we allow you to give us the prompt based generations like. we will extract first letter from `[A,B,C,D]` as shown: 
```
[
    {
        "metaphor_id": 0,
        "answer": "The answer is A",
    },
    {
        "metaphor_id": 1,
        "answer": "The answer is B",
    },
    ...
]

```
For the Rule based Track, The answer must be the only choice from `[A,B,C,D]` as shown: 
```
[
    {
        "metaphor_id": 0,
        "answer": "A",
    },
    {
        "metaphor_id": 1,
        "answer": "B",
    },
    ...
]

```
- Code: The code folder should contain all the codes of data augmentation, data processing, model training and model inference. 

## Evaluation

The top 3 participating teams in each task and track will be certificated by NLPCC and CCF-NLP.

## Benchmark Results

We provide benchmark results for the MAP-NEO and CT-LLM models on two subtasks. You can find the example [code & results file](./benchmark/) for these models in their respective repositories:

- [MAP-NEO](https://github.com/multimodal-art-projection/MAP-NEO)
- [CT-LLM](https://github.com/Chinese-Tiny-LLM/Chinese-Tiny-LLM)

### Results

| Model   | Subtask 1 | Subtask 2 |
|---------|-----------|-----------|
| MAP-NEO | 48.4      | 37.8      |
| CT-LLM  | 22.8      | 5.6       |

### Leaderboard

#### Subtask 1 Track 1
Final result：
<table>
  <tr> <th>排名 </th><th>队伍名</th><th>A榜</th><th>B榜</th><th>总分</th></tr>
  <tr> <th>1 </th> <td>kangreen</td><td>98.8</td><td>98.0</td><td>98.4</td></tr>
  <tr> <th>2 </th> <td>ShaunTheSheep</td><td>96.2</td><td>96</td><td>96.1</td></tr>
  <tr> <th>3 </th> <td>YNU-HPCC</td><td>96.6</td><td>95.2</td><td>95.9</td></tr>
</table>

#### Subtask 1 Track 2 
Final result：
<table>
  <tr> <th>排名 </th><th>队伍名</th><th>A榜</th><th>B榜</th><th>总分</th></tr>
  <tr> <th>1 </th> <td>YNU-HPCC</td><td>98.4</td><td>97.4</td><td>97.9</td></tr>
</table>

#### Subtask 2 Track 1
Final result：
<table>
  <tr> <th>排名 </th><th>队伍名</th><th>A榜</th><th>B榜</th><th>总分</th></tr>
  <tr> <th>1 </th> <td>YNU-HPCC</td><td>96.6</td><td>93.6</td><td>95.1</td></tr>
  <tr> <th>2 </th> <td>ZZU_NLP</td><td>93.8</td><td>91.82</td><td>92.8</td></tr>
  <tr> <th>3 </th> <td>ShaunTheSheep</td><td>92.2</td><td>92.81</td><td>92.5</td></tr>
  <tr> <th>4 </th> <td>kangreen</td><td>92.8</td><td>91.8</td><td>92.3</td></tr>
</table>

#### Subtask 2 Track 2 
Final result：
<table>
  <tr> <th>排名 </th><th>队伍名</th><th>A榜</th><th>B榜</th><th>总分</th></tr>
  <tr> <th>1 </th> <td>YNU-HPCC</td><td>95</td><td>93.2</td><td>94.1</td></tr>
</table>

## Contact & Citation

If your publication employs our dataset, please cite the following article:

```\
@article{Shao2024CMDAGAC,
  title={CMDAG: A Chinese Metaphor Dataset with Annotated Grounds as CoT for Boosting Metaphor Generation},
  author={Yujie Shao and Xinrong Yao and Xingwei Qu and Chenghua Lin and Shi Wang and Stephen W. Huang and Ge Zhang and Jie Fu},
  journal={ArXiv},
  year={2024},
  volume={abs/2402.13145},
  url={https://api.semanticscholar.org/CorpusID:267759689}
}
```

If you have any questions about this task, please email to quxingwei25@gmail.com.
