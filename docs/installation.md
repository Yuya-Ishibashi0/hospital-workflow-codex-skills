# Installation

## Repo-local harness として使う

```bash
git clone https://github.com/Yuya-Ishibashi0/hospital-workflow-codex-skills.git
cd hospital-workflow-codex-skills
codex
```

この方法では、Codex が `AGENTS.md`、`.agents/skills/`、`harness/`、`templates/`、`use-cases/` を同じリポジトリ内で参照できます。

このリポジトリは単体の Skill 置き場ではなく、Codex を病院の非診療業務改善タスクに適用するための運用パッケージとして使います。まず `harness/README.md` と `harness/task-routing.md` を確認すると、どの依頼にどの Skill とテンプレートを使うか把握しやすくなります。

生成される成果物は、原則としてチャット本文ではなく `outputs/` 配下の `.docx`、`.xlsx`、`.pptx`、`.md`、`.csv` として保存します。

基本の呼び出し方:

```text
$hospital-workflow-harness
会議メモを整理し、議事録とアクション一覧をファイルで作成してください。
```

## User-level harness として導入する

```bash
python3 tools/install_user_harness.py --dry-run
python3 tools/install_user_harness.py
```

スクリプトは、ハーネス本体を Codex home に配置し、`skills/` のオーケストレーターと専門 Skill をユーザー Skill として参照できるようにします。導入後は Codex を再起動してください。

同名のユーザー Skill がすでに存在する場合、インストーラーは上書きせず停止します。内容を確認したうえで置き換える場合のみ `--force` を使います。置き換え対象は `~/.codex/backups/` に退避されます。

```bash
python3 tools/install_user_harness.py --force
```

アンインストールでは、このインストーラーが所有するリンクとハーネス本体だけを削除します。

```bash
python3 tools/install_user_harness.py --uninstall --dry-run
python3 tools/install_user_harness.py --uninstall
```

導入後は次のように明示できます。

```text
$hospital-workflow-harness
会議メモを整理し、議事録とアクション一覧をファイルで作成してください。
```

## 構造を診断する

```bash
python3 tools/harness_doctor.py
```

plugin manifest、Skill、harness 文書、templates の不足を確認します。

## 明示的に Skill を呼ぶ

```text
Use the $admin-workflow-consultant skill to organize duplicate Excel entry and paper transfer work into a low-risk improvement proposal.
```

```text
$meeting-action-organizer 非診療会議メモから決定事項、未決事項、担当、期限を整理してください。
```

## Skill が表示されない場合

- repo-local 利用では `.agents/skills/<skill-name>/SKILL.md` が存在するか確認します。
- user-level 利用では `~/.codex/skills/<skill-name>` がインストール先を指しているか確認します。
- `SKILL.md` の先頭に YAML frontmatter があるか確認します。
- `name` と `description` が入っているか確認します。
- Codex を再起動します。
- `python3 tools/validate_skill_metadata.py` でメタデータを確認します。

## Plugin 配布

`.codex-plugin/plugin.json` と plugin 用 `skills/` は追加済みです。今後は Codex marketplace からの配布、更新管理、ロールバック、リリース検証を整備します。

## 注意事項

患者情報、電子カルテ内容、実患者の状況、実在職員名は入力しないでください。診断、治療、患者説明、診療記録、申し送りには使わないでください。
