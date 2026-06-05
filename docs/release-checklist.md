# Release Checklist

## 1. Scope and safety

- [ ] Codex 専用の非診療業務改善ハーネスという範囲を維持している
- [ ] 患者情報、診療判断、診療記録、申し送り、患者説明を扱っていない
- [ ] 実在病院名、実在職員名、実務データを examples / evals / screenshots に含めていない
- [ ] 成果物が人間確認前に `completed` にならない

## 2. Skill and harness synchronization

```bash
python3 tools/sync_harness_bundle.py --write
python3 tools/sync_repo_skills.py --write
```

- [ ] `skills/` が正本になっている
- [ ] `.agents/skills/` が正本と一致している
- [ ] オーケストレーター内の references / templates がルートと一致している

## 3. Automated checks

```bash
python3 tools/release_check.py
```

- [ ] Skill metadata
- [ ] 必須セクション
- [ ] plugin manifest
- [ ] routing / templates / eval cases
- [ ] installer lifecycle
- [ ] task lifecycle
- [ ] Python syntax

## 4. Artifact checks

- [ ] サンプル DOCX をWord互換アプリで開ける
- [ ] サンプル XLSX をExcel互換アプリで開ける
- [ ] サンプル PPTX がある場合はPowerPoint互換アプリで開ける
- [ ] 文字切れ、表崩れ、空白ページ、スライド重なりがない
- [ ] テキストファイルの拡張子をOffice形式へ変更していない

## 5. Documentation and version

- [ ] `.codex-plugin/plugin.json` の version を更新した
- [ ] `CHANGELOG.md` を更新した
- [ ] README / English README / installation guide が現在の導入方法と一致している
- [ ] スクリーンショットは実際のCodex操作画面だけを使用している

## 6. Publication

- [ ] Git差分に一時ファイルや生成物が含まれていない
- [ ] GitHub Actions が成功している
- [ ] タグとrelease noteがmanifest versionと一致している
