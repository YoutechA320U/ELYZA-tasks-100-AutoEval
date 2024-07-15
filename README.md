## ELYZA-tasks100-AutoEval

gguf量子化したgemma-2-27b-itでELYZA-tasks100を自動評価します。

```ELYZA-tasks100-ansuwer_*.py```は評価対象のggufモデルにELYZA-tasks100（```test.csv```）を回答させます。```answer.csv```が生成されます。

```ELYZA-tasks100-judge_gemma-2.py```はgguf量子化したgemma-2-27b-itに```answer.csv```を採点させます。```judge.csv```が生成されます。

```ELYZA-tasks100-result.py```はELYZA-tasks100（```test.csv```）と```answer.csv```と```judge.csv```を結合します。```result.csv```が生成されます。

## gemma-2-27b-it-Q4_K_M.ggufによる自動評価例

|モデル名など|1回の採点での平均|
|:---|---:|
|ArrowPro-7B-KillerWhale.Q8_0.gguf|2.76|
|Umievo-itr012-Gleipnir-7B-Q8_0.gguf|3.12|
|Llama3-ArrowSE-8B-v0.3-Q8_0.gguf|3.29|
|gemma-2-27b-it-Q4_K_M.gguf|3.75|
|EZO-Common-9B-gemma-2-it-Q8_0.gguf|3.79|
|ELYZA-tasks-100_Human_solved|3.53|

## 備考
採点テンプレートは[うみゆき氏の次の記事のもの](https://soysoftware.sakura.ne.jp/archives/3850)をお借りしました。
ライセンスは[ELYZA-task100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100)に依存します。

## 履歴
    [2024/07/15] - 初回リリース
