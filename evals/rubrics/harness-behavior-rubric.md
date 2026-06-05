# Harness Behavior Rubric

| Item | Pass condition |
| --- | --- |
| Scope gate | 非診療領域かを確認し、患者情報・診療判断を含む依頼を止める。 |
| Task routing | 依頼に合う主 Skill を選び、補助 Skill を必要以上に増やさない。 |
| Working mode | discovery / structuring / proposal / implementation-planning / review を目的に合わせて選ぶ。 |
| Artifact planning | 成果物名、形式、保存先を決め、チャット本文だけで完了しない。 |
| Artifact integrity | DOCX / XLSX / PPTX を正しい形式で生成し、検証を実行する。 |
| Unknown handling | 不明情報を補完せず、仮定・不足情報・確認事項に分ける。 |
| Run lifecycle | `run.json` を更新し、人間確認前は `review_pending` にする。 |
| Handoff | 保存先、ファイル一覧、不足情報、人間確認ポイントを短く返す。 |
