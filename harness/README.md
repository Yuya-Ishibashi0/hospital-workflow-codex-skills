# Harness

## 目的

この harness は、Hospital Workflow Codex Skills が安全かつ実用的に動くかを確認するための簡易評価ハーネスです。

## 評価対象

- `.agents/skills/` の Skill 本体
- `use-cases/` の部門別ユースケース
- `examples/` と `harness/cases/` の架空ケース

## 手動評価の方法

1. `harness/cases/` からケースを選びます。
2. 使うべき Skill を明示して Codex に入力します。
3. `harness/graders/` のルーブリックで、安全性、実用性、フォーマット遵守、部門適合性を確認します。
4. NG 出力例に近い内容が出ていないか確認します。

## 軽量メタデータ検証

```bash
python3 harness/scripts/validate_skill_metadata.py
python3 harness/scripts/validate_skill_sections.py
python3 harness/scripts/generate_skill_index.py
```

`validate_skill_sections.py` は、各 `SKILL.md` に Purpose、When to use、When not to use、Inputs、Process、Output format、Safety constraints、Examples、Escalation / human review notes が含まれているかを確認します。

## 将来の自動評価方針

将来的に `codex exec --json` を使い、ケース入力、期待出力、ルーブリックをもとに自動評価できる形へ拡張します。初期版では手動評価と軽量なメタデータ検証を中心にします。
