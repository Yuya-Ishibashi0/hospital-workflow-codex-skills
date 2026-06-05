# Run Lifecycle

ハーネスで実行する各タスクは、`outputs/YYYYMMDD-task-name/` を一つの作業単位として扱います。

## 必須ファイル

- `task-brief.md`: 依頼、範囲、モード、Skill、仮定、不足情報、成果物計画
- `run.json`: 実行状態と成果物一覧

## 状態

| Status | Meaning |
| --- | --- |
| `discovery` | 入力と不足情報を確認中 |
| `planned` | Skill、モード、成果物形式を決定済み |
| `in_progress` | 成果物を作成中 |
| `review_pending` | ファイル生成と機械検証が完了し、人間確認待ち |
| `completed` | 人間確認を経て利用可能 |
| `cancelled` | 対象外、情報不足、利用者判断などで中止 |

Codex は人間確認前に `completed` にしません。通常の引き渡し状態は `review_pending` です。

状態更新には次を使います。

```bash
python3 tools/update_task_run.py outputs/YYYYMMDD-task-name \
  --status planned \
  --primary-skill hospital-manual-builder

python3 tools/update_task_run.py outputs/YYYYMMDD-task-name \
  --status in_progress

python3 tools/update_task_run.py outputs/YYYYMMDD-task-name \
  --deliverable manual.docx \
  --purpose "新人向けマニュアル" \
  --status review_pending
```

人間確認後だけ、次を実行できます。

```bash
python3 tools/update_task_run.py outputs/YYYYMMDD-task-name \
  --status completed \
  --human-reviewed
```

## 成果物記録

`run.json` の `deliverables` は次の形式にします。

```json
[
  {
    "path": "manual.docx",
    "format": "docx",
    "purpose": "新人向け手順書",
    "validated": true
  }
]
```

## 完了条件

`review_pending` に進めるには、以下を満たす必要があります。

- 対象外領域を含まない。
- `task-brief.md` に仮定と不足情報が記載されている。
- 予定した成果物が存在する。
- Office ファイルが正しいパッケージ構造を持つ。
- 人間確認ポイントが明示されている。
