# Hospital Workflow Codex Skills

Codex Skills for non-clinical workflows in Japanese hospitals.

日本の病院における非診療領域の事務・運用・教育・文書作成・業務改善を支援する Codex Skills ライブラリです。看護部、リハビリテーション部、医局、医事課、総務課、教育研修担当、地域連携室などの部門で、患者個別の医療判断に関わらない業務を扱います。

## What this is

- Codex Skills として使える OSS プロジェクトです。
- Skill はすべて `.agents/skills/` に配置しています。
- 各 Skill は `SKILL.md`、`references/`、`examples/`、`assets/` を持ちます。
- 日本の病院業務に合わせたユースケースを `use-cases/` に整理しています。
- 安全性、実用性、フォーマット遵守、部門適合性を確認する簡易評価ハーネスを含みます。

## What this is not

- 医療 AI 診断ツールではありません。
- 患者個別の判断支援ではありません。
- 電子カルテ連携ツールではありません。
- 診療記録や申し送り文を自動作成するものではありません。
- 患者説明文を生成するものではありません。
- 医療機関のルールや法令確認を代替するものではありません。

## Included Skills

| Skill | Role |
| --- | --- |
| `admin-workflow-consultant` | 非診療領域の事務作業、転記、紙運用、二重入力などを棚卸しし、改善案を整理します。 |
| `automation-planning-consultant` | RPA ありきではなく、Excel、Forms、CSV、SaaS、既存設定変更などの省力化手段を比較します。 |
| `hospital-document-drafter` | 院内お知らせ、依頼文、報告文、FAQ、研修案内などの非診療文書を作成します。 |
| `hospital-template-document-builder` | メモ、CSV、議事録などを既存 Excel / Word / PowerPoint / 院内様式に沿って整理します。 |
| `hospital-manual-builder` | 業務マニュアル、手順書、FAQ、チェックリスト、改訂案を作成します。 |
| `hospital-visual-material-designer` | 掲示物、研修資料、スライド、図解、画像生成プロンプト、代替レイアウト案を設計します。 |
| `survey-insight-analyst` | 研修アンケート、職員アンケート、自由記述を分類し、改善示唆を出します。 |
| `meeting-action-organizer` | 非診療領域の会議メモから決定事項、未決事項、担当者、期限、次回アクションを整理します。 |
| `training-program-designer` | 新人研修、AI リテラシー研修、管理職研修、職種別研修の構成を設計します。 |

## Installation / Import

### Repo-local Codex Skills

```bash
git clone https://github.com/Yuya-Ishibashi0/hospital-workflow-codex-skills.git
cd hospital-workflow-codex-skills
codex
```

Codex はリポジトリ内の `.agents/skills/` を読み取れます。このリポジトリ内で Codex を起動すると、Repo Skill として利用できます。明示的に使う場合は `$skill-name` のように呼べます。

Example:

```text
Use the $hospital-template-document-builder skill to organize this training survey summary into a hospital report template.
```

### User-level Codex Skills

```bash
mkdir -p ~/.agents/skills
cp -R .agents/skills/* ~/.agents/skills/
```

他のリポジトリでも使いたい場合は、ユーザー Skill としてコピーしてください。Skill が出てこない場合は Codex を再起動してください。今後は plugin 化も検討します。

詳しい手順は [docs/installation.md](docs/installation.md) を参照してください。

## Safety Policy

- 患者情報、実患者名、実在職員名、電子カルテ内容を入力しないでください。
- 対象は非診療領域に限定します。
- 診断、治療方針、患者個別の医療判断、患者説明文、診療記録、申し送り文には使いません。
- AI 出力はたたき台です。提出、掲示、配布、運用変更の前に必ず人間が確認してください。
- 院内規程、所属組織のルール、法令、委員会決定、管理者判断を優先してください。

詳細は [docs/safety-guidelines.md](docs/safety-guidelines.md) を参照してください。

## Use Cases by Department

- [Common](use-cases/common.md)
- [Nursing](use-cases/nursing.md)
- [Rehabilitation](use-cases/rehabilitation.md)
- [Medical Office](use-cases/medical-office.md)
- [General Affairs](use-cases/general-affairs.md)
- [Medical Staff Office](use-cases/medical-staff-office.md)
- [Education](use-cases/education.md)
- [Regional Cooperation](use-cases/regional-cooperation.md)

## Harness / Eval Cases

`harness/` は Skill の安全性、実用性、フォーマット遵守、部門適合性を確認するための簡易評価ハーネスです。初期版では手動評価と軽量なメタデータ検証を中心にします。将来的に `codex exec --json` による評価を追加する予定です。

```bash
python3 harness/scripts/validate_skill_metadata.py
python3 harness/scripts/generate_skill_index.py
```

## Contributing

Contribution Guide は [docs/contribution-guide.md](docs/contribution-guide.md) を参照してください。

## Issue Examples

初期公開後に登録しやすい改善 Issue の下書きを [.github/ISSUE_EXAMPLES/](.github/ISSUE_EXAMPLES/) にまとめています。

- Skill ごとの詳細なサンプル出力
- 部門別 use-case の追加
- `codex exec --json` 評価設計
- サンプル Excel / Word テンプレート
- Safety rubric のスコア化
- ChatGPT Skills / Codex plugin 化の設計メモ
