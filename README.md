## ELYZA-tasks100-AutoEval

gguf量子化したgemma-2-27b-itでELYZA-tasks100を自動評価します。

```ELYZA-tasks100-ansuwer_*.py```は評価対象のggufモデルにELYZA-tasks100（```test.csv```）を回答させます。```answer.csv```が生成されます。

```ELYZA-tasks100-judge_gemma-2.py```はgguf量子化したgemma-2-27b-itに```answer.csv```を採点させます。```judge.csv```が生成されます。

```ELYZA-tasks100-result.py```はELYZA-tasks100（```test.csv```）と```answer.csv```と```judge.csv```を結合します。```result.csv```が生成されます。

## gemma-2-27b-it-Q6_K-3436.gguf(llama.cpp_b3436)による自動評価(評価/被評価共にtemplreture=0.8)
※VRAM28GB環境で検証しています。

リンクの無いものはconvert_hf_to_gguf.pyで自前で量子化したもの。
|モデル名など|スコア|
|:---|---:|
|gemma-2-27b-it-Q6_K-3436.gguf|3.86|
|EZO-Humanities-9B-gemma-2-it-Q8_0-3436.gguf|3.83|
|[dahara1/gemma-2-27b-it.Q4_K_M.gguf](https://huggingface.co/dahara1/gemma-2-27b-it-gguf-japanese-imatrix)|3.82|
|Gemma-2-9B-It-SPPO-Iter3-Q8_0-3436.gguf|3.82|
|EZO-Common-9B-gemma-2-it-f16-3436.gguf|3.74|
|EZO-Common-9B-gemma-2-it-Q8_0-3436.gguf|3.73|f16と大差ない|
|EZO-Humanities-9B-gemma-2-it-f16-3436.gguf|3.68|何故かQ8_0より低スコア|
|[dahara1/gemma-2-9b-it.f16.Q8.gguf](https://huggingface.co/dahara1/gemma-2-9b-it-gguf-japanese-imatrix)|3.61|
|[YukiTomita-CC/ELYZA-tasks-100_Human_solved](https://huggingface.co/datasets/YukiTomita-CC/ELYZA-tasks-100_Human_solved)|3.58|
|[grapevine-AI/calm3-22b-chat-Q6_K.gguf](https://huggingface.co/grapevine-AI/CALM3-22B-Chat-GGUF)|3.53|
|Llama-3-ELYZA-JP-8B-Q8_0.gguf|3.38|
|Ninja-V3-Q8_0.gguf|3.27|
|mistral-yuki-7B-Q8_0.gguf|3.12|
|Oumuamua-7b-instruct-v2-Q8_0.gguf|3.11|
|Ninja-V2-7B-Q8_0.gguf|3.09|
|Ninja-v1-NSFW-Q_8_0.gguf|2.88|
|japanese-starling-chatv-7b.Q8_0.gguf|2.87|
|Japanese-Chat-Umievo-itr001-7b.Q8_0.gguf|2.83|
|chatntq-ja-7b-v1.0.Q8_0.gguf|2.55|
|ELYZA-japanese-Llama-2-13b-instruct-Q8_0.gguf|2.52|
|[ReadyON/karakuri-lm-8x7b-instruct-v0.1-IQ3_XS.gguf](https://huggingface.co/ReadyON/karakuri-lm-8x7b-instruct-v0.1-gguf)|2.44|
|[TheBloke/calm2-7b-chat.Q8_0.gguf](https://huggingface.co/TheBloke/calm2-7B-chat-GGUF)|2.15|
## 備考
採点テンプレートは[うみゆき氏の次の記事のもの](https://soysoftware.sakura.ne.jp/archives/3850)をお借りしました。

ライセンスは[ELYZA-task-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100)に依存します。

## 履歴
    [2024/07/15] - 初回リリース
    [2024/07/22] - answer.csvに使用モデルを、judge.csvに平均点を追記するよう対応
    [2024/07/22] - Qwen2に対応
    [2024/07/22] - 採点者をgemma-2-27b-it-Q6_K前提に変更