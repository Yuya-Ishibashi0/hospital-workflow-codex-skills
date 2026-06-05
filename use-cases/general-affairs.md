# General Affairs Use Cases

## 院内通知文作成

- 業務名: 職員向け通知
- よくある困りごと: 要点と依頼事項が埋もれる。
- 推奨Skill: `hospital-document-drafter`
- 補助Skill: `hospital-visual-material-designer`
- 入力例: 通知内容、対象、締切、問い合わせ先
- 出力例: 通知文、掲示版、短縮版
- 注意点: 院内規程を優先する。
- 対象外: 患者説明文

## 物品購入・稟議フロー整理

- 業務名: 稟議と購買依頼のフロー整理
- よくある困りごと: 必要書類と承認経路が分かりにくい。
- 推奨Skill: `admin-workflow-consultant`
- 補助Skill: `hospital-manual-builder`
- 入力例: 架空の申請手順、様式、承認者
- 出力例: 現状フロー、改善案、チェックリスト
- 注意点: 購買規程を優先する。
- 対象外: 契約や法務判断

## 職員アンケート分析

- 業務名: 職員向けアンケート整理
- よくある困りごと: 自由記述の分類に時間がかかる。
- 推奨Skill: `survey-insight-analyst`
- 補助Skill: `hospital-template-document-builder`
- 入力例: 匿名化した回答
- 出力例: 傾向、分類、改善要望、報告書ドラフト
- 注意点: 個人特定につながる情報を除く。
- 対象外: 人事評価、懲戒判断

## 採用・見学対応FAQ

- 業務名: 採用見学のFAQ整備
- よくある困りごと: 回答が担当者ごとに違う。
- 推奨Skill: `hospital-document-drafter`
- 補助Skill: `hospital-manual-builder`
- 入力例: よくある質問、公式回答、確認先
- 出力例: FAQ、確認が必要な項目、共有文
- 注意点: 人事規程と広報確認を優先する。
- 対象外: 個別採用判断

## 職員研修企画

- 業務名: 総務主催研修
- よくある困りごと: 構成とアンケートが決まらない。
- 推奨Skill: `training-program-designer`
- 補助Skill: `hospital-visual-material-designer`
- 入力例: テーマ、対象、時間、目的
- 出力例: 研修構成、進行台本、案内文案
- 注意点: 労務、法務、個人情報テーマは担当確認。
- 対象外: 個別労務判断

## 文書管理ルールの整理

- 業務名: 院内文書管理の手順化
- よくある困りごと: 保存場所や版管理が曖昧。
- 推奨Skill: `hospital-manual-builder`
- 補助Skill: `automation-planning-consultant`
- 入力例: 保存場所、命名規則、確認者
- 出力例: 手順書、チェックリスト、FAQ
- 注意点: 文書管理規程を優先する。
- 対象外: 法定保存期間の最終判断

## 総務依頼受付フロー改善

- 業務名: 総務への依頼受付整理
- よくある困りごと: メール、紙、口頭依頼が混在する。
- 推奨Skill: `automation-planning-consultant`
- 補助Skill: `admin-workflow-consultant`
- 入力例: 依頼種別、受付経路、件数
- 出力例: 改善手段、PoC案、相談文
- 注意点: 権限、個人情報、システム変更は確認。
- 対象外: 患者情報を含む依頼処理

