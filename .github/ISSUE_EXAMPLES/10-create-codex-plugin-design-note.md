# Codex plugin の配布・更新フローを整備する

## 背景

`.codex-plugin/plugin.json`、plugin 用 `skills/`、user-level installer は実装済みです。次の段階として、GitHub から安全に導入・更新できる marketplace 配布とリリース手順を整える必要があります。

## 対象

- `.codex-plugin/plugin.json`
- `tools/install_user_harness.py`
- `docs/installation.md`
- リリース手順と marketplace 用メタデータ

## 追加したい内容

- Codex marketplace での配布方法を検証する。
- バージョン更新、互換性、ロールバック手順を文書化する。
- plugin manifest と Skill bundle のリリース前検証を自動化する。
- user-level installer との使い分けを明確にする。

## 安全上の制約

- plugin 配布によって患者情報や電子カルテ連携を扱う方向へ広げない。
- 同名 Skill を無断で上書きしない。
- 更新失敗時に旧版へ戻せること。

## 完了条件

- marketplace または同等の配布経路で導入検証が完了している。
- 更新とロールバックの手順が再現できる。
- `python3 tools/harness_doctor.py` がリリース前チェックに含まれる。
