# 部門別 use-case をさらに 20 件追加する

## 背景

初期版では主要部門の use-case を整理しているが、実際の院内業務は部署や委員会ごとに細かい。新しい Skill を増やす前に、既存 Skill にマッピングできる use-case を増やしたい。

## 対象

- `use-cases/common.md`
- `use-cases/nursing.md`
- `use-cases/rehabilitation.md`
- `use-cases/medical-office.md`
- `use-cases/general-affairs.md`
- `use-cases/medical-staff-office.md`
- `use-cases/education.md`
- `use-cases/regional-cooperation.md`

## 追加したい内容

- 合計 20 件以上の use-case を追加する。
- 各 use-case に、業務名、よくある困りごと、推奨 Skill、補助 Skill、入力例、出力例、注意点、対象外を含める。
- 既存 9 Skill のどれに対応するかを明確にする。

## 安全上の制約

- 患者個人情報を前提にしない。
- レセプト、未収金、地域連携などでは、法的判断・算定判断・医療判断に踏み込まない。
- 個別症例や患者説明に関わる use-case は追加しない。

## 完了条件

- 20 件以上の新規 use-case が追加されている。
- 各 use-case に推奨 Skill が明記されている。
- 新しい Skill を増やさず、既存 Skill へのマッピングを優先している。

