# Roadmap

## 0.2.x

- `harness/` を Codex の実行制御レイヤーとして整理
- `$hospital-workflow-harness` オーケストレーターの追加
- Codex plugin manifest と user-level installer の追加
- タスク状態、成果物検証、人間確認待ちの実行ライフサイクル整備
- 二重入力削減、既存様式整理、会議整理、マニュアル作成、研修アンケート分析の use-case 拡充
- `templates/` の成果物テンプレート追加
- `tools/` のメタデータ検証、必須セクション確認、Skill 一覧生成の改善
- `evals/` のケースとルーブリック整理

具体的な改善 Issue の下書きは `.github/ISSUE_EXAMPLES/` にあります。初期公開後は、この下書きをもとに優先度を付けて Issue 化します。

## 将来検討

- Codex marketplace からの配布と更新
- より本格的な `evals/` の整備
- `codex exec --json` による自動評価
- サンプル Excel / Word テンプレートの追加
- 多言語対応
- 部門別 use-case 拡充
- Markdown / PDF 出力

## 初期版に入れないもの

Claude Code、OpenCode、ローカル LLM、Web UI、Docker、API 連携、電子カルテ連携、患者情報を扱う処理は対象にしません。このリポジトリは Codex 専用の軽量ハーネスとして維持します。
