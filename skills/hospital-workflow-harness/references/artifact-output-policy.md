# Artifact Output Policy

Codex がこのハーネスで Skill を使うときは、成果物をチャット本文ではなくファイルとして作成します。

## 基本ルール

- チャット欄に成果物全文を貼らない。
- 依頼された成果物は、原則として `.docx`、`.xlsx`、`.pptx`、`.md`、`.csv` のいずれかで保存する。
- ユーザーが形式を指定した場合は、その形式を優先する。
- 形式指定がない場合は、この文書の標準形式に従う。
- 作成後のチャット返信は、保存先、ファイル名、内容の短い要約、人間が確認すべき点だけにする。

## 標準保存先

生成した作業成果物は、ユーザーが別の場所を指定しない限り `outputs/` に保存します。

```text
outputs/
  YYYYMMDD-task-name/
    document.docx
    table.xlsx
    slides.pptx
    notes.md
```

公開リポジトリに実務データを混ぜないため、`outputs/` 配下の生成物は既定では Git 管理しません。

## Skill 別の標準成果物

| Skill | 標準成果物 |
| --- | --- |
| `admin-workflow-consultant` | 業務整理レポート `.docx`、必要に応じて業務フロー表 `.xlsx` |
| `automation-planning-consultant` | 省力化検討メモ `.docx`、比較表 `.xlsx` |
| `hospital-document-drafter` | 院内文書 `.docx` |
| `hospital-template-document-builder` | 対応表 `.xlsx`、報告書 `.docx`、資料構成 `.pptx` |
| `hospital-manual-builder` | マニュアル `.docx`、チェックリスト `.xlsx` |
| `hospital-visual-material-designer` | スライド `.pptx`、掲示物原稿 `.docx` |
| `survey-insight-analyst` | 集計表 `.xlsx`、報告書 `.docx` |
| `meeting-action-organizer` | 議事録 `.docx`、アクション一覧 `.xlsx` |
| `training-program-designer` | 研修企画書 `.docx`、研修スライド `.pptx`、アンケート案 `.docx` |

## チャット返信の型

```text
作成しました。

- 保存先: outputs/YYYYMMDD-task-name/
- 作成ファイル:
  - manual.docx
  - checklist.xlsx
- 確認ポイント:
  - 院内規程との整合
  - 担当者名、期限、提出先
  - 患者情報や個人情報が含まれていないこと
```

## 例外

以下の場合のみ、チャット本文で短い下書きを返してもよいです。

- ユーザーが明示的に「チャットで見せて」と依頼した場合
- 1画面に収まる短い文面だけを確認したい場合
- ファイル作成前の方針確認や目次案の確認段階

それ以外は、ファイル作成を優先します。
