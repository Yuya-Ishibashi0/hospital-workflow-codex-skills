# Medical Staff Office Use Cases

## 医局会議アジェンダ作成

- 業務名: 医局会議準備
- よくある困りごと: 議題、担当、資料が整理されない。
- 推奨Skill: `meeting-action-organizer`
- 補助Skill: `hospital-document-drafter`
- 入力例: 架空の議題メモ
- 出力例: アジェンダ、確認事項、共有文
- 注意点: 診療方針や患者情報は含めない。
- 対象外: 診療判断

## 医局内お知らせ文作成

- 業務名: 医師向け周知文
- よくある困りごと: 要点と依頼事項が伝わりにくい。
- 推奨Skill: `hospital-document-drafter`
- 補助Skill: `hospital-visual-material-designer`
- 入力例: お知らせ内容、締切、連絡先
- 出力例: 件名、本文、短縮版
- 注意点: 院内ルールを優先する。
- 対象外: 患者説明文、診療記録

## 研究会・勉強会の企画書

- 業務名: 院内勉強会企画
- よくある困りごと: 目的、対象、時間配分が曖昧。
- 推奨Skill: `training-program-designer`
- 補助Skill: `hospital-template-document-builder`
- 入力例: テーマ、対象、時間、到達目標
- 出力例: 企画書構成、進行案、アンケート
- 注意点: 研究内容や医療判断には踏み込まない。
- 対象外: 研究倫理判断、臨床判断

## 研修医オリエン資料構成案

- 業務名: 研修医向け非診療オリエン
- よくある困りごと: 院内ルールや提出物の説明が散らばる。
- 推奨Skill: `hospital-visual-material-designer`
- 補助Skill: `training-program-designer`
- 入力例: 説明項目、時間、配布資料
- 出力例: スライド構成、配布資料案、FAQ
- 注意点: 臨床指導内容は責任者確認。
- 対象外: 患者個別対応

## 医局内FAQ整備

- 業務名: 医局事務FAQ
- よくある困りごと: 学会申請、書類提出などの質問が重複する。
- 推奨Skill: `hospital-document-drafter`
- 補助Skill: `hospital-manual-builder`
- 入力例: よくある質問、回答、確認先
- 出力例: FAQ一覧、確認が必要な項目
- 注意点: 院内規程と担当部署確認を優先する。
- 対象外: 医療判断

## 学会準備タスク整理

- 業務名: 学会発表前の事務タスク整理
- よくある困りごと: 締切、提出物、担当が分かりにくい。
- 推奨Skill: `meeting-action-organizer`
- 補助Skill: `hospital-template-document-builder`
- 入力例: 架空の提出物、締切、担当
- 出力例: タスク一覧、期限、確認事項
- 注意点: 研究内容や医療判断には踏み込まない。
- 対象外: 研究データ解析、倫理判断
