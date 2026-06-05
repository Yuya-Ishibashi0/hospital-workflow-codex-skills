# サンプル Excel テンプレートを追加する

## 背景

`hospital-template-document-builder` や `survey-insight-analyst` は、既存 Excel 様式への整理と相性がよい。初期版では実ファイルのテンプレートは含めていないため、架空データのサンプルを追加したい。

## 対象

- `examples/`
- `skills/hospital-template-document-builder/assets/`
- `skills/survey-insight-analyst/assets/`
- 必要に応じて `docs/`

## 追加したい内容

- 研修報告書、出席簿、FAQ 一覧、業務改善提案書などのサンプル Excel テンプレート案を追加する。
- 初期段階では `.xlsx` ではなく Markdown / CSV 形式の設計案でもよい。
- 不明情報を勝手に補完しない転記ルールを明記する。

## 安全上の制約

- 実患者情報、実在職員名、実在病院名を含めない。
- 個別診療、算定判断、電子カルテ内容を扱う表を作らない。
- 提出前に人間確認が必要であることを明記する。

## 完了条件

- 少なくとも 3 種類の Excel テンプレート案が追加されている。
- `hospital-template-document-builder` から使い方が分かる。
- 空欄、不足情報、元資料との対応関係の扱いが明記されている。
