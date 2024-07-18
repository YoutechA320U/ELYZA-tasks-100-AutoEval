from llama_cpp import Llama #llama.cppのPythonライブラリであるllama-cpp-python

model="hoge_huga.gguf" #評価対象のモデルのパスを入力。
llm = Llama(
      model_path=model,
      n_gpu_layers=-1, # #GPUにロードするレイヤー数（llama-cpp-pythonがcuda版の場合）
      n_ctx=2048, # 最大コンテキストサイズ。入力の上限。
      #last_n_tokens_size =0, # Maximum number of tokens to keep in the last_n_tokens deque.
)

role = "<|START_OF_TURN_TOKEN|><|SYTEM_TOKEN|>\n\
あなたは誠実で優秀なアシスタントです。<|END_OF_TURN_TOKEN|>"
role += "\n"

import csv
csv_path="test.csv"
answer_csv_path="answer.csv"
with open(answer_csv_path, mode='w',newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['answer'])
# CSVファイルを開く
with open(csv_path, mode='r', encoding='utf-8',newline="") as file:
    reader = csv.reader(file)
    #print(reader)
    # 各行を読み込む
    for row in reader:
     if row[0]!="input":
        #print(row[0])
        prompt=row[0]
        prompt_K = (role+"<|START_OF_TURN_TOKEN|><|USER_TOKEN|>\n"+prompt+"<|END_OF_TURN_TOKEN|>\n<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>\n")
        output = llm(
            prompt=prompt_K, 
            max_tokens=1024,
            temperature = 0.8,
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
            stop=["<|"] # ストップ。特定の文字を生成したらその文字を生成せず停止する。
        )
        output= output["choices"][0]["text"]
        output =output.replace("\\n", "\n").replace("\\u3000", "\u3000").replace("!","！").replace("?","？")
        while output[-1]=="\n":
              output=output[:-1]
        while output[0]=="\n":
              output=output[1:] 
        print( prompt_K+output+"<|END_OF_TURN_TOKEN|>")
        with open(answer_csv_path, mode='a', encoding='utf-8',newline="") as f:
            writer = csv.writer(f)
            writer.writerow([output])
