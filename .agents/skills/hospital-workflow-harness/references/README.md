# Harness

`harness/` は、Codex を病院の非診療業務改善タスクに適用するための実行制御レイヤーです。

ここは評価スクリプト置き場ではありません。Codex に対して、作業前提、スコープ、安全境界、タスク分類、Skill 選択、成果物の標準形式、人間確認ポイントを与えるための運用パッケージです。

## このディレクトリが定義すること

- Codex をどのような業務改善エージェントとして動かすか
- 依頼内容をどの作業モードに分けるか
- どの Skill / template を使うか
- どこまで Codex が判断してよいか
- どの成果物をどのファイル形式で出すか
- チャット欄に長文を貼らず、成果物ファイルとして保存するルール
- どの時点で人間、情報システム、法務、システム会社へ確認するか

## ファイル

| File | Role |
| --- | --- |
| `operating-model.md` | Codex の基本姿勢と作業の流れ |
| `task-routing.md` | 依頼種別ごとの Skill / template 選択 |
| `safety-boundaries.md` | 非診療・個人情報・医療安全の境界 |
| `output-contracts.md` | 成果物ごとの標準出力形式 |
| `artifact-output-policy.md` | 成果物をファイルとして作成するためのルール |
| `artifact-generation.md` | Office ファイル生成と検証の実行ルール |
| `run-lifecycle.md` | タスク状態、実行記録、引き渡し条件 |
| `human-review-policy.md` | 人間確認が必要な判断と確認先 |
| `workflow-modes.md` | discovery / structuring / proposal などの作業モード |

## 関連ディレクトリ

- `skills/`: Skill の正本。plugin 配布と保守はここを基準にする
- `.agents/skills/`: `skills/` から同期生成する repo-local ミラー
- `skills/hospital-workflow-harness/`: 安全確認から成果物作成までを統括するオーケストレーター
- `templates/`: 成果物の再現性を上げる出力テンプレート
- `tools/`: Skill メタデータ検証や索引生成などの保守ツール
- `evals/`: 将来の評価ケースやルーブリック

## 実行入口

通常の利用では、Skill名を指定する必要はありません。このリポジトリをCodexで開き、病院の非診療業務について日本語で依頼すると、`hospital-workflow-harness` が自動的に適用されます。

`$hospital-workflow-harness` は、動作を明示したい場合だけ使用する任意の指定です。

この入口が以下を順に行います。

1. 対象外領域と患者情報の確認
2. 作業モードの選択
3. 主 Skill と補助 Skill の選択
4. 成果物ファイルと保存先の決定
5. 専門 Skill による実行
6. 人間確認ポイントを付けた引き渡し
