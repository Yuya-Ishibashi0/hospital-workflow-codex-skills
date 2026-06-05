# Tools

`tools/` は、ハーネスや Skill ライブラリを保守するための補助ツール置き場です。

ここにあるスクリプトはハーネス本体ではありません。Codex の実行制御レイヤーは `harness/` に置きます。

## Scripts

```bash
python3 tools/validate_skill_metadata.py
python3 tools/validate_skill_sections.py
python3 tools/generate_skill_index.py
python3 tools/harness_doctor.py
python3 tools/sync_repo_skills.py --check
python3 tools/sync_repo_skills.py --write
python3 tools/sync_harness_bundle.py --check
python3 tools/sync_harness_bundle.py --write
python3 tools/validate_artifacts.py outputs/YYYYMMDD-task-name
python3 tools/validate_harness_contracts.py
python3 tools/validate_markdown_links.py
python3 tools/smoke_test_harness.py
python3 tools/release_check.py
python3 tools/start_harness_task.py manual-update --title "部署内マニュアル改訂"
python3 tools/update_task_run.py outputs/YYYYMMDD-task-name --status planned --primary-skill hospital-manual-builder
python3 tools/install_user_harness.py --dry-run
```

## 役割

- Skill の frontmatter 確認
- Skill 必須セクション確認
- Skill 一覧の生成
- plugin / harness / templates の構造診断
- plugin 用 `skills/` から repo-local `.agents/skills/` への同期
- harness 文書と templates のオーケストレーターSkillへの同期
- 生成した DOCX / XLSX / PPTX / Markdown / CSV の構造検証
- routing、templates、eval cases、対象外の旧要件が混ざっていないかの検証
- README、docs、Issue下書きなどの相対リンク検証
- 一時環境でのタスク状態遷移、インストール、更新、競合保護、アンインストールの確認
- リリース前ゲートの一括実行
- 標準タスクフォルダと実行メタデータの作成
- タスク状態、使用 Skill、成果物、人間確認の記録
- ユーザー環境へのハーネス導入
