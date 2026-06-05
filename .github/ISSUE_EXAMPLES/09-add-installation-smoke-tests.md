# User-level installer のスモークテストを追加する

## 背景

`tools/install_user_harness.py` は競合検出、バックアップ、更新、アンインストールを扱うため、リリース前に一連の動作を自動確認する必要があります。

## 対象

- `tools/install_user_harness.py`
- `.github/workflows/validate.yml`
- `docs/installation.md`

## 追加したい内容

- 一時ディレクトリへの新規インストールを検証する。
- 同名 Skill がある場合に上書きせず停止することを検証する。
- `--force` でバックアップが作られることを検証する。
- 更新後も Skill リンクが有効であることを検証する。
- `--uninstall` が管理対象だけを削除することを検証する。

## 安全上の制約

- 実際の `~/.codex` を変更しない。
- テストは一時ディレクトリだけで実行する。
- 無関係なユーザー Skill を削除しない。

## 完了条件

- GitHub Actions 上でインストールライフサイクルが成功する。
- 競合時に既存ファイルが保持される。
- バックアップとアンインストールが再現可能である。
