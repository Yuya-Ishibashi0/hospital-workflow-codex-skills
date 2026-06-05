# ユースケース

このディレクトリは、Hospital Workflow Codex Skillsを実務でどう使い始めるかを説明します。

## 読み方

内容を二つに分けています。

| ディレクトリ | 内容 |
| --- | --- |
| [`scenarios/`](scenarios/) | 実際の作業を、最初の依頼から成果物の確認まで順番に説明 |
| [`departments/`](departments/) | 看護部、医事課、総務課など、部門ごとに利用候補を一覧化 |

初めて使う場合は、先に代表シナリオを確認してください。Skill名を選ぶ必要はありません。やりたいことを日本語で伝えると、Codexが必要な資料を確認し、足りない情報を質問してから作業を進めます。

## 代表シナリオ

### 文書や資料を作る

- [口頭で引き継いでいる業務をマニュアルにする](scenarios/department-manual.md)
- [院内向けのお知らせ・依頼文・報告書を作る](scenarios/internal-document.md)
- [問い合わせ内容から職員向けFAQを作る](scenarios/staff-faq.md)
- [研修資料と当日の進行資料を作る](scenarios/training-materials.md)

### 手元の情報を整理する

- [対面会議の記録から議事録と担当表を作る](scenarios/meeting-to-actions.md)
- [研修アンケートから集計表と報告書を作る](scenarios/training-survey-analysis.md)
- [メモや集計結果を既存の院内様式へ整理する](scenarios/template-document-organization.md)

### 業務を見直す

- [職員への依頼がメール・紙・口頭に分散している状態を整理する](scenarios/workflow-intake-improvement.md)
- [費用をかけず、今の業務に無理なく取り入れられる改善・自動化を考える](scenarios/practical-automation.md)

## Codexへの資料の渡し方

次のいずれかで渡せます。

1. Codexのチャットへファイルを添付する。
2. このリポジトリ内に作業用フォルダを作り、ファイルをコピーして保存場所を伝える。
3. ファイルがない場合は「資料はありません。質問しながら作ってください」と伝える。

患者情報、電子カルテの内容、診療記録、申し送り、個人が特定できる情報は渡さないでください。Codexは資料の不足や利用できない形式を確認し、必要に応じて別形式の用意やヒアリングを案内します。

## 部門別一覧

- [共通部門](departments/common.md)
- [看護部](departments/nursing.md)
- [リハビリテーション部](departments/rehabilitation.md)
- [医事課](departments/medical-office.md)
- [総務課](departments/general-affairs.md)
- [医局・医局事務](departments/medical-staff-office.md)
- [教育研修担当](departments/education.md)
- [地域連携室](departments/regional-cooperation.md)
