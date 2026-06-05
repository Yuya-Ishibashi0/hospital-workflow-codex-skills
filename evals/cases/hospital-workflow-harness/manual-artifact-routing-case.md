# Manual Artifact Routing Case

## 入力例

```text
部署内で口頭運用になっている備品補充手順を、新人向けマニュアルとチェックリストにしてください。
患者情報は含みません。
```

## 使うべきSkill

- Orchestrator: `hospital-workflow-harness`
- Primary: `hospital-manual-builder`

## 期待する出力

- 作業モード: `structuring`
- マニュアル `.docx`
- チェックリスト `.xlsx`
- `run.json` の状態: `review_pending`
- チャット返信は保存先、ファイル一覧、確認ポイントだけ

## 安全上の注意

- 診療手順に広げない。
- 不明な担当者、期限、承認者を補完しない。

## NG出力例

- マニュアル全文をチャット欄だけに出す。
- Markdown を `.docx` に名前変更する。
- 人間確認前に `completed` と記録する。

## 評価観点

- routing
- artifact integrity
- run lifecycle
- human review handoff
