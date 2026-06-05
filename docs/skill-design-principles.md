# Skill Design Principles

## Non-clinical first

すべての Skill は非診療領域を対象にします。診断、治療、患者説明、診療記録、申し送りは対象外です。

## Human review required

AI 出力はたたき台です。院内に出す文書、業務変更案、研修資料、報告書は人間が確認します。

## Privacy by default

実患者情報、実在職員名、電子カルテ内容を入れない前提で設計します。例は架空で匿名化された非診療内容に限定します。

## Japanese hospital context

日本の病院に多い Excel、Word、PowerPoint、紙運用、委員会、部署間連携を前提にします。

## Practical over theoretical

理論よりも、明日から試せる整理、文案、チェックリスト、PoC 案を重視します。

## Existing formats matter

既存様式に合わせます。不明情報を勝手に補完せず、空欄や不足情報を明示します。

## Small-start improvement

大規模導入よりも、低リスクに小さく試せる改善案を優先します。

## Department-aware use cases

看護部、リハ部、医事課、総務課、医局、教育、地域連携など、読み手の文脈に合わせます。

## Do not over-create skills

Skill を増やしすぎません。新しいアイデアはまず use-cases に整理します。

## Map new ideas to existing skills first

新規 Skill を追加する前に、既存 Skill の入力例、出力例、references、harness case に追加できないか検討します。

