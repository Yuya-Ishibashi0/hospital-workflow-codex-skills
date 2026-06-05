# Contribution Guide

## 新しい Skill 追加の基準

新しい Skill は、既存 Skill の組み合わせでは明確に扱えない、独立した仕事がある場合だけ追加します。単なる文案、部署別バリエーション、出力形式の違いは、まず既存 Skill の examples、references、use-cases、templates に追加してください。

## まず既存 Skill にマッピングする

新しいアイデアを出す場合は、以下を確認してください。

- 推奨 Skill と補助 Skill を決められるか。
- 既存 Skill の `When to use` に含められるか。
- `harness/task-routing.md` に追記すれば運用できるか。
- `templates/` の追加や修正で足りるか。

## 新しい use-case 追加の方法

`use-cases/` の該当部門ファイルに、業務名、困りごと、推奨 Skill、補助 Skill、入力例、出力例、注意点、対象外を追加してください。

## 医療安全上の禁止事項

- 診断、治療判断、患者個別の医療判断に踏み込まない。
- 患者説明文を作らない。
- 診療記録や申し送り文を作らない。
- 電子カルテ連携や患者個人情報処理を追加しない。
- 実患者情報、実在病院名、実在職員名を使わない。

## examples、templates、evals

Skill を追加または大きく変更した場合は、examples、templates、use-cases、evals も確認してください。安全上の NG 出力例も必要に応じて `evals/` に追加します。

## Issue examples

初期公開後に扱いやすい改善 Issue の下書きは `.github/ISSUE_EXAMPLES/` にあります。Issue を作成する前に、以下を確認してください。

- 既存 Skill にマッピングできる改善か。
- 患者情報、診断、治療判断、患者説明文、診療記録、申し送りに関わらないか。
- examples、templates、use-cases、evals のどこを更新する必要があるか。
- 初期版に入れない Web UI、Docker、API 連携、電子カルテ連携に踏み込んでいないか。

## PR 前チェックリスト

- 患者情報を含んでいない。
- 診断、治療判断に踏み込んでいない。
- 対象外業務を明記している。
- Skill の成果物がチャット本文ではなくファイル出力を前提にしている。
- `skills/` を正本として編集した。
- harness または templates を変更した場合は `python3 tools/sync_harness_bundle.py --write` を実行した。
- `python3 tools/sync_repo_skills.py --write` を実行した。
- Skill 追加時は examples を追加した。
- Skill 追加時は task routing と templates を確認した。
- 必要に応じて evals のケースやルーブリックを更新した。
- use-case 追加時は推奨 Skill を明記した。
- README または docs を必要に応じて更新した。
- `python3 tools/harness_doctor.py` が成功した。
- `python3 tools/release_check.py` が成功した。
