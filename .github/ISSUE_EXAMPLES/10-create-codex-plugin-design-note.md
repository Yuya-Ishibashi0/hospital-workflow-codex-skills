# Codex plugin 化の設計メモを作成する

## 背景

README と installation guide では将来的な plugin 化に触れている。現時点では plugin 化しないが、配布方法、Skill 更新、利用者導線、安全レビューの観点を整理しておくと今後の判断がしやすい。

## 対象

- `docs/roadmap.md`
- `docs/installation.md`
- 新規設計メモ `docs/codex-plugin-design.md` など

## 追加したい内容

- plugin 化した場合のメリット、懸念、対象外を整理する。
- Skill 更新フロー、バージョン管理、レビュー観点を整理する。
- 初期版では repo-local / user-level Skill に留める理由を明記する。

## 安全上の制約

- plugin 化により患者情報や電子カルテ連携を扱う方向へ広げない。
- 院内導入時は組織のルール確認が必要であることを明記する。
- 自動更新や外部連携を前提にしない。

## 完了条件

- plugin 化の設計メモが追加されている。
- `docs/installation.md` または `docs/roadmap.md` から参照されている。
- 初期版では plugin 化しない理由が明確になっている。

