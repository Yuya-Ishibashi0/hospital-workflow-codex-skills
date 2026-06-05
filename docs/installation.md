# Installation

## Repo-local Skill として使う

```bash
git clone https://github.com/Yuya-Ishibashi0/hospital-workflow-codex-skills.git
cd hospital-workflow-codex-skills
codex
```

この方法では、Codex がリポジトリ内の `.agents/skills/` を読み取り、Repo Skill として利用できます。プロジェクト単位で試したい場合に向いています。

## 明示的に Skill を呼ぶ

```text
Use the $hospital-template-document-builder skill to organize this training survey summary into a hospital report template.
```

```text
$survey-insight-analyst 研修アンケートの自由記述を分類し、次回研修への示唆を出してください。
```

## User-level Skill としてコピーする

```bash
mkdir -p ~/.agents/skills
cp -R .agents/skills/* ~/.agents/skills/
```

他のリポジトリでも使いたい場合は、ユーザー Skill としてコピーしてください。コピー後に Skill が表示されない場合は Codex を再起動してください。

## Skill が表示されない場合

- `.agents/skills/<skill-name>/SKILL.md` が存在するか確認します。
- `SKILL.md` の先頭に YAML frontmatter があるか確認します。
- `name` と `description` が入っているか確認します。
- Codex を再起動します。
- `python3 harness/scripts/validate_skill_metadata.py` でメタデータを確認します。

## 将来的な plugin 化

初期版は repo-local / user-level Skill として提供します。将来的には Codex plugin としての配布、Skill の更新管理、評価ハーネスとの統合を検討します。

## 注意事項

患者情報、電子カルテ内容、実患者の状況、実在職員名は入力しないでください。診断、治療、患者説明、診療記録、申し送りには使わないでください。

