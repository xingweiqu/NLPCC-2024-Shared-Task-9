from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm
import json
model_path = '/ML-A100/team/mm/zhangge/models/CT-LLM-SFT-DPO'
data_path='/ML-A100/team/mm/zk/NLPCC-2024-Shared-Task-9/task_data/track2_test.jsonl'
save_path='./task2_track1_ctllm.json'
tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False)

# Since transformers 4.35.0, the GPT-Q/AWQ model can be loaded using AutoModelForCausalLM.
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    torch_dtype='auto'
).eval()
# data_path='task_data/track2_val.jsonl'
result_dic_list=[]
with open(data_path) as jsonl_file:
    for idx,line in tqdm(enumerate(jsonl_file)):
        data=json.loads(line)
        text=data['比喻句']
        A=data['答案A_本体']+';'+data['答案A_喻体']+';'+data['答案A_共性']
        B=data['答案B_本体']+';'+data['答案B_喻体']+';'+data['答案B_共性']
        C=data['答案C_本体']+';'+data['答案C_喻体']+';'+data['答案C_共性']
        D=data['答案D_本体']+';'+data['答案D_喻体']+';'+data['答案D_共性']
        # gt=data['正确答案'][-1]
        options=f'A:{A}\nB:{B}\nC:{C}\nD:{D}\n'
        # instruction=f'给定一段比喻句,请你从下面的选项中，选出最符合的选项\n问题:\n{text}\n选项:\n{options}'
        # instruction=f'请你理解下面比喻句中的内容:{text},从下面的选项中，选出最符合的本体、喻体和共性\n{options}'
        # instruction=f'给定一段含有关于本体和喻体的隐喻（metaphor）的中文句子:{text},请你找出其中的本体、喻体,以及本体和喻体之间的共性,并从下面的选项中，选出最符合选项\n{options}'
        # instruction=f'给定一段含有关于本体和喻体的隐喻（metaphor）的中文句子,请你找出其中的本体、喻体,并推测本体和喻体之间的共性,从下面本体、喻体以及本体和喻体之间的共性的选项中,选择最符合的选项\n{text}\n{options}'
        # instruction=f'给定一段比喻句,请你找出其中的本体、喻体,以及共性,并从下面的选项中，选出最符合选项\n{text}\n{options}'
        instruction=f'给定一段含有关于本体和喻体的隐喻（metaphor）的中文句子,请你找出其中的本体、喻体,以及共性\n{text}\n{options}'#v1
        
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

with open(save_path,'w') as json_file:
    json_data=json.dumps(result_dic_list,indent=4, ensure_ascii=False)
    json_file.write(json_data)