## ELYZA-tasks100-AutoEval

gguf量子化したgemma-2-27b-itでELYZA-tasks100を自動評価します。

```ELYZA-tasks100-ansuwer_*.py```は評価対象のggufモデルにELYZA-tasks100（```test.csv```）を回答させます。```answer.csv```が生成されます。

```ELYZA-tasks100-judge_gemma-2.py```はgguf量子化したgemma-2-27b-itに```answer.csv```を採点させます。```judge.csv```が生成されます。

```ELYZA-tasks100-result.py```はELYZA-tasks100（```test.csv```）と```answer.csv```と```judge.csv```を結合します。```result.csv```が生成されます。

## [YukiTomita-CC/gemma-2-27b-it-GGUF/](https://huggingface.co/YukiTomita-CC/gemma-2-27b-it-GGUF)gemma-2-27b-it-Q4_K_M.ggufによる自動評価サンプル

||モデル名など|1回の採点での平均|
|---|:---|---:|
|1|EZO-Common-9B-gemma-2-it-Q8_0.gguf|3.79|
|2|gemma-2-27b-it-Q4_K_M.gguf|3.75|
|3|gemma-2-9b-it-SPPO-Iter3-Q8_0.gguf|3.74|
|4|EZO-Humanities-9B-gemma-2-it-Q8_0.gguf|3.73|
|5|gemma-2-9b-it-Q8_0.gguf|3.63|
|6|YukiTomita-CC/ELYZA-tasks-100_Human_solved|3.53|
|7|mistral-yuki-7B-Q8_0.gguf|3.29|
|8|Llama3-ArrowSE-8B-v0.3-Q8_0.gguf|3.29|
|9|Umievo-itr012-Gleipnir-7B-Q8_0.gguf|3.12|
|10|ArrowPro-7B-KillerWhale.Q8_0.gguf|2.76|
|11|calm2-7b-chat.Q8_0.gguf|2.28|

## 備考
採点テンプレートは[うみゆき氏の次の記事のもの](https://soysoftware.sakura.ne.jp/archives/3850)をお借りしました。

ライセンスは[ELYZA-task-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100)に依存します。

## 履歴
    [2024/07/15] - 初回リリース
    [2024/07/22] - answer.csvに使用モデルを、judge.csvに平均点を追記するよう対応
    [2024/07/22] - Qwen2に対応
