# Skill ごとの NG 例を拡充する

## 背景

各 Skill は対象外業務を明記しているが、利用者が迷いやすい境界例をさらに示すと安全に使いやすくなる。特に患者情報、診療記録、申し送り、患者説明文に近づく依頼は明確に避ける必要がある。

## 対象

- `.agents/skills/*/SKILL.md`
- `.agents/skills/*/examples/`
- `docs/safety-guidelines.md`
- `harness/cases/`

## 追加したい内容

- 9 Skill それぞれに、少なくとも 2 件の NG 依頼例を追加する。
- NG 理由と、安全な言い換え例を添える。
- harness case に危険な依頼の判定例を追加する。

## 安全上の制約

- NG 例に実患者情報を含めない。
- 危険な出力そのものを長く再現しない。
- 安全な代替案は非診療・匿名化・人間確認を前提にする。

## 完了条件

- 9 Skill すべてに NG 例が追加されている。
- `docs/safety-guidelines.md` と矛盾しない。
- 少なくとも 2 件の harness case で NG 判定の観点が増えている。

