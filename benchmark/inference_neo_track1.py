from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm
import json
# model_path = '/ML-A100/team/mm/zhangge/models/neo_7b_instruct_v0.1'
model_path = '/ML-A100/team/mm/zhangge/models/CT-LLM-SFT-DPO'
data_path='/ML-A100/team/mm/zk/NLPCC-2024-Shared-Task-9/task_data/track1_test.jsonl'
save_path='./task1_track1.json'
tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False)

# Since transformers 4.35.0, the GPT-Q/AWQ model can be loaded using AutoModelForCausalLM.
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    torch_dtype='auto'
).eval()

score=0
cnt=0
result_dic_list=[]
with open(data_path) as jsonl_file:
    for idx,line in tqdm(enumerate(jsonl_file)):
        result_dic={}
        # cnt+=1
        # if cnt <=100:continue
        data=json.loads(line)
        text='本体:'+data['本体']+',喻体:'+data['喻体']+',共性:'+data['共性']
        A=data['选项A']
        B=data['选项B']
        C=data['选项C']
        D=data['选项D']
        # gt=data['正确选项'][-1]
        options=f'A:{A}\nB:{B}\nC:{C}\nD:{D}\n'
        # instruction1=f'给定本体、喻体与共性,请你基于本体和喻体之间的共性,写一个简短准确的含有关于本体和喻体的隐喻（metaphor）的中文句子。{text}'
        # instruction=f'请你基于本体和喻体之间的共性,从下面隐喻句子的选项中，选出最符合的句子,请直接回答对应选项(A,B,C,D)，不需要其他额外的回复\n{text}\n{options}'
        instruction=f'请你基于本体和喻体，及其之间的共性,从下面隐喻句子的选项中，选出最符合的句子,请直接回答对应选项，不需要其他额外的回复\n{text}\n{options}'
        # content='给定本体、喻体与共性,请你基于本体和喻体之间的共性,写一个简短准确的含有关于本体和喻体的隐喻（metaphor）的中文句子。本体:心,喻体:寒冰,共性:冰冷的内心'
        messages = [
            {"role": "user", "content": f"{instruction}"}
        ]
        input_ids = tokenizer.apply_chat_template(conversation=messages, tokenize=True, return_tensors='pt')
        output_ids = model.generate(input_ids.to('cuda'), max_new_tokens=256,eos_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True)
        result_dic={'metaphor_id':idx,
                    'answer':response
                    }
        result_dic_list.append(result_dic)

with open('./task1_track1_ctllm.json','w') as json_file:
    json_data=json.dumps(result_dic_list,indent=4, ensure_ascii=False)
    json_file.write(json_data)