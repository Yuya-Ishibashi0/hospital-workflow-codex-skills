# Common Use Cases

## 二重入力・転記削減

- 業務名: 研修、委員会、物品管理などの二重入力整理
- よくある困りごと: 紙、Excel、報告書に同じ情報を転記している。
- 推奨Skill: `admin-workflow-consultant`
- 補助Skill: `automation-planning-consultant`, `hospital-template-document-builder`
- 入力例: 架空の転記元、転記先、頻度、担当者
- 出力例: 現状フロー、無駄、改善案、小さく試す案
- 注意点: 個人情報を含む名簿は匿名化する。
- 対象外: 患者情報、電子カルテ連携

## 会議メモ整理

- 業務名: 委員会や部署会議のアクション整理
- よくある困りごと: 決定事項、担当、期限が曖昧になる。
- 推奨Skill: `meeting-action-organizer`
- 補助Skill: `hospital-document-drafter`
- 入力例: 架空の会議メモ
- 出力例: 決定事項、未決事項、担当者、共有文
- 注意点: 患者個別カンファレンスは扱わない。
- 対象外: 診療方針、申し送り

## 院内お知らせ作成

- 業務名: 職員向け通知文作成
- よくある困りごと: 文面が長く、依頼事項が伝わりにくい。
- 推奨Skill: `hospital-document-drafter`
- 補助Skill: `hospital-visual-material-designer`
- 入力例: 周知内容、対象者、締切、問い合わせ先
- 出力例: 件名、本文、掲示版、短縮版
- 注意点: 院内規程と責任部署の確認を優先する。
- 対象外: 患者説明文

## 研修アンケート分析

- 業務名: 研修後アンケートの集計と示唆
- よくある困りごと: 自由記述を報告書にまとめにくい。
- 推奨Skill: `survey-insight-analyst`
- 補助Skill: `hospital-template-document-builder`
- 入力例: 匿名化した満足度と自由記述
- 出力例: 全体傾向、分類、改善要望、次回テーマ
- 注意点: 個人が特定される記述は除外する。
- 対象外: 患者アンケートの個別対応判断

## 既存様式への情報整理

- 業務名: Excel / Word / PowerPoint 様式への転記
- よくある困りごと: どの情報をどの項目に入れるか迷う。
- 推奨Skill: `hospital-template-document-builder`
- 補助Skill: `hospital-document-drafter`
- 入力例: テンプレート項目と元メモ
- 出力例: 対応表、不足情報、転記ルール
- 注意点: 不明情報を勝手に補完しない。
- 対象外: 診療記録、申し送り

## 業務マニュアル作成

- 業務名: 部署内手順書の作成・改訂
- よくある困りごと: 口頭ルールが多く、新人が迷う。
- 推奨Skill: `hospital-manual-builder`
- 補助Skill: `admin-workflow-consultant`
- 入力例: 現在の手順、注意点、よくあるミス
- 出力例: 手順、FAQ、チェックリスト、改訂履歴案
- 注意点: 院内規程と責任者確認を優先する。
- 対象外: 診療手順

## 自動化・省力化検討

- 業務名: 定型事務の自動化候補整理
- よくある困りごと: Excel 関数、フォーム、共有フォルダ運用、既存システム設定変更など、どこから改善すべきか判断できない。
- 推奨Skill: `automation-planning-consultant`
- 補助Skill: `admin-workflow-consultant`
- 入力例: 作業頻度、件数、使用ツール、例外の多さ
- 出力例: 選択肢、難易度、リスク、小さく試す案、相談文
- 注意点: システム変更は担当者へ確認する。
- 対象外: 医療安全に直接影響する自動処理
