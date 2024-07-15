from llama_cpp import Llama #llama.cppのPythonライブラリであるllama-cpp-python
import gradio as gr #Gradio AIの試作で広く使われているブラウザGUIライブラリ
model="gemma-2-27b-it-Q4_K_M.gguf" #対象のモデルのパスを入力。
llm = Llama(
      model_path=model,
      n_gpu_layers=-1, # #GPUにロードするレイヤー数（llama-cpp-pythonがcuda版の場合）
      n_ctx=4096, # 最大コンテキストサイズ。入力の上限。
)

prompt = "問題, 正解例, 採点基準, 言語モデルが生成した回答が与えられます。\n\
\n\
# 指示\n\
「採点基準」と「正解例」を参考にして、、回答を1,2,3,4,5の5段階で採点し、数字のみを出力してください。\n\
\n\
# 問題\n\
{input_text}\n\
\n\
# 正解例\n\
{output_text}\n\
\n\
# 採点基準\n\
基本的な採点基準\n\
- 1点: 誤っている、 指示に従えていない\n\
- 2点: 誤っているが、方向性は合っている\n\
- 3点: 部分的に誤っている、 部分的に合っている\n\
- 4点: 合っている\n\
- 5点: 役に立つ\n\
\n\
基本的な減点項目\n\
- 不自然な日本語: -1点\n\
- 部分的に事実と異なる内容を述べている: -1点\n\
- 「倫理的に答えられません」のように過度に安全性を気にしてしまっている: 2点にする\n\
\n\
問題固有の採点基準\n\
{eval_aspect}\n\
\n\
# 言語モデルの回答\n\
{pred}\n\
\n\
# ここまでが'言語モデルの回答'です。回答が空白だった場合、1点にしてください。\n\
\n\
# 指示\n\
「採点基準」と「正解例」を参考にして、回答を1,2,3,4,5の5段階で採点し、数字のみを出力してください。"
prompt += "\n"

import csv
csv_path="test.csv"
answer_csv_path="answer.csv"
judge_csv_path="judge.csv"
with open(judge_csv_path, mode='w',newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['judge'])
with open(csv_path, mode='r', encoding='utf-8',newline="") as file1,open(answer_csv_path, mode='r', encoding='utf-8',newline="") as file2:
    reader1 = csv.reader(file1)
    reader2 = csv.reader(file2)
    # 各行を読み込む
    for row1, row2 in  zip(reader1, reader2):
     if row1[0]!="input":
        prompt1=prompt.replace("{input_text}",row1[0]).replace("{output_text}",row1[1]).replace("{eval_aspect}",row1[2])
     if row2[0]!="answer":
        prompt2=prompt1.replace("{pred}",row2[0])
        prompt_G2 = ("<start_of_turn>user\n"+prompt2+"<end_of_turn>\n<start_of_turn>model\n")
        output = llm(
               prompt=prompt_G2,
               max_tokens=1024,
               temperature = 0.7,
               top_p=0.95, 
               min_p=0.05,
               typical_p=1.0,
               frequency_penalty=0.0,
               presence_penalty=0.0,
               repeat_penalty=1.1,
               top_k=40, 
               seed=-1,
               tfs_z=1.0,
               mirostat_mode=0,
               mirostat_tau=5.0,
               mirostat_eta=0.1,
               stop=["<start_of_turn>model","<end_of_turn>","<start_of_turn>user","prompt_tokens"] # ストップ。特定の文字を生成したらその文字を生成せず停止する。
        )
        output =str(output)
        output= output.split("', ")
        output =output[3]
        output =output.replace("'choices': [{'text': '", "").replace("\\n", "\n").replace("\\n", "\n").replace("\\u3000", "\u3000")\
         .replace("!","！").replace("?","？")
        while output[-1]=="\n":
              output=output[:-1]
        while output[0]=="\n":
              output=output[1:] 
        print(prompt_G2+"\n採点:"+output+"点\n")
        with open(judge_csv_path, mode='a', encoding='utf-8',newline="") as f:
            writer = csv.writer(f)
            writer.writerow([output])