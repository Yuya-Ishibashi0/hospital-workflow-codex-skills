<p align="center">
  <img src="assets/hwcs-logo.png" alt="Hospital Workflow Codex Skills" width="760">
</p>

<p align="center">
  <strong>病院の非診療業務改善タスクに Codex を適用するための軽量エージェントハーネス</strong>
</p>

<p align="center">
  日本語 | <a href="README.en.md">English</a>
</p>

<p align="center">
  <strong>v0.2.0 development</strong>
  ·
  <a href="LICENSE">MIT License</a>
  ·
  <a href="harness/README.md">Harness</a>
  ·
  <a href="docs/safety-guidelines.md">安全方針</a>
</p>

# Hospital Workflow Codex Skills

このリポジトリは、病院の非診療領域における業務改善タスクを支援するための、**Codex 向け軽量エージェントハーネス**です。

単なる Skill 集ではなく、`AGENTS.md`、Codex Skills、業務テンプレート、タスクルーティング、安全境界、出力契約、保守ツールを組み合わせ、Codex が安全・再現性高く・目的通りに作業できるようにするための運用パッケージです。

## このリポジトリでいうハーネス

ここでのハーネスとは、Codex を病院業務改善タスクに適用するための **実行制御レイヤー** です。

このリポジトリは Codex 専用です。Claude Code / OpenCode など、他のエージェントランタイムへの対応は初期版の対象外です。

Codex に対して、以下をまとめて提供します。

- 作業前提
- 対象範囲
- 安全境界
- タスク分類
- Skill 選択
- 成果物テンプレート
- ファイル形式
- 人間確認ポイント
- 保守ツール

## 対象範囲

対象は、病院・医療機関における非診療領域の業務改善です。

- 二重入力・多重入力の整理
- 紙・Excel・Word への転記作業の削減
- 既存 Excel / Word / PowerPoint / 院内様式への情報整理
- 会議内容の整理
- 部門別マニュアル作成
- 院内文書、報告書、依頼文、FAQ の作成
- 研修資料、掲示物、スライド構成、図解案の作成
- 研修アンケート、職員アンケートの分析
- 自動化・省力化の検討

## 対象外

- 診療判断
- 医療上の助言
- 患者情報の処理
- 電子カルテ内容の分析
- 診断、治療方針、投薬判断
- 医療安全上の最終判断
- 個人情報を含む実データの無断利用

## 構成

```text
hospital-workflow-codex-skills/
  .codex-plugin/plugin.json
  AGENTS.md
  .agents/skills/
  skills/
  harness/
  templates/
  use-cases/
  tools/
  evals/
  examples/
```

| Directory | Role |
| --- | --- |
| `.codex-plugin/` | Codex plugin として配布するための manifest |
| `AGENTS.md` | Codex がこのリポジトリで守る上位ルール |
| `.agents/skills/` | repo-local 利用向けの Codex Skills |
| `skills/` | plugin 配布向けのオーケストレーターと専門 Skills |
| `harness/` | Codex の実行制御レイヤー |
| `templates/` | 提案書、議事録、業務フロー、既存様式整理などの成果物テンプレート |
| `use-cases/` | 代表的な業務改善シナリオ |
| `tools/` | Skill メタデータ検証、索引生成などの保守ツール |
| `evals/` | 将来の評価ケース、ルーブリック、回帰テスト |
| `examples/` | 利用例、サンプル成果物 |
| `outputs/` | Codex が生成した作業成果物の既定保存先 |

## Harness

`harness/` はこのリポジトリの中心です。

- [Operating model](harness/operating-model.md)
- [Task routing](harness/task-routing.md)
- [Safety boundaries](harness/safety-boundaries.md)
- [Output contracts](harness/output-contracts.md)
- [Artifact output policy](harness/artifact-output-policy.md)
- [Human review policy](harness/human-review-policy.md)
- [Workflow modes](harness/workflow-modes.md)

## 成果物の出力方針

このハーネスでは、Skill の成果物をチャット欄に長文で貼り付けるのではなく、原則としてファイルで作成します。

標準の保存先は `outputs/` です。

| 内容 | 標準形式 |
| --- | --- |
| マニュアル、報告書、依頼文、議事録 | `.docx` または `.md` |
| 対応表、チェックリスト、アンケート集計 | `.xlsx` または `.csv` |
| 研修資料、掲示物、スライド構成 | `.pptx` または `.md` |

チャットで返すのは、作成したファイル名、保存場所、確認ポイントの短い要約だけです。詳細は [Artifact output policy](harness/artifact-output-policy.md) を参照してください。

## 利用する主な Codex Skills

通常は `$hospital-workflow-harness` を入口として使います。このオーケストレーターが安全確認、作業モード選択、専門 Skill 選択、成果物ファイルの決定、人間確認までを統括します。

専門 Skill を明示的に使うこともできます。

