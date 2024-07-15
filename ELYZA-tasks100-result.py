import pandas as pd
csv_path="test.csv"
answer_csv_path="answer.csv"
judge_csv_path="judge.csv"
#ファイルの読み込み
df1 = pd.read_csv(csv_path)
df2 = pd.read_csv(answer_csv_path)
df3 = pd.read_csv(judge_csv_path)
df_concat = pd.concat([df1,df2,df3],axis=1)
result_csv_path="result.csv"
df_concat.to_csv(result_csv_path,index=None)