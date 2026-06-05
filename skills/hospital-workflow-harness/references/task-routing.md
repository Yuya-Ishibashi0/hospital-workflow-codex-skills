# Task Routing

依頼内容を見たら、最初に元資料と希望成果物を確認し、その後に以下の表で作業種別を決めます。必要な資料がなければ、ヒアリングまたは入力用ファイルの作成から開始します。

| 依頼種別 | 主な Skill | 使う template | 標準成果物 |
| --- | --- | --- | --- |
| 二重入力、転記、紙運用、Excel 管理の整理 | `admin-workflow-consultant` | `workflow-map.md`, `workflow-hearing-sheet.md` | `.docx` + 必要に応じて `.xlsx` |
| 既存 Excel / Word / PowerPoint / 院内様式への整理 | `hospital-template-document-builder` | `template-document-mapping.md` | `.xlsx` / `.docx` / `.pptx` |
| 会議メモ、TODO、論点整理 | `meeting-action-organizer` | `meeting-minutes.md` | `.docx` + TODO 表 `.xlsx` |
| 部門別マニュアル、手順書 | `hospital-manual-builder` | `department-manual.md` | `.docx` + 必要に応じてチェックリスト `.xlsx` |
| 院内文書、依頼文、報告文、FAQ | `hospital-document-drafter` | `proposal-outline.md` | `.docx` |
| 研修アンケート、職員アンケートの整理 | `survey-insight-analyst` | `survey-summary-report.md` | 集計 `.xlsx` + 報告 `.docx` |
| 研修、勉強会、AI リテラシー研修 | `training-program-designer` | `operation-design.md` | 企画 `.docx` + 資料 `.pptx` |
| 掲示物、研修資料、スライド、図解案 | `hospital-visual-material-designer` | `operation-design.md` | `.pptx` または `.docx` |
| 費用を抑え、現在の業務に無理なく取り入れられる改善・自動化の検討 | `automation-planning-consultant` | `workflow-map.md`, `proposal-outline.md` | `.docx` + 比較表 `.xlsx` |

## 補助 Skill の扱い

既存の補助 Skill が使える場合は、主 Skill の出力を補強するために使います。

補助 Skill は原則二つまでとし、主 Skill だけで完結する場合は追加しません。

- 文書化: `hospital-document-drafter`
- 既存様式への整理: `hospital-template-document-builder`
- アンケート分析: `survey-insight-analyst`
- 研修資料: `training-program-designer`, `hospital-visual-material-designer`

## 迷った場合

依頼が曖昧な場合は、すぐに成果物を作らず、以下を確認します。

- 対象部門
- 現在の業務フロー
- 入力資料や既存様式
- 資料を添付できるか、作業用フォルダへコピーできるか
- 例外処理
- 関係者
- 現場で困っている点
- 使えるシステムや制約
- 個人情報や患者情報が含まれていないか
