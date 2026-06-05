# Evals

`evals/` は、将来的に Codex の出力を評価するためのケース、ルーブリック、回帰テストを置く場所です。

`harness/` と `evals/` は役割が異なります。

- `harness/`: Codex をどう動かすかを定義する制御層
- `evals/`: Codex の出力をどう評価するかを扱う場所
- `tools/`: リポジトリ保守用スクリプト

初期版では、既存の手動評価ケースとルーブリックをここに置いています。

## Harness evals

`evals/cases/hospital-workflow-harness/` では、個別 Skill の文章品質ではなく、次を確認します。

- 対象外依頼を安全に止めるか
- 適切な主 Skill と作業モードを選ぶか
- チャット長文ではなく成果物ファイルを作るか
- Office ファイルを機械検証するか
- 人間確認前に `completed` にしないか

`harness-behavior-rubric.md` を使って手動評価します。
