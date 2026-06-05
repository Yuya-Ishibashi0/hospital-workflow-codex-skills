# 医事課のユースケース一覧

## 受付・窓口業務改善

- 業務名: 受付フロー棚卸し
- よくある困りごと: 案内、書類確認、部署連絡が重複する。
- 推奨Skill: `admin-workflow-consultant`
- 補助Skill: `hospital-manual-builder`
- 入力例: 架空の受付手順、使用様式、担当
- 出力例: 現状フロー、改善案、FAQ
- 注意点: 患者個別情報を含めない。
- 対象外: 診療判断、患者説明

## 問い合わせFAQ作成

- 業務名: 職員向け問い合わせFAQ
- よくある困りごと: 同じ質問に何度も回答している。
- 推奨Skill: `hospital-document-drafter`
- 補助Skill: `hospital-manual-builder`
- 入力例: よくある質問、回答方針、確認先
- 出力例: FAQ、注意事項、確認が必要な質問
- 注意点: 患者向け医療説明にはしない。
- 対象外: 患者個別回答

## 月次業務チェックリスト

- 業務名: 月末月初作業の整理
- よくある困りごと: 抜け漏れや担当の曖昧さがある。
- 推奨Skill: `hospital-manual-builder`
- 補助Skill: `meeting-action-organizer`
- 入力例: 作業一覧、期限、担当
- 出力例: チェックリスト、担当表、確認項目
- 注意点: 院内ルールを優先する。
- 対象外: 算定判断

## 書類受付フローの棚卸し

- 業務名: 書類受付から回付までの整理
- よくある困りごと: 紙台帳とExcelの二重管理がある。
- 推奨Skill: `admin-workflow-consultant`
- 補助Skill: `hospital-template-document-builder`
- 入力例: 書類種別、台帳項目、回付先
- 出力例: 無駄の発生ポイント、改善案、転記ルール
- 注意点: 個別患者名は入れない。
- 対象外: 診療情報の判断

## 未収金対応フローの整理

- 業務名: 未収金事務フロー整理
- よくある困りごと: 連絡、記録、確認の手順が統一されていない。
- 推奨Skill: `hospital-manual-builder`
- 補助Skill: `admin-workflow-consultant`
- 入力例: 架空の事務手順、確認先
- 出力例: 手順書、注意事項、管理者確認点
- 注意点: 法的判断はしない。
- 対象外: 個別事案の法的助言

## レセプト業務スケジュール整理

- 業務名: 月次スケジュールと担当整理
- よくある困りごと: 締切と確認者が分かりにくい。
- 推奨Skill: `meeting-action-organizer`
- 補助Skill: `hospital-template-document-builder`
- 入力例: 架空の工程、締切、担当
- 出力例: スケジュール表、担当表、確認事項
- 注意点: 算定判断はしない。
- 対象外: 個別請求判断、診療内容判断
