# CHANGELOG

## 0.2.0 - Unreleased

- リポジトリの位置づけを、Codex Skills 集から Codex 向け軽量エージェントハーネスへ再整理しました。
- `harness/` を Codex の実行制御レイヤーとして定義し、operating model、task routing、safety boundaries、output contracts、human review policy、workflow modes を追加しました。
- 成果物の再現性を高めるため、`templates/` に業務ヒアリング、業務フロー、既存様式整理、アンケート整理、提案書、議事録、部門別マニュアル、運用設計のテンプレートを追加しました。
- 保守用スクリプトを `tools/` に分離しました。
- 将来の評価ケースとルーブリックを `evals/` に分離しました。
- README を日本語利用者向けに再構成し、ロゴ、English README へのリンク、スクリーンショット掲載方針を追加しました。
- Skill の成果物をチャット本文ではなく `.docx`、`.xlsx`、`.pptx`、`.md`、`.csv` のファイルとして作成する方針を追加しました。
- Codex plugin manifest、`$hospital-workflow-harness` オーケストレーター、harness doctor、タスク初期化、ユーザー環境導入ツールを追加しました。

## 0.1.0

- 初期 9 Skills を追加しました。
- 部門別 use-cases を追加しました。
- safety guidelines を追加しました。
- installation guide を追加しました。
- basic harness structure を追加しました。
- GitHub issue templates を追加しました。
