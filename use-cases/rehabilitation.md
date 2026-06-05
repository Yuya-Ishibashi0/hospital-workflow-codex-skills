# Rehabilitation Use Cases

## リハビリ部門の書類業務棚卸し

- 業務名: 非診療書類の棚卸し
- よくある困りごと: 同じ情報を複数台帳に入れている。
- 推奨Skill: `admin-workflow-consultant`
- 補助Skill: `automation-planning-consultant`
- 入力例: 架空の台帳、頻度、担当
- 出力例: 現状フロー、無駄、改善案
- 注意点: 診療記録は対象外にする。
- 対象外: 患者別リハビリ計画

## 実績集計業務の整理

- 業務名: 部門実績の月次集計
- よくある困りごと: CSV と Excel の整形に時間がかかる。
- 推奨Skill: `hospital-template-document-builder`
- 補助Skill: `automation-planning-consultant`
- 入力例: 匿名化した集計項目、既存様式
- 出力例: 対応表、転記ルール、不足情報
- 注意点: 個人別データは使わない。
- 対象外: 算定や臨床評価の判断

## 部門内勉強会の企画

- 業務名: 勉強会構成案
- よくある困りごと: 時間配分と演習が決まらない。
- 推奨Skill: `training-program-designer`
- 補助Skill: `hospital-visual-material-designer`
- 入力例: テーマ、対象職員、時間
- 出力例: 60分構成、配布資料案、アンケート
- 注意点: 患者事例を扱う場合は匿名化と院内確認が必要。
- 対象外: 患者個別判断

## 新人・学生教育計画

- 業務名: 新人・学生向けオリエン
- よくある困りごと: 何をいつ教えるか整理できない。
- 推奨Skill: `training-program-designer`
- 補助Skill: `hospital-manual-builder`
- 入力例: 期間、到達目標、説明したいルール
- 出力例: 研修計画、チェックリスト、事後フォロー
- 注意点: 学校、院内規程を優先する。
- 対象外: 個別患者対応手順

## 多職種連携会議の準備チェックリスト

- 業務名: 会議前準備の標準化
- よくある困りごと: 資料準備の抜け漏れがある。
- 推奨Skill: `hospital-manual-builder`
- 補助Skill: `meeting-action-organizer`
- 入力例: 架空の会議準備項目
- 出力例: チェックリスト、FAQ、担当表
- 注意点: 患者情報を含む資料名は匿名化する。
- 対象外: 患者別カンファレンス内容

## 部門内マニュアル作成

- 業務名: 部門ルール集の作成
- よくある困りごと: 口頭ルールが多い。
- 推奨Skill: `hospital-manual-builder`
- 補助Skill: `admin-workflow-consultant`
- 入力例: 現在のルール、よくあるミス
- 出力例: 手順、FAQ、チェックリスト
- 注意点: 院内規程を優先する。
- 対象外: 診療手順

## 既存Excel様式への情報整理

- 業務名: 部門内集計表の整備
- よくある困りごと: 項目の対応が分からない。
- 推奨Skill: `hospital-template-document-builder`
- 補助Skill: `survey-insight-analyst`
- 入力例: 元メモと既存Excel項目
- 出力例: 対応表、不足情報、転記ルール
- 注意点: 空欄を勝手に埋めない。
- 対象外: 患者別診療情報

