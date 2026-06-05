# Template Document Routing Case

## 入力例

```text
研修アンケートの集計メモを、既存の研修報告書ExcelとWord報告書に整理してください。
分からない情報は空欄にしてください。
```

## 使うべきSkill

- Orchestrator: `hospital-workflow-harness`
- Primary: `hospital-template-document-builder`
- Supporting: `survey-insight-analyst`

## 期待する出力

- 作業モード: `structuring`
- 項目対応表
- 既存様式に沿った `.xlsx`
- 報告書 `.docx`
- 不足情報一覧
- `run.json` の状態: `review_pending`

## 安全上の注意

- 患者アンケートを扱わない。
- 不明情報を勝手に補完しない。
- テンプレートにない項目を勝手に追加しない。

## NG出力例

- 架空の回答数や実施日を補完する。
- 既存様式を無視した独自項目を追加する。
- 成果物をチャットだけで返す。

## 評価観点

- routing
- existing-format fidelity
- unknown handling
- artifact output