| Skill | Role |
| --- | --- |
| `admin-workflow-consultant` | 二重入力、転記、紙運用、Excel 管理などの非診療業務フローを整理する |
| `automation-planning-consultant` | Excel、フォーム、CSV、共有フォルダ、既存システム設定などの省力化案を整理する |
| `hospital-template-document-builder` | メモ、CSV、アンケート結果を既存様式に沿って整理する |
| `meeting-action-organizer` | 非診療会議メモから決定事項、未決事項、担当、期限を整理する |
| `hospital-manual-builder` | 部門別マニュアル、手順書、FAQ、チェックリストを作成する |
| `hospital-document-drafter` | 院内向けの依頼文、報告文、周知文、相談文を作成する |
| `training-program-designer` | 研修、勉強会、AI リテラシー研修の構成を作成する |
| `hospital-visual-material-designer` | 掲示物、スライド、図解、画像生成プロンプトの構成を作成する |
| `survey-insight-analyst` | 研修アンケート、職員アンケート、自由記述を分析する |

新しい Skill を追加する場合は、まず `harness/task-routing.md`、`templates/`、`use-cases/` に反映し、既存 Skill の組み合わせでは扱えない独立した仕事かを確認します。

## Templates

`templates/` には、Codex の出力を安定させるための型を置きます。

- [業務ヒアリングシート](templates/workflow-hearing-sheet.md)
- [業務フロー整理](templates/workflow-map.md)
- [既存様式への情報整理](templates/template-document-mapping.md)
- [アンケート整理レポート](templates/survey-summary-report.md)
- [改善提案書](templates/proposal-outline.md)
- [会議整理](templates/meeting-minutes.md)
- [部門別マニュアル](templates/department-manual.md)
- [運用設計書](templates/operation-design.md)

## Use Cases

代表的な業務改善シナリオは [use-cases/](use-cases/) に置いています。

- [会議メモから TODO と論点を整理する](use-cases/meeting-to-actions.md)
- [部門別マニュアルを作る](use-cases/department-manual.md)
- [既存様式に情報を整理する](use-cases/template-document-organization.md)
- [研修アンケートを分析する](use-cases/training-survey-analysis.md)

## スクリーンショット掲載予定

このリポジトリでは、利用例を実画面のスクリーンショットで説明することを重視します。

掲載する画像は、実際に Codex / Computer Use で操作した画面に限定します。合成した説明画像や、実画面と異なるモック画像は使いません。

置き場:

```text
docs/assets/screenshots/
```

## 使い方

### Repo-local harness

最も簡単で安定した使い方です。

```bash
git clone https://github.com/Yuya-Ishibashi0/hospital-workflow-codex-skills.git
cd hospital-workflow-codex-skills
codex
```

Codex を起動したら、次のように依頼します。

```text
$hospital-workflow-harness
部署内の物品管理手順を整理し、新人向けマニュアルとチェックリストを作成してください。
```

Codex は `AGENTS.md`、harness、Skill、template を参照し、成果物を `outputs/` に保存します。

### User-level harness

他のリポジトリからも使う場合:

```bash
python3 tools/install_user_harness.py --dry-run
python3 tools/install_user_harness.py
```

導入後に Codex を再起動してください。`$hospital-workflow-harness` と専門 Skill がユーザー Skill として利用できるようになります。

同名 Skill がある場合は安全のため停止します。確認後に置き換える場合は `--force`、削除する場合は `--uninstall` を使います。置き換え前の内容は `~/.codex/backups/` に退避されます。

### Harness doctor

```bash
python3 tools/harness_doctor.py
```

plugin manifest、オーケストレーター、専門 Skill、harness 文書、templates の不足を確認します。

### Plugin package

このリポジトリには `.codex-plugin/plugin.json` と `skills/` が含まれ、Codex plugin としてパッケージできる構成になっています。

現在の確実な導入経路は repo-local harness と user-level installer です。Codex marketplace からの配布は今後のリリース工程として整備します。

## 保守ツール

`tools/` はハーネス本体ではなく、リポジトリを保守するための補助ツールです。

```bash
python3 tools/validate_skill_metadata.py
python3 tools/validate_skill_sections.py
python3 tools/generate_skill_index.py
```

リリース前の一括確認:

```bash
python3 tools/release_check.py
```

詳細は [Release checklist](docs/release-checklist.md) を参照してください。

## Evals

`evals/` は、将来の評価ケースやルーブリックを置く場所です。

- `harness/` = Codex をどう動かすかを定義する制御層
- `evals/` = Codex の出力をどう評価するかを扱う場所
- `tools/` = リポジトリ保守用スクリプト

## 安全方針

このハーネスでは、患者情報、電子カルテ内容、診療判断、患者説明文、診療記録、申し送り文を扱いません。

Codex の出力は、業務改善や文書化のたたき台です。運用変更、配布、掲示、外部送付、システム設定変更の前に、人間が確認してください。

詳しくは [harness/safety-boundaries.md](harness/safety-boundaries.md) と [harness/human-review-policy.md](harness/human-review-policy.md) を参照してください。

## License

[MIT License](LICENSE)
